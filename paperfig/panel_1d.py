import numpy as np
import matplotlib.pyplot as plt
from .figure import add_axes_cm
from .utils import apply_tick_style, apply_label_style, apply_grid_style


# ============================================================
# 1) LOG–LOG PANEL
# ============================================================
def plotLogLog_panel_core(
        fig,
        curves,
        pos_cm=(0, 0),
        size_cm=(3.5, 3.5),
        xlabel="x",
        ylabel="y",
        title=None,
        xlim=None,
        ylim=None,
        xticks=None,
        yticks=None,
        xticklabels=None,
        yticklabels=None,
        options=None
):
    """Unified log–log panel using PaperFigOptions."""

    import paperfig as pf

    # ---------------------------------------------------------
    # Use global or local options
    # ---------------------------------------------------------
    if options is None:
        options = pf.global_options
    opts = options

    # ---------------------------------------------------------
    # Axes creation
    # ---------------------------------------------------------
    ax = add_axes_cm(fig, pos_cm[0], pos_cm[1], size_cm[0], size_cm[1])
    ax.set_xscale("log")
    ax.set_yscale("log")

    # ---------------------------------------------------------
    # Color / linestyle cycles
    # ---------------------------------------------------------
    colors = opts.colors
    linestyles = ["-"] * len(curves)

    # ---------------------------------------------------------
    # Plot curves
    # ---------------------------------------------------------
    for i, data in enumerate(curves):
        ax.plot(
            np.asarray(data["x"]),
            np.asarray(data["y"]),
            linestyle=linestyles[i % len(linestyles)],
            color=colors[i % len(colors)],
            linewidth=opts.linewidth,
            markersize=3.0,
            label=data.get("label", None)
        )

    # ---------------------------------------------------------
    # Labels
    # ---------------------------------------------------------
    apply_label_style(
        ax,
        xlabel,
        ylabel,
        title,
        opts.fontsize
    )

    # Limits
    if xlim: ax.set_xlim(xlim)
    if ylim: ax.set_ylim(ylim)

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
    # Grid styling
    # ---------------------------------------------------------
    apply_grid_style(
        ax,
        show=True,
        major=True,
        minor=True,
        major_linewidth=0.3,
        minor_linewidth=0.2,
        major_color=opts.grid_color,
        minor_color=opts.grid_color
    )

    # ---------------------------------------------------------
    # Spines
    # ---------------------------------------------------------
    for spine in ax.spines.values():
        spine.set_linewidth(opts.spine_width)
        spine.set_color(opts.spine_color)

    # ---------------------------------------------------------
    # Legend
    # ---------------------------------------------------------
    if any("label" in c for c in curves):
        ax.legend(
            fontsize=opts.ticks_fontsize,
            frameon=False,
            loc="best",
            handlelength=2.2,
            handletextpad=0.4
        )

    return ax


# ============================================================
# 2) LIN–LIN PANEL
# ============================================================
def plotLinLin_panel_core(
        fig,
        curves,
        pos_cm=(0, 0),
        size_cm=(3.5, 3.5),
        xlabel="x",
        ylabel="y",
        title=None,
        xlim=None,
        ylim=None,
        xticks=None,
        yticks=None,
        xticklabels=None,
        yticklabels=None,
        options=None
):
    """Unified linear panel using PaperFigOptions."""

    import paperfig as pf

    # ---------------------------------------------------------
    # Resolve options
    # ---------------------------------------------------------
    if options is None:
        options = pf.global_options
    opts = options

    # ---------------------------------------------------------
    # Create axes
    # ---------------------------------------------------------
    ax = add_axes_cm(fig, pos_cm[0], pos_cm[1], size_cm[0], size_cm[1])

    # ---------------------------------------------------------
    # Cycles
    # ---------------------------------------------------------
    colors = opts.colors
    linestyles = ["-"] * len(curves)

    # ---------------------------------------------------------
    # Plot curves
    # ---------------------------------------------------------
    for i, data in enumerate(curves):
        ax.plot(
            data["x"], data["y"],
            linestyle=linestyles[i % len(linestyles)],
            color=colors[i % len(colors)],
            linewidth=opts.linewidth,
            markersize=3.0,
            label=data.get("label", None)
        )

    # ---------------------------------------------------------
    # Labels
    # ---------------------------------------------------------
    apply_label_style(ax, xlabel, ylabel, title, opts.fontsize)

    # Limits
    if xlim: ax.set_xlim(xlim)
    if ylim: ax.set_ylim(ylim)

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
    # Grid
    # ---------------------------------------------------------
    apply_grid_style(
        ax,
        show=True,
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

    # ---------------------------------------------------------
    # Legend
    # ---------------------------------------------------------
    if any("label" in c for c in curves):
        ax.legend(
            fontsize=opts.ticks_fontsize,
            frameon=False,
            loc="best",
            handlelength=2.2,
            handletextpad=0.4
        )

    return ax


# ============================================================
# 3) SCATTER 2D PANEL
# ============================================================
def plotScatter2D_panel_core(
        fig,
        datasets,
        pos_cm=(0, 0),
        size_cm=(3.5, 3.5),
        xlabel="x",
        ylabel="y",
        title=None,
        xlim=None,
        ylim=None,
        xticks=None,
        yticks=None,
        xticklabels=None,
        yticklabels=None,
        options=None
):
    """Unified scatter panel using PaperFigOptions."""

    import paperfig as pf

    # ---------------------------------------------------------
    # Resolve options
    # ---------------------------------------------------------
    if options is None:
        options = pf.global_options
    opts = options

    # ---------------------------------------------------------
    # Create axes
    # ---------------------------------------------------------
    ax = add_axes_cm(fig, pos_cm[0], pos_cm[1], size_cm[0], size_cm[1])

    # ---------------------------------------------------------
    # Cycles
    # ---------------------------------------------------------
    colors = opts.colors
    markerstyles = ["o"] * len(datasets)

    # ---------------------------------------------------------
    # Plot scatter datasets
    # ---------------------------------------------------------
    for i, data in enumerate(datasets):
        ax.scatter(
            data["x"], data["y"],
            s=10,                      # base marker size
            color=colors[i % len(colors)],
            alpha=0.8,
            marker=markerstyles[i % len(markerstyles)],
            edgecolors="none",
            label=data.get("label", None)
        )

    # ---------------------------------------------------------
    # Labels
    # ---------------------------------------------------------
    apply_label_style(ax, xlabel, ylabel, title, opts.fontsize)

    # Limits
    if xlim: ax.set_xlim(xlim)
    if ylim: ax.set_ylim(ylim)

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
    # Grid
    # ---------------------------------------------------------
    apply_grid_style(
        ax,
        show=True,
        major=True,
        minor=False,
        major_linewidth=0.4,
        major_color=opts.grid_color,
        alpha=0.6
    )

    # ---------------------------------------------------------
    # Spines
    # ---------------------------------------------------------
    for spine in ax.spines.values():
        spine.set_linewidth(opts.spine_width)
        spine.set_color(opts.spine_color)

    # ---------------------------------------------------------
    # Legend
    # ---------------------------------------------------------
    if any("label" in d for d in datasets):
        ax.legend(
            fontsize=opts.ticks_fontsize,
            frameon=False,
            loc="best",
            handlelength=1.8,
            handletextpad=0.4
        )

    return ax



