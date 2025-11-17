from .figure import create_paper_figure, add_label_cm
from .panel_3d import quiver3_advanced_panel
from .panel_2d import add_colorbar_cm
from .panel_1d import plotScatter2D_panel_core


def PlotVectorfieldPanel(csv_path, figure_path,
                         coord_system="cart",   # "cart", "cyl", "sph", or "user"
                         color_func=None,
                         param_func=None,
                         vector_func=None,
                         magn_max=1.1):
    """
    Plot a 3D vector field with color-coded magnitude and 1D projection panel.
    Supports automatic coordinate transformation (cartesian, cylindrical,
    spherical) or user-defined mappings.

    Parameters
    ----------
    csv_path : str
        Path to CSV file containing columns x, y, z, mx, my, mz.
    figure_path : str
        Output figure filename (PNG).
    coord_system : str
        Coordinate mode: "cart", "cyl", "sph", or "user".
    color_func, param_func, vector_func : callable
        Custom mapping functions if coord_system="user".
    """

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib as mpl

    # ==========================================================
    # === Define built-in coordinate systems ===
    # ==========================================================
    def color_function(mx, my, mz):
        return mz / np.sqrt(mx**2 + my**2 + mz**2)  # default: color by z-component

    # ---------------- Cartesian ----------------
    def parameter_function_cart(x, y, z):
        xi = x
        Label = r"$x$ [nm]"
        return xi, Label

    def vector_transform_cart(x, y, z, mx, my, mz):
        return mx, my, mz, r"$m_x$", r"$m_y$", r"$m_z$"

    # ---------------- Cylindrical ----------------
    def parameter_function_cyl(x, y, z):
        rho = np.sqrt(x**2 + y**2)
        Label = r"$\rho$ [nm]"
        return rho, Label

    def vector_transform_cyl(x, y, z, mx, my, mz):
        rho = np.sqrt(x**2 + y**2)
        phi = np.arctan2(y, x)
        Mrho = mx * np.cos(phi) + my * np.sin(phi)
        Mphi = my * np.cos(phi) - mx * np.sin(phi)
        Mz = mz
        return Mrho, Mphi, Mz, r"$m_{\rho}$", r"$m_{\phi}$", r"$m_z$"

    # ---------------- Spherical ----------------
    def parameter_function_sph(x, y, z):
        r = np.sqrt(x**2 + y**2 + z**2)
        Label = r"$r$ [nm]"
        return r, Label

    def vector_transform_sph(x, y, z, mx, my, mz):
        # spherical unit vectors:
        # r̂ = (sinθ cosφ, sinθ sinφ, cosθ)
        # θ̂ = (cosθ cosφ, cosθ sinφ, -sinθ)
        # φ̂ = (-sinφ, cosφ, 0)
        r = np.sqrt(x**2 + y**2 + z**2)
        theta = np.arccos(np.clip(z / np.maximum(r, 1e-12), -1, 1))
        phi = np.arctan2(y, x)

        # Transform:
        Mr = mx * np.sin(theta) * np.cos(phi) + my * np.sin(theta) * np.sin(phi) + mz * np.cos(theta)
        Mtheta = mx * np.cos(theta) * np.cos(phi) + my * np.cos(theta) * np.sin(phi) - mz * np.sin(theta)
        Mphi = -mx * np.sin(phi) + my * np.cos(phi)

        return Mr, Mtheta, Mphi, r"$m_r$", r"$m_{\theta}$", r"$m_{\phi}$"

    # ==========================================================
    # === Select coordinate system ===
    # ==========================================================
    if coord_system == "cart":
        color_func = color_function
        param_func = parameter_function_cart
        vector_func = vector_transform_cart
    elif coord_system == "cyl":
        color_func = color_function
        param_func = parameter_function_cyl
        vector_func = vector_transform_cyl
    elif coord_system == "sph":
        color_func = color_function
        param_func = parameter_function_sph
        vector_func = vector_transform_sph
    elif coord_system == "user":
        if (color_func is None) or (param_func is None) or (vector_func is None):
            raise ValueError("For coord_system='user', provide all three mapping functions.")
    else:
        raise ValueError("coord_system must be 'cart', 'cyl', 'sph', or 'user'.")

    # ==========================================================
    # === Daten einlesen ===
    # ==========================================================
    cols = ['x', 'y', 'z', 'mx', 'my', 'mz']
    data = pd.read_csv(csv_path, sep=r"\s+", header=None, names=cols)
    data = data.apply(pd.to_numeric, errors="coerce").dropna()
    x, y, z = data['x'].values, data['y'].values, data['z'].values
    mx, my, mz = data['mx'].values, data['my'].values, data['mz'].values

    # ==========================================================
    # === Color coding & setup ===
    # ==========================================================
    C = color_func(mx, my, mz)

    fig_width_cm = 8.5
    fig_height_cm = 4.25
    y_shift1 = -0.25

    axes_width1_cm = 4.0
    axes_xPos1_cm = 0.3
    axes_yPos1_cm = 0.45 + y_shift1

    axes_width2_cm = 3.0
    axes_xPos2_cm = 5.0
    axes_yPos2_cm = 1.2 + y_shift1

    dpi_figure = 600
    fig = create_paper_figure(width_cm=fig_width_cm, height_cm=fig_height_cm,
                              dpi=dpi_figure, fontsize=7)

    add_label_cm(fig, r"(a)", axes_xPos1_cm-0.25, axes_yPos2_cm+axes_width2_cm,
                 fig_width_cm, fig_height_cm)
    add_label_cm(fig, r"(b)", axes_xPos2_cm-1.1, axes_yPos2_cm+axes_width2_cm,
                 fig_width_cm, fig_height_cm)

    # ==========================================================
    # === Panel (a): 3D Vector Field ===
    # ==========================================================
    ax1, im1 = quiver3_advanced_panel(
        fig, x, y, z, mx, my, mz, C,
        Cmin=-1.0, Cmax=1.0, margin_cm=0.0,
        scale=0.1, subsample=15, view="custom",
        dpi=800, cmap="rainbow",
        crop_cm=(0.0, 0.0, 0.0, 0.0),
        cam_pos=(3, -3, 2),
        focal_point=(0, 0, 0),
        up_direction=(0, 0, 1),
        axes_width_cm=axes_width1_cm,
        axes_pos_x_cm=axes_xPos1_cm,
        axes_pos_y_cm=axes_yPos1_cm
    )

    add_label_cm(fig, r"$x$", axes_xPos1_cm+0.5, axes_yPos2_cm-0.3,
                 fig_width_cm, fig_height_cm)
    add_label_cm(fig, r"$z$", axes_xPos1_cm+0.025, axes_yPos2_cm+0.7,
                 fig_width_cm, fig_height_cm)

    # === Colorbar ===
    cmap = plt.get_cmap("rainbow")
    norm = mpl.colors.Normalize(vmin=-1.0, vmax=1.0)
    sm = mpl.cm.ScalarMappable(norm=norm, cmap=cmap)
    sm.set_array([])
    add_colorbar_cm(fig, sm,
                    pos_cm=(0.1, 3.0),
                    size_cm=(0.1, 0.75),
                    clabel=r"$m_z$",
                    fontsize=4, ticks_fontsize=4,
                    orientation="vertical")

    # ==========================================================
    # === Panel (b): Scatter ===
    # ==========================================================
    parameter_1D, param_Label = param_func(x, y, z)
    M1, M2, M3, Label1, Label2, Label3 = vector_func(x, y, z, mx, my, mz)
    datasets = [
        {"x": parameter_1D, "y": M1, "label": Label1},
        {"x": parameter_1D, "y": M2, "label": Label2},
        {"x": parameter_1D, "y": M3, "label": Label3}
    ]

    ax2 = plotScatter2D_panel_core(
        fig, datasets,
        pos_cm=(axes_xPos2_cm, axes_yPos2_cm),
        size_cm=(axes_width2_cm, axes_width2_cm),
        xlabel=param_Label,
        ylabel=None,
        markersize=1,
        alpha=1.0,
        ylim=[-magn_max, magn_max],
        colors=["#D55E00", "#0072B2", "#009E73"]
    )

    ax2.grid(True, linestyle="-", color="0.8", linewidth=0.1)
    ax2.tick_params(direction="in", width=0.4, length=1.0,
                    top=True, right=True)

    fig.savefig(figure_path, bbox_inches=None, pad_inches=0, facecolor="white")
    plt.close(fig)
    print(f"✅ Saved figure: {figure_path}")
