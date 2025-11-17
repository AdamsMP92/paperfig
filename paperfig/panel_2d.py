import numpy as np
from .figure import add_axes_cm

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
        fontsize=7,
        ticks_fontsize=6,
        show_ticks=True,
        aspect="equal"
):
    """Create a fixed-size 2D map panel without colorbar."""
    ax = add_axes_cm(fig, pos_cm[0], pos_cm[1], size_cm[0], size_cm[1])
    im = ax.imshow(
        Z, extent=[x.min(), x.max(), y.min(), y.max()],
        cmap=cmap, origin="lower",
        vmin=vmin, vmax=vmax, aspect=aspect
    )

    if show_ticks:
        ax.tick_params(labelsize=ticks_fontsize,
                       width=0.4,
                       length=1.8)
        ax.tick_params(direction="in",
                       length=1.0,
                       width=0.5,
                       top=True,
                       right=True)
    else:
        ax.set_xticks([]); ax.set_yticks([])

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
        fontsize=7,
        ticks_fontsize=6,
        show_ticks=True,
        aspect="equal",
        shading="auto"
):
    """
    Create a fixed-size 2D map panel using pcolormesh.
    Supports:
      - x,y as 1D axes
      - x,y as 2D meshgrid
    """

    # ------------------------------------------------------------
    # Create axes in cm coordinates
    # ------------------------------------------------------------
    ax = add_axes_cm(fig, pos_cm[0], pos_cm[1], size_cm[0], size_cm[1])

    # ------------------------------------------------------------
    # Normalize x and y into meshgrid (pcolormesh requires 2D)
    # ------------------------------------------------------------
    x = np.asarray(x)
    y = np.asarray(y)

    # Case 1: x,y are 1D → build meshgrid
    if x.ndim == 1 and y.ndim == 1:
        X, Y = np.meshgrid(x, y)

    # Case 2: x,y already 2D → use directly
    elif x.ndim == 2 and y.ndim == 2:
        X, Y = x, y

    else:
        raise ValueError("x and y must be either both 1D or both 2D arrays")

    # ------------------------------------------------------------
    # 2D color plotting via pcolormesh
    # ------------------------------------------------------------
    mesh = ax.pcolormesh(
        X, Y, Z,
        cmap=cmap,
        shading=shading,
        vmin=vmin,
        vmax=vmax
    )

    # ------------------------------------------------------------
    # Apply axis limits if given
    # ------------------------------------------------------------
    if xlim is not None:
        ax.set_xlim(xlim)
    if ylim is not None:
        ax.set_ylim(ylim)

    # ------------------------------------------------------------
    # Tick styling
    # ------------------------------------------------------------
    if show_ticks:
        ax.tick_params(labelsize=ticks_fontsize,
                       width=0.4,
                       length=1.8)
        ax.tick_params(direction="in",
                       length=1.0,
                       width=0.5,
                       top=True,
                       right=True)
    else:
        ax.set_xticks([]); ax.set_yticks([])

    # ------------------------------------------------------------
    # Labeling & Title
    # ------------------------------------------------------------
    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)

    if title is not None:
        ax.set_title(title, fontsize=fontsize, pad=1.5)

    ax.set_aspect(aspect)

    return ax, mesh

def add_colorbar_cm(
        fig, im,
        pos_cm=(0, 0),
        size_cm=(0.2, 3.5),
        clabel=None,
        fontsize=7,
        ticks_fontsize=6,
        tick_direction="in",
        orientation="vertical"
):
    """Add a manually positioned colorbar (in cm units)."""
    cax = add_axes_cm(fig, pos_cm[0], pos_cm[1], size_cm[0], size_cm[1])

    cbar = fig.colorbar(im, cax=cax, orientation=orientation)
    cbar.ax.tick_params(labelsize=ticks_fontsize, width=0.4, length=1.5,
                        direction=tick_direction)
    if clabel:
        cbar.set_label(clabel, fontsize=fontsize, labelpad=1.2)
    return cbar
