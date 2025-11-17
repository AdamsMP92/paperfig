import numpy as np
from .figure import add_axes_cm
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
        xticks=None,
        yticks=None,
        xticklabels=None,
        yticklabels=None,
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
      - custom xticks / yticks / ticklabels
    """

    ax = add_axes_cm(fig, pos_cm[0], pos_cm[1], size_cm[0], size_cm[1])

    # Normalize axes
    x = np.asarray(x)
    y = np.asarray(y)

    if x.ndim == 1 and y.ndim == 1:
        X, Y = np.meshgrid(x, y)
    elif x.ndim == 2 and y.ndim == 2:
        X, Y = x, y
    else:
        raise ValueError("x and y must be both 1D or both 2D arrays")

    # Plot
    mesh = ax.pcolormesh(
        X, Y, Z,
        cmap=cmap,
        shading=shading,
        vmin=vmin,
        vmax=vmax
    )

    # Axis limits
    if xlim is not None:
        ax.set_xlim(xlim)
    if ylim is not None:
        ax.set_ylim(ylim)

    # Ticks
    if show_ticks:
        ax.tick_params(labelsize=ticks_fontsize,
                       width=0.4,
                       length=1.8,
                       direction="in",
                       top=True,
                       right=True)
    else:
        ax.set_xticks([])
        ax.set_yticks([])

    # Custom ticks
    if xticks is not None:
        ax.set_xticks(xticks)
        if xticklabels is not None:
            ax.set_xticklabels(xticklabels, fontsize=ticks_fontsize)

    if yticks is not None:
        ax.set_yticks(yticks)
        if yticklabels is not None:
            ax.set_yticklabels(yticklabels, fontsize=ticks_fontsize)

    # Labels
    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)

    # Title
    if title is not None:
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
        tick_direction="in",
        orientation="vertical",
        ticks=None
):
    """
    Add a manually positioned colorbar in cm coordinates,
    independent of any image/mappable.

    Parameters
    ----------
    vmin, vmax : float
        Data range for the color scale.
    cmap : str or Colormap
        Colormap for the colorbar.
    ticks : list or None
        Optional explicit tick locations.
    """

    # --- Create axes in cm ---
    cax = add_axes_cm(fig, pos_cm[0], pos_cm[1], size_cm[0], size_cm[1])

    # --- Create artificial mappable (standalone color scale) ---
    norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax)
    sm = mpl.cm.ScalarMappable(norm=norm, cmap=cmap)
    sm.set_array([])  # required by Matplotlib

    # --- Draw colorbar ---
    cbar = fig.colorbar(sm, cax=cax, orientation=orientation)

    # --- Apply ticks if given ---
    if ticks is not None:
        cbar.set_ticks(ticks)

    # --- Tick styling ---
    cbar.ax.tick_params(
        labelsize=ticks_fontsize,
        width=0.4,
        length=1.5,
        direction=tick_direction
    )

    # --- Label ---
    if clabel:
        cbar.set_label(clabel, fontsize=fontsize, labelpad=1.2)

    return cbar

