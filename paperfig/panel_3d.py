import numpy as np
import matplotlib.pyplot as plt
import pyvista as pv
from .figure import add_axes_cm
from .utils import crop_image, add_reference_axes

def quiver3_advanced(
    x, y, z, Hx, Hy, Hz, C,
    cmap="viridis",
    scale=1.0,
    f_head_length=4.0/6.0,
    f_stick_radius=1.0/6.0,
    f_head_radius=1.0/3.0,
    centering=True,
    subsample=1
):
    """
    High-quality 3D quiver visualization (MATLAB-style) with proportional geometry.

    Parameters
    ----------
    x, y, z : array-like
        Coordinates of vector origins.
    Hx, Hy, Hz : array-like
        Vector components.
    C : array-like
        Scalar field used for color mapping.
    cmap : str
        Matplotlib colormap name.
    scale : float
        Global scaling factor for all arrow dimensions.
    f_head_length : float
        Head length as a fraction of stick_length.
    f_stick_radius : float
        Stick radius as a fraction of stick_length.
    f_head_radius : float
        Head radius as a fraction of stick_length.
    centering : bool
        If True, arrows are centered on (x,y,z).
    subsample : int
        Draw every n-th arrow for performance.
    """

    # ===== Geometry scaling =====
    stick_length = 1.0 * scale
    head_length  = f_head_length * stick_length
    stick_radius = f_stick_radius * stick_length
    head_radius  = f_head_radius * stick_length

    # ===== Normalize directions =====
    H = np.stack([Hx, Hy, Hz], axis=1)
    H /= np.linalg.norm(H, axis=1)[:, None]

    # ===== Color mapping =====
    cmap_func = plt.get_cmap(cmap)
    scalars = (C - np.min(C)) / (np.max(C) - np.min(C))
    colors = cmap_func(scalars)[:, :3]  # RGB (ignore alpha)

    # ===== Plot setup =====
    plotter = pv.Plotter(window_size=[900, 800])
    plotter.enable_anti_aliasing('ssaa')

    # ===== Draw arrows =====
    for i in range(0, len(x), subsample):
        p0 = np.array([x[i], y[i], z[i]])
        direction = H[i]
        color = colors[i]
        print("quiver3 build progress: " + str(i/len(x)*100) + " %")
        arrow = pv.Cylinder(
            center=p0 + direction * stick_length/2 if not centering else p0,
            direction=direction,
            radius=stick_radius,
            height=stick_length
        )
        cone = pv.Cone(
            center=p0 + direction * (stick_length + head_length/2) if not centering else p0 + direction*(stick_length/2),
            direction=direction,
            height=head_length,
            radius=head_radius
        )

        actor = arrow.merge(cone)
        plotter.add_mesh(actor, color=color, smooth_shading=True, specular=0.3)

    # ===== Scene =====
    plotter.set_background("white")
    plotter.add_axes(line_width=2)
    plotter.show()


