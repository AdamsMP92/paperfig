import numpy as np
import matplotlib.pyplot as plt
import pyvista as pv
import matplotlib.ticker as mticker

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
        yticklabels=None, 
        disable_xticklabels=False,
        disable_yticklabels=False
):
    """Unified tick styling for 1D and 2D plots."""

    if not show_ticks:
        ax.set_xticks([])
        ax.set_yticks([])
        return ax

    # --------------------------------------------------------------------
    # IMPORTANT: Enable minor ticks FIRST so they don't overwrite later.
    # --------------------------------------------------------------------
    ax.minorticks_on()
    
    # --------------------------------------------------------------------
    # First SET tick positions so formatter knows what to label
    # --------------------------------------------------------------------
    if xticks is not None:
        ax.set_xticks(xticks)
    if yticks is not None:
        ax.set_yticks(yticks)

    # --------------------------------------------------------------------
    # IF NOT disabled: apply custom ticklabels (if provided)
    # --------------------------------------------------------------------
    if not disable_xticklabels and xticklabels is not None:
        ax.set_xticklabels(xticklabels, fontsize=ticks_fontsize)

    if not disable_yticklabels and yticklabels is not None:
        ax.set_yticklabels(yticklabels, fontsize=ticks_fontsize)

    # --------------------------------------------------------------------
    # Aesthetics
    # --------------------------------------------------------------------
    ax.tick_params(
        which="major",
        direction="in",
        labelsize=ticks_fontsize,
        length=major_tick_length,
        width=major_tick_width,
        top=True,
        right=True
    )

    ax.tick_params(
        which="minor",
        direction="in",
        length=minor_tick_length,
        width=minor_tick_width,
        top=True,
        right=True
    )

    # --------------------------------------------------------------------
    # Disable tick labels (strong version – overrides ANY formatter)
    # --------------------------------------------------------------------
    if disable_xticklabels:
        ax.set_xticklabels([])
        ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda *args: ""))
        ax.xaxis.set_minor_formatter(mticker.FuncFormatter(lambda *args: ""))
        ax.tick_params(labelbottom=False)

    if disable_yticklabels:
        ax.set_yticklabels([])
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda *args: ""))
        ax.yaxis.set_minor_formatter(mticker.FuncFormatter(lambda *args: ""))
        ax.tick_params(labelleft=False)
    
    return ax



def apply_grid_style(
        ax,
        show=True,
        major=True,
        minor=False,
        major_linestyle="-",
        minor_linestyle=":",
        major_color="0.85",
        minor_color="0.9",
        major_linewidth=0.3,
        minor_linewidth=0.2,
        alpha=1.0
):
    """
    Unified, publication-ready grid styling for any Axes.
    """

    if not show:
        ax.grid(False)
        return ax

    # Major grid
    if major:
        ax.grid(
            True,
            which="major",
            linestyle=major_linestyle,
            linewidth=major_linewidth,
            color=major_color,
            alpha=alpha
        )

    # Minor grid
    if minor:
        ax.grid(
            True,
            which="minor",
            linestyle=minor_linestyle,
            linewidth=minor_linewidth,
            color=minor_color,
            alpha=alpha
        )

    return ax


def apply_label_style(
        ax,
        xlabel=None,
        ylabel=None,
        title=None,
        fontsize=7,
        labelpad=1.5,
        titlepad=1.5
):
    """
    Unified labeling for axes: xlabel, ylabel, and title.
    Clean, consistent, and compact.
    """

    if xlabel is not None:
        ax.set_xlabel(xlabel, fontsize=fontsize, labelpad=labelpad)

    if ylabel is not None:
        ax.set_ylabel(ylabel, fontsize=fontsize, labelpad=labelpad)

    if title is not None:
        ax.set_title(title, fontsize=fontsize, pad=titlepad)

    return ax

