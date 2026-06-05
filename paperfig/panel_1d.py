import numpy as np
import matplotlib.pyplot as plt
from .figure import add_axes_cm
from .utils import apply_tick_style, apply_label_style, apply_grid_style


def _as_1d_plot_array(values):
    """Return a flat 1D array, accepting either one array or a list of arrays."""
    if isinstance(values, (list, tuple)) and values:
        first = values[0]
        if isinstance(first, (list, tuple, np.ndarray)):
            return np.concatenate([np.ravel(np.asarray(v)) for v in values])
    return np.ravel(np.asarray(values))


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
        options=None,
        markersize=1.0, 
        disable_xticklabels=False,
        disable_yticklabels=False
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
    # Plot curves
    # ---------------------------------------------------------
    for i, data in enumerate(curves):

        # --- Style resolution: curve overrides > defaults ---
        linestyle = data.get("ls", data.get("linestyle", "-"))
        color     = data.get("color", opts.colors[i % len(opts.colors)])
        marker    = data.get("marker", None)

        ax.plot(
            np.asarray(data["x"]),
            np.asarray(data["y"]),
            linestyle=linestyle,
            color=color,
            marker=marker,
            linewidth=data["linewidth"],
            markersize=markersize,
            label=data.get("label", None)
        )

    # ---------------------------------------------------------
    # Labels
    # ---------------------------------------------------------
    apply_label_style(
        ax,
        xlabel,
        ylabel,
        title
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
        major_tick_length=opts.major_tick_length,
        major_tick_width=opts.major_tick_width,
        minor_tick_length=opts.minor_tick_length,
        minor_tick_width=opts.minor_tick_width,
        xticks=xticks,
        yticks=yticks,
        xticklabels=xticklabels,
        yticklabels=yticklabels, 
        disable_xticklabels=disable_xticklabels,
        disable_yticklabels=disable_yticklabels
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
            frameon=False,
            loc="best",
            handlelength=2.2,
            handletextpad=0.4
        )

    return ax





