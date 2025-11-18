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


def apply_tick_style(
        ax,
        show_ticks=True,
        ticks_fontsize=6,
        major_tick_length=2.5,
        major_tick_width=0.45,
        minor_tick_length=1.5,
        minor_tick_width=0.35,
        xticks=None,
        yticks=None,
        xticklabels=None,
        yticklabels=None
):
    """Unified tick styling for 1D and 2D plots."""

    if not show_ticks:
        ax.set_xticks([])
        ax.set_yticks([])
        return ax

    # Set tick positions
    if xticks is not None:
        ax.set_xticks(xticks)
        if xticklabels is not None:
            ax.set_xticklabels(xticklabels, fontsize=ticks_fontsize)

    if yticks is not None:
        ax.set_yticks(yticks)
        if yticklabels is not None:
            ax.set_yticklabels(yticklabels, fontsize=ticks_fontsize)

    # Major ticks
    ax.tick_params(
        which="major",
        direction="in",
        labelsize=ticks_fontsize,
        length=major_tick_length,
        width=major_tick_width,
        top=True,
        right=True
    )

    # Minor ticks
    ax.tick_params(
        which="minor",
        direction="in",
        length=minor_tick_length,
        width=minor_tick_width,
        top=True,
        right=True
    )

    ax.minorticks_on()
    return ax

