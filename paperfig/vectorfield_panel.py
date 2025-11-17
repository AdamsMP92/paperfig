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


###########################################################################
def plot_vectorfield_panels(
        fig,
        x, y, z,
        mx, my, mz,
        coord_system="cart",              # "cart", "cyl", "sph", "user"
        color_func=None,
        param_func=None,
        vector_func=None,
        magn_max=1.1,

        # --- Panel (a): 3D vector field ---
        panelA_pos_cm=(0.5, 0.5),
        panelA_size_cm=(4.0, 4.0),

        # --- Colorbar ---
        colorbar_pos_cm=(5.0, 0.5),
        colorbar_size_cm=(0.2, 3.0),
        cmap="rainbow",

        # --- Panel (b): 1D projection ---
        panelB_pos_cm=(7.0, 0.8),
        panelB_size_cm=(4.0, 3.5),

        # --- Labels ---
        labelA="(a)",
        labelB="(b)",
        add_labels=True,
        fig_width_cm=8.5,
        fig_height_cm=6.0
):
    """
    Attach two vectorfield panels (3D quiver + 1D projection) to an *existing* figure.
    Input data are raw arrays, not a CSV file.
    Panel placement fully controlled by cm-coordinates.
    """

    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib as mpl

    # ==========================================================
    # === Built-in coordinate systems
    # ==========================================================

    def default_color(mx, my, mz):
        return mz / np.sqrt(mx**2 + my**2 + mz**2 + 1e-12)

    # ---------------- Cartesian ----------------
    def parameter_cart(x, y, z):
        return x, r"$x$ [nm]"

    def vector_cart(x, y, z, mx, my, mz):
        return mx, my, mz, r"$m_x$", r"$m_y$", r"$m_z$"

    # ---------------- Cylindrical ----------------
    def parameter_cyl(x, y, z):
        rho = np.sqrt(x**2 + y**2)
        return rho, r"$\rho$ [nm]"

    def vector_cyl(x, y, z, mx, my, mz):
        rho = np.sqrt(x**2 + y**2)
        phi = np.arctan2(y, x)
        Mrho = mx * np.cos(phi) + my * np.sin(phi)
        Mphi = my * np.cos(phi) - mx * np.sin(phi)
        return Mrho, Mphi, mz, r"$m_{\rho}$", r"$m_{\phi}$", r"$m_z$"

    # ---------------- Spherical ----------------
    def parameter_sph(x, y, z):
        r = np.sqrt(x**2 + y**2 + z**2)
        return r, r"$r$ [nm]"

    def vector_sph(x, y, z, mx, my, mz):
        r = np.sqrt(x**2 + y**2 + z**2 + 1e-12)
        theta = np.arccos(np.clip(z / r, -1, 1))
        phi = np.arctan2(y, x)

        Mr =  (mx * np.sin(theta) * np.cos(phi)
              + my * np.sin(theta) * np.sin(phi)
              + mz * np.cos(theta))

        Mtheta = (mx * np.cos(theta) * np.cos(phi)
                 + my * np.cos(theta) * np.sin(phi)
                 - mz * np.sin(theta))

        Mphi = -mx * np.sin(phi) + my * np.cos(phi)

        return Mr, Mtheta, Mphi, r"$m_r$", r"$m_\theta$", r"$m_\phi$"

    # ==========================================================
    # === Select coordinate mode
    # ==========================================================

    if coord_system == "cart":
        color_func = default_color
        param_func = parameter_cart
        vector_func = vector_cart
    elif coord_system == "cyl":
        color_func = default_color
        param_func = parameter_cyl
        vector_func = vector_cyl
    elif coord_system == "sph":
        color_func = default_color
        param_func = parameter_sph
        vector_func = vector_sph
    elif coord_system == "user":
        if color_func is None or param_func is None or vector_func is None:
            raise ValueError("For user mode, supply color_func, param_func, vector_func.")
    else:
        raise ValueError("coord_system must be 'cart', 'cyl', 'sph', or 'user'.")

    # ==========================================================
    # === Color coding ===
    # ==========================================================

    C = color_func(mx, my, mz)

    # ==========================================================
    # === Panel (a): 3D vector field ===
    # ==========================================================

    axA, imA = quiver3_advanced_panel(
        fig, x, y, z, mx, my, mz, C,
        Cmin=-1.0,
        Cmax=1.0,
        cmap=cmap,
        axes_pos_x_cm=panelA_pos_cm[0],
        axes_pos_y_cm=panelA_pos_cm[1],
        axes_width_cm=panelA_size_cm[0],
        margin_cm=0.0
    )

    # Label (a)
    if add_labels:
        add_label_cm(fig, labelA,
                     panelA_pos_cm[0] - 0.3,
                     panelA_pos_cm[1] + panelA_size_cm[1] + 0.2,
                     fig_width_cm, fig_height_cm)

    # ==========================================================
    # === Colorbar ===
    # ==========================================================

    sm = mpl.cm.ScalarMappable(
        norm=mpl.colors.Normalize(vmin=-1.0, vmax=1.0),
        cmap=cmap
    )
    sm.set_array([])

    add_colorbar_cm(
        fig,
        pos_cm=colorbar_pos_cm,
        size_cm=colorbar_size_cm,
        vmin=-1.0,
        vmax=1.0,
        cmap=cmap,
        clabel=r"$m_z$"
    )

    # ==========================================================
    # === Panel (b): 1D projection ===
    # ==========================================================

    param_vals, xlabel = param_func(x, y, z)
    M1, M2, M3, L1, L2, L3 = vector_func(x, y, z, mx, my, mz)

    datasets = [
        {"x": param_vals, "y": M1, "label": L1},
        {"x": param_vals, "y": M2, "label": L2},
        {"x": param_vals, "y": M3, "label": L3},
    ]

    axB = plotScatter2D_panel_core(
        fig, datasets,
        pos_cm=panelB_pos_cm,
        size_cm=panelB_size_cm,
        xlabel=xlabel,
        ylabel=None,
        ylim=[-magn_max, magn_max],
        markersize=1.0
    )

    axB.grid(True, linestyle="-", color="0.8", linewidth=0.1)
    axB.tick_params(direction="in", width=0.4, length=1.0, top=True, right=True)

    # Label (b)
    if add_labels:
        add_label_cm(fig, labelB,
                     panelB_pos_cm[0] - 0.3,
                     panelB_pos_cm[1] + panelB_size_cm[1] + 0.2,
                     fig_width_cm, fig_height_cm)

    return axA, axB

