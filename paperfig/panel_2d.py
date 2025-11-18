import numpy as np
from .figure import add_axes_cm
from .utils import apply_tick_style
import matplotlib as mpl

def plot2D_panel_core(
        fig, x, y, Z,
        pos_cm=(0, 0),
        size_cm=(3.5, 3.5),
        cmap="plasma",
        xlabel="x",
        ylabel="y",
        title=None,
        vmin=None,
        vmax=None,
        xlim=None,
        ylim=None,
        xticks=None,
        yticks=None,
        xticklabels=None,
        yticklabels=None,
        fontsize=7,
        ticks_fontsize=6,
        show_ticks=True,
        aspect="equal",
        major_tick_length=2.0,
        major_tick_width=0.45,
        minor_tick_length=1.2,
        minor_tick_width=0.35
):
    """2D imshow panel with unified tick style."""
    
    ax = add_axes_cm(fig, pos_cm[0], pos_cm[1], size_cm[0], size_cm[1])

    im = ax.imshow(
        Z,
        extent=[x.min(), x.max(), y.min(), y.max()],
        cmap=cmap,
        origin="lower",
        vmin=vmin,
        vmax=vmax,
        aspect=aspect
    )

    # Limits
    if xlim is not None:
        ax.set_xlim(xlim)
    if ylim is not None:
        ax.set_ylim(ylim)

    # Unified ticks
    apply_tick_style(
        ax,
        show_ticks,
        ticks_fontsize,
        major_tick_length,
        major_tick_width,
        minor_tick_length,
        minor_tick_width,
        xticks,
        yticks,
        xticklabels,
        yticklabels
    )

    # Labels and title
    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)

    if title:
        ax.set_title(title, fontsize=fontsize, pad=1.5)

    return ax, im


def plot2D_pcolormesh_panel_core(
        fig, x, y, Z,
        pos_cm=(0, 0),
        size_cm=(3.5, 3.5),
        cmap="plasma",
        xlabel="x",
        ylabel="y",
        title=None,
        vmin=None,
        vmax=None,
        xlim=None,
        ylim=None,
        xticks=None,
        yticks=None,
        xticklabels=None,
        yticklabels=None,
        fontsize=7,
        ticks_fontsize=6,
        show_ticks=True,
        aspect="equal",
        shading="auto",
        major_tick_length=2.0,
        major_tick_width=0.45,
        minor_tick_length=1.2,
        minor_tick_width=0.35
):
    """2D pcolormesh panel with unified tick style and custom labels."""

    ax = add_axes_cm(fig, pos_cm[0], pos_cm[1], size_cm[0], size_cm[1])

    x = np.asarray(x)
    y = np.asarray(y)

    if x.ndim == 1 and y.ndim == 1:
        X, Y = np.meshgrid(x, y)
    else:
        X, Y = x, y

    mesh = ax.pcolormesh(
        X, Y, Z,
        cmap=cmap,
        shading=shading,
        vmin=vmin,
        vmax=vmax
    )

    if xlim is not None:
        ax.set_xlim(xlim)
    if ylim is not None:
        ax.set_ylim(ylim)

    apply_tick_style(
        ax,
        show_ticks,
        ticks_fontsize,
        major_tick_length,
        major_tick_width,
        minor_tick_length,
        minor_tick_width,
        xticks,
        yticks,
        xticklabels,
        yticklabels
    )

    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)
    if title:
        ax.set_title(title, fontsize=fontsize, pad=1.5)

    ax.set_aspect(aspect)
    return ax, mesh




def add_colorbar_cm(
        fig,
        pos_cm=(0, 0),
        size_cm=(0.2, 3.5),
        vmin=0.0,
        vmax=1.0,
        cmap="viridis",
        clabel=None,
        fontsize=7,
        ticks_fontsize=6,
        ticks=None,
        major_tick_length=2.0,
        major_tick_width=0.45,
        minor_tick_length=1.0,
        minor_tick_width=0.35,
        tick_direction="in",
        orientation="vertical"
):
    """Colorbar with unified tick styling."""

    cax = add_axes_cm(fig, pos_cm[0], pos_cm[1], size_cm[0], size_cm[1])

    norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax)
    sm = mpl.cm.ScalarMappable(norm=norm, cmap=cmap)
    sm.set_array([])

    cbar = fig.colorbar(sm, cax=cax, orientation=orientation)

    if ticks is not None:
        cbar.set_ticks(ticks)

    cbar.ax.tick_params(
        which="major",
        labelsize=ticks_fontsize,
        direction=tick_direction,
        length=major_tick_length,
        width=major_tick_width
    )

    if clabel:
        cbar.set_label(clabel, fontsize=fontsize)

    return cbar


