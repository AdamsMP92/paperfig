import numpy as np
import matplotlib.pyplot as plt
import pyvista as pv

def crop_image(img, left=0, right=0, top=0, bottom=0):
    h, w = img.shape[:2]
    return img[
        top : h - bottom,
        left : w - right
    ]

def Show_Axes_Margins(fig):
    for ax in fig.axes:
        bbox = ax.get_position()
        rect = plt.Rectangle(
            (bbox.x0, bbox.y0),
            bbox.width, bbox.height,
            transform=fig.transFigure,
            color="red", linewidth=1.5, linestyle="--",
            fill=False, zorder=1000
        )
        fig.patches.append(rect)

def add_reference_axes(plotter, length=0.5, radius=0.02, offset=0.8):
    colors = {"x": (1, 0, 0), "y": (0, 1, 0), "z": (0, 0, 1)}
    dirs   = {"x": [1, 0, 0], "y": [0, 1, 0], "z": [0, 0, 1]}
    origin = np.array([-offset, -offset, -offset])

    for key in dirs:
        arrow = pv.Arrow(
            start=origin, direction=dirs[key],
            tip_length=0.3, tip_radius=radius * 1.6,
            shaft_radius=radius, scale=length
        )
        plotter.add_mesh(arrow, color=colors[key], smooth_shading=True)