# ============================================================
# 2) SEMILOG–X PANEL
# ============================================================
def plotSemiLogX_panel_core(
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
        options=None,
        markersize=1.0,
        disable_xticklabels=False,
        disable_yticklabels=False
):
    """Unified semilog-x panel using PaperFigOptions."""

    import paperfig as pf
    import numpy as np

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
    ax.set_yscale("linear")

    # ---------------------------------------------------------
    # Plot curves
    # ---------------------------------------------------------
    for i, data in enumerate(curves):

        linestyle = data.get("ls", data.get("linestyle", "-"))
        color     = data.get("color", opts.colors[i % len(opts.colors)])
        marker    = data.get("marker", None)

        ax.plot(
            np.asarray(data["x"]),
            np.asarray(data["y"]),
            linestyle=linestyle,
            color=color,
            marker=marker,
            linewidth=data["linewidth"],
            markersize=markersize,
            label=data.get("label", None)
        )

    # ---------------------------------------------------------
    # Labels
    # ---------------------------------------------------------
    apply_label_style(
        ax,
        xlabel,
        ylabel,
        title
    )

    # ---------------------------------------------------------
    # Limits
    # ---------------------------------------------------------
    if xlim: ax.set_xlim(xlim)
    if ylim: ax.set_ylim(ylim)

    # ---------------------------------------------------------
    # Ticks
    # ---------------------------------------------------------
    apply_tick_style(
        ax,
        show_ticks=True,
        major_tick_length=opts.major_tick_length,
        major_tick_width=opts.major_tick_width,
        minor_tick_length=opts.minor_tick_length,
        minor_tick_width=opts.minor_tick_width,
        xticks=xticks,
        yticks=yticks,
        xticklabels=xticklabels,
        yticklabels=yticklabels,
        disable_xticklabels=disable_xticklabels,
        disable_yticklabels=disable_yticklabels
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

        # --- Style resolution: curve overrides > defaults ---
        linestyle = data.get("ls", data.get("linestyle", "-"))
        color     = data.get("color", data.get("colors", "k"))
        marker    = data.get("marker", None)
        markersize = data.get("markersize", 1.0)
        #print(data["color"])

        ax.plot(
            np.asarray(data["x"]),
            np.asarray(data["y"]),
            linestyle=linestyle,
            color=color,
            marker=marker,
            linewidth=data["linewidth"],
            markersize=markersize,
            label=data.get("label", None)
        )

    # ---------------------------------------------------------
    # Labels
    # ---------------------------------------------------------
    apply_label_style(ax, 
                      xlabel, 
                      ylabel, 
                      title)

    # Limits
    if xlim: ax.set_xlim(xlim)
    if ylim: ax.set_ylim(ylim)

    # ---------------------------------------------------------
    # Ticks
    # ---------------------------------------------------------
    apply_tick_style(
        ax,
        show_ticks=True,
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
        alpha=0.8,
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

         # --- Style resolution: curve overrides > defaults ---
        linestyle = data.get("ls", data.get("linestyle", "-"))
        color     = data.get("color", data.get("colors", "k"))
        marker    = data.get("marker", None)
        markersize = data.get("markersize", 1.0)

        ax.scatter(
            data["x"], data["y"],
            s=markersize,                      # base marker size
            color=color,
            alpha=alpha,
            marker=markerstyles[i % len(markerstyles)],
            edgecolors="none",
            label=data.get("label", None)
        )

    # ---------------------------------------------------------
    # Labels
    # ---------------------------------------------------------
    apply_label_style(ax, xlabel, ylabel, title)

    # Limits
    if xlim: ax.set_xlim(xlim)
    if ylim: ax.set_ylim(ylim)

    # ---------------------------------------------------------
    # Ticks
    # ---------------------------------------------------------
    apply_tick_style(
        ax,
        show_ticks=True,
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
            frameon=False,
            loc="best",
            handlelength=1.8,
            handletextpad=0.4
        )

    ax.set_axisbelow(True)
        
    return ax





# ============================================================
# 4) General 1D PANEL
# ============================================================
def plotGeneral1D_panel_core(
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
        alpha=0.8,
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

    # ---------------------------------------------------------
    # Plot scatter datasets
    # ---------------------------------------------------------
    for i, data in enumerate(datasets):

        linestyle   = data.get("ls", data.get("linestyle", "-"))
        color       = data.get("color", "k")
        marker      = data.get("marker", "o")
        markersize  = data.get("markersize", 3.0)
        plottype    = data.get("plottype", "scatter")
        linewidth   = data.get("linewidth", 1.0)

        x = _as_1d_plot_array(data["x"])
        y = _as_1d_plot_array(data["y"])

        if plottype == "scatter":
            ax.scatter(
                x, y,
                s=markersize**2,     # consistent sizing
                color=color,
                alpha=alpha,
                marker=marker,
                edgecolors=None,
                label=data.get("label", None)
            )

        elif plottype == "line":
            ax.plot(
                x, y,
                linestyle=linestyle,
                color=color,
                marker=marker,
                linewidth=linewidth,
                markersize=markersize,
                label=data.get("label", None)
            )
        elif plottype == "bar":
            ax.bar(
                0.5 * (x[1:] + x[:-1]), y, 
                width=x[1] - x[0],
                color=color,
                alpha=alpha,
                edgecolor='k',
                   )


    # ---------------------------------------------------------
    # Labels
    # ---------------------------------------------------------
    apply_label_style(ax, xlabel, ylabel, title)

    # Limits
    if xlim: ax.set_xlim(xlim)
    if ylim: ax.set_ylim(ylim)

    # ---------------------------------------------------------
    # Ticks
    # ---------------------------------------------------------
    apply_tick_style(
        ax,
        show_ticks=True,
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
            frameon=False,
            loc="best",
            handlelength=1.8,
            handletextpad=0.4
        )

    ax.set_axisbelow(True)
        
    return ax