def quiver3_advanced_panel(
        fig, x, y, z, Hx, Hy, Hz, C, Cmin, Cmax,
        cmap="viridis",
        scale=1.0,
        f_head_length=4.0 / 6.0,
        f_stick_radius=1.0 / 6.0,
        f_head_radius=1.0 / 3.0,
        centering=True,                # Pfeil um (x,y,z) zentrieren (True) oder bei (x,y,z) starten (False)
        subsample=1,
        view="iso",
        dpi=300,
        background="white",
        axes_width_cm=None,
        axes_pos_x_cm=None,
        axes_pos_y_cm=None,
        margin_cm=0.0,
        crop_cm=(0, 0, 0, 0),
        cam_pos=(3, 3, 2),  # camera position (x,y,z)
        focal_point=(0, 0, 0),  # focal point (center of scene)
        up_direction=(0, 0, 1)
):
    """
    Returns a rendered image (NumPy array) of a 3D quiver field panel.

    centering=True:
        Each arrow is centered around its reference point (x,y,z),
        i.e., half of the shaft extends forward, half backward.

    normalize_coords=True:
        Centers and normalizes (x,y,z) to fit roughly within [-1,1]^3
        for consistent scaling across datasets.
    """

    # ===== Convert input to numpy arrays =====
    x = np.asarray(x)
    y = np.asarray(y)
    z = np.asarray(z)
    Hx = np.asarray(Hx)
    Hy = np.asarray(Hy)
    Hz = np.asarray(Hz)
    C  = np.asarray(C)

    # ===== coordinate centering and normalization =====
    coords = np.stack([x, y, z], axis=1)
    center = np.mean(coords, axis=0)
    coords -= center
    max_dist = np.max(np.linalg.norm(coords, axis=1))
    coords /= max_dist
    x, y, z = coords[:, 0], coords[:, 1], coords[:, 2]

    # ===== Geometry scaling =====
    stick_length = 1.0 * scale
    head_length  = f_head_length * stick_length
    stick_radius = f_stick_radius * stick_length
    head_radius  = f_head_radius * stick_length
    L_tot = head_length + stick_length

    # ===== Normalize directions =====
    H = np.stack([Hx, Hy, Hz], axis=1)
    H_norm = np.linalg.norm(H, axis=1)
    H_norm[H_norm == 0] = 1.0
    H /= H_norm[:, None]

    # ===== Color mapping =====
    # Cmin = np.min(C)
    # Cmax = np.max(C)
    cmap_func = plt.get_cmap(cmap)
    scalars = (C - Cmin) / (Cmax - Cmin + 1e-12)
    colors = cmap_func(scalars)[:, :3]

    # ===== Determine render window size =====
    if axes_width_cm is not None:
        pixels = int((axes_width_cm / 2.54) * dpi)
        window_size = [pixels, pixels]
    else:
        window_size = [800, 800]

    # ===== Create PyVista plotter =====
    plotter = pv.Plotter(off_screen=True, window_size=window_size)
    plotter.set_background(background)
    plotter.enable_anti_aliasing('ssaa')

    # ===== Draw arrows =====
    N = len(x)
    for i in range(0, N, subsample):
        p0 = np.array([x[i], y[i], z[i]])
        direction = H[i]
        color = colors[i]

        # --- Grundposition: Pfeil startet bei p0 ---
        arrow_center = p0 + direction * (stick_length / 2)
        cone_center = p0 + direction * (stick_length + head_length / 2)

        if centering:
            # Gesamten Pfeil um halbe Gesamtlänge nach hinten schieben
            arrow_center -= direction * (L_tot / 2)
            cone_center -= direction * (L_tot / 2)

        # --- Erzeuge Geometrien ---
        arrow = pv.Cylinder(
            center=arrow_center,
            direction=direction,
            radius=stick_radius,
            height=stick_length
        )
        cone = pv.Cone(
            center=cone_center,
            direction=direction,
            height=head_length,
            radius=head_radius
        )

        actor = arrow.merge(cone)
        plotter.add_mesh(actor, color=color, smooth_shading=True, specular=0.3)

        print(f"quiver3 build progress:" + str(round(100 * i / N, 3)) + " %")

    # ===== Camera view setup =====
    if view == "iso":
        plotter.view_isometric()
    elif view == "xy":
        plotter.view_xy()
    elif view == "xz":
        plotter.view_xz()
    elif view == "yz":
        plotter.view_yz()
    elif view == "top":
        plotter.camera_position = [(0, 0, 1), (0, 0, 0), (0, 1, 0)]
    elif view == "custom":
        plotter.camera_position = [
            cam_pos,  # camera position (x,y,z)
            focal_point,  # focal point (center of scene)
            up_direction # "up" direction
        ]

    # ===== Margin control (zoom out for margin) =====
    if margin_cm > 0 and axes_width_cm is not None:
        zoom_factor = axes_width_cm / (axes_width_cm + 2 * margin_cm)
        plotter.camera.zoom(zoom_factor)

    # ===== Optional: add small axis cross =====
    try:
        add_reference_axes(plotter, length=0.5, radius=0.015, offset=0.8)
    except Exception:
        pass

    #plotter.show_axes()  # kleines Overlay

    # ===== Render image =====
    img = plotter.screenshot(return_img=True)
    plotter.close()

    # ===== Cropping (cm → px) =====
    if crop_cm != (0, 0, 0, 0):
        px_per_cm = dpi / 2.54
        crop_px = tuple(int(c * px_per_cm) for c in crop_cm)
        img = crop_image(img, *crop_px)

    ax = add_axes_cm(fig, axes_pos_x_cm, axes_pos_y_cm, axes_width_cm, axes_width_cm)
    ax.imshow(img)
    ax.axis("off")

    return ax, img
