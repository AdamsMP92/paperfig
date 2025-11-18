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
        aspect="equal",
        grid=False,
        options=None
):
    """2D imshow panel with unified PaperFigOptions styling."""

    import paperfig as pf

    # ---------------------------------------------------------
    # Resolve options
    # ---------------------------------------------------------
    if options is None:
        options = pf.global_options
    opts = options

    # ---------------------------------------------------------
    # Create axis
    # ---------------------------------------------------------
    ax = add_axes_cm(fig, pos_cm[0], pos_cm[1], size_cm[0], size_cm[1])

    # Plot
    im = ax.imshow(
        Z,
        extent=[x.min(), x.max(), y.min(), y.max()],
        cmap=cmap,
        origin="lower",
        vmin=vmin,
        vmax=vmax,
        aspect=aspect
    )

    # ---------------------------------------------------------
    # Limits
    # ---------------------------------------------------------
    if xlim is not None: ax.set_xlim(xlim)
    if ylim is not None: ax.set_ylim(ylim)

    # ---------------------------------------------------------
    # Ticks
    # ---------------------------------------------------------
    apply_tick_style(
        ax,
        show_ticks=True,
        ticks_fontsize=opts.ticks_fontsize,
        major_tick_length=opts.major_tick_length,
        major_tick_width=opts.major_tick_width,
        minor_tick_length=opts.minor_tick_length,
        minor_tick_width=opts.minor_tick_width,
        xticks=xticks,
        yticks=yticks,
        xticklabels=xticklabels,
        yticklabels=yticklabels
    )

    # ---------------------------------------------------------
    # Labels
    # ---------------------------------------------------------
    apply_label_style(ax, xlabel, ylabel, title, opts.fontsize)

    # ---------------------------------------------------------
    # Grid
    # ---------------------------------------------------------
    apply_grid_style(
        ax,
        show=grid,
        major=True,
        minor=False,
        major_linewidth=0.25,
        major_color=opts.grid_color
    )

    # ---------------------------------------------------------
    # Spines
    # ---------------------------------------------------------
    for spine in ax.spines.values():
        spine.set_linewidth(opts.spine_width)
        spine.set_color(opts.spine_color)

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
        aspect="equal",
        grid=False,
        shading="auto",
        options=None
):
    """2D pcolormesh panel with unified PaperFigOptions styling."""

    import paperfig as pf

    # ---------------------------------------------------------
    # Resolve options
    # ---------------------------------------------------------
    if options is None:
        options = pf.global_options
    opts = options

    # ---------------------------------------------------------
    # Create axis
    # ---------------------------------------------------------
    ax = add_axes_cm(fig, pos_cm[0], pos_cm[1], size_cm[0], size_cm[1])

    # Prepare meshgrid
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

    # ---------------------------------------------------------
    # Limits
    # ---------------------------------------------------------
    if xlim is not None: ax.set_xlim(xlim)
    if ylim is not None: ax.set_ylim(ylim)

    # ---------------------------------------------------------
    # Ticks
    # ---------------------------------------------------------
    apply_tick_style(
        ax,
        show_ticks=True,
        ticks_fontsize=opts.ticks_fontsize,
        major_tick_length=opts.major_tick_length,
        major_tick_width=opts.major_tick_width,
        minor_tick_length=opts.minor_tick_length,
        minor_tick_width=opts.minor_tick_width,
        xticks=xticks,
        yticks=yticks,
        xticklabels=xticklabels,
        yticklabels=yticklabels
    )

    # ---------------------------------------------------------
    # Labels
    # ---------------------------------------------------------
    apply_label_style(ax, xlabel, ylabel, title, opts.fontsize)

    # ---------------------------------------------------------
    # Grid
    # ---------------------------------------------------------
    apply_grid_style(
        ax,
        show=grid,
        major=True,
        minor=False,
        major_linewidth=0.25,
        major_color=opts.grid_color
    )

    # ---------------------------------------------------------
    # Spines
    # ---------------------------------------------------------
    for spine in ax.spines.values():
        spine.set_linewidth(opts.spine_width)
        spine.set_color(opts.spine_color)

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
        ticks=None,
        orientation="vertical",
        options=None
):
    """Colorbar with unified PaperFigOptions styling."""

    import paperfig as pf

    # ---------------------------------------------------------
    # Resolve options
    # ---------------------------------------------------------
    if options is None:
        options = pf.global_options
    opts = options

    # ---------------------------------------------------------
    # Axis
    # ---------------------------------------------------------
    cax = add_axes_cm(fig, pos_cm[0], pos_cm[1], size_cm[0], size_cm[1])

    # Colorbar mappable
    norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax)
    sm = mpl.cm.ScalarMappable(norm=norm, cmap=cmap)
    sm.set_array([])

    cbar = fig.colorbar(sm, cax=cax, orientation=orientation)

    if ticks is not None:
        cbar.set_ticks(ticks)

    # ---------------------------------------------------------
    # Tick styling
    # ---------------------------------------------------------
    cbar.ax.tick_params(
        which="major",
        labelsize=opts.ticks_fontsize,
        direction=opts.tick_direction,
        length=opts.major_tick_length,
        width=opts.major_tick_width
    )

    # ---------------------------------------------------------
    # Label styling
    # ---------------------------------------------------------
    if clabel:
        cbar.set_label(clabel, fontsize=opts.fontsize, labelpad=1.5)

    # ---------------------------------------------------------
    # Spines
    # ---------------------------------------------------------
    for spine in cbar.ax.spines.values():
        spine.set_linewidth(opts.spine_width)
        spine.set_color(opts.spine_color)

    return cbar
