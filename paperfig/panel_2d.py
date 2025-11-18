import numpy as np
import matplotlib as mpl
from .figure import add_axes_cm
from .utils import apply_tick_style, apply_label_style, apply_grid_style


# ============================================================
# 1) 2D IM SHOW PANEL
# ============================================================
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
        grid=False,
        major_tick_length=2.0,
        major_tick_width=0.45,
        minor_tick_length=1.2,
        minor_tick_width=0.35
):
    """2D imshow panel with unified label/grid/tick styling."""
    
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

    # Apply ticks
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

    # Apply labels
    apply_label_style(ax, xlabel, ylabel, title, fontsize)

    # Apply grid (optional)
    apply_grid_style(
        ax,
        show=grid,
        major=True,
        minor=False,
        major_linewidth=0.25,
        major_color="0.8"
    )

    return ax, im



# ============================================================
# 2) 2D PCOLORMESH PANEL
# ============================================================
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
        grid=False,
        shading="auto",
        major_tick_length=2.0,
        major_tick_width=0.45,
        minor_tick_length=1.2,
        minor_tick_width=0.35
):
    """2D pcolormesh panel with unified label/grid/tick styling."""

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

    # Axis limits
    if xlim is not None:
        ax.set_xlim(xlim)
    if ylim is not None:
        ax.set_ylim(ylim)

    # Unified tick system
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

    # Unified labels
    apply_label_style(ax, xlabel, ylabel, title, fontsize)

    # Optional grid
    apply_grid_style(
        ax,
        show=grid,
        major=True,
        minor=False,
        major_linewidth=0.25,
        major_color="0.8"
    )

    ax.set_aspect(aspect)
    return ax, mesh



# ============================================================
# 3) COLORBAR (CM-PLACED)
# ============================================================
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
    """Colorbar with unified tick + label styling."""

    cax = add_axes_cm(fig, pos_cm[0], pos_cm[1], size_cm[0], size_cm[1])

    norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax)
    sm = mpl.cm.ScalarMappable(norm=norm, cmap=cmap)
    sm.set_array([])

    cbar = fig.colorbar(sm, cax=cax, orientation=orientation)

    if ticks is not None:
        cbar.set_ticks(ticks)

    # Tick styling
    cbar.ax.tick_params(
        which="major",
        labelsize=ticks_fontsize,
        direction=tick_direction,
        length=major_tick_length,
        width=major_tick_width
    )

    # Label styling
    if clabel:
        cbar.set_label(clabel, fontsize=fontsize, labelpad=1.5)

    return cbar
