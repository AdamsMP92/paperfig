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
        fontsize=7,
        ticks_fontsize=6,
        show_ticks=True,
        grid=True,
        legend=True,
        linewidth=0.8,
        markersize=3.0,
        linestyles=None,
        colors=None,
        xticks=None,
        yticks=None,
        xticklabels=None,
        yticklabels=None,
        major_tick_length=3.0,
        major_tick_width=0.6,
        minor_tick_length=1.6,
        minor_tick_width=0.35,
):
    """Unified log–log panel with consistent tick/grid/label styling."""

    ax = add_axes_cm(fig, pos_cm[0], pos_cm[1], size_cm[0], size_cm[1])
    ax.set_xscale("log")
    ax.set_yscale("log")

    # Cycles
    if colors is None:
        colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    if linestyles is None:
        linestyles = ["-"] * len(curves)

    # Plot curves
    for i, data in enumerate(curves):
        ax.plot(
            np.asarray(data["x"]),
            np.asarray(data["y"]),
            linestyle=linestyles[i % len(linestyles)],
            color=colors[i % len(colors)],
            linewidth=linewidth,
            markersize=markersize,
            label=data.get("label", None)
        )

    # Apply labels
    apply_label_style(ax, xlabel, ylabel, title, fontsize)

    # Apply limits
    if xlim: ax.set_xlim(xlim)
    if ylim: ax.set_ylim(ylim)

    # Unified tick styling
    apply_tick_style(
        ax,
        show_ticks,
        ticks_fontsize,
        major_tick_length,
        major_tick_width,
        minor_tick_length,
        minor_tick_width,
        xticks, yticks,
        xticklabels, yticklabels
    )

    # Unified grid styling
    apply_grid_style(
        ax,
        show=grid,
        major=True,
        minor=True,
        major_linewidth=0.3,
        minor_linewidth=0.2,
        major_color="0.85",
        minor_color="0.85"
    )

    # Legend
    if legend and any("label" in c for c in curves):
        ax.legend(
            fontsize=ticks_fontsize,
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
        fontsize=7,
        ticks_fontsize=6,
        show_ticks=True,
        grid=True,
        legend=True,
        linewidth=0.8,
        markersize=3.0,
        linestyles=None,
        colors=None,
        xticks=None,
        yticks=None,
        xticklabels=None,
        yticklabels=None,
        major_tick_length=2.0,
        major_tick_width=0.45,
        minor_tick_length=1.2,
        minor_tick_width=0.35,
):
    """Unified linear panel with consistent tick/grid/label styling."""

    ax = add_axes_cm(fig, pos_cm[0], pos_cm[1], size_cm[0], size_cm[1])

    if colors is None:
        colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    if linestyles is None:
        linestyles = ["-"] * len(curves)

    # Plot curves
    for i, data in enumerate(curves):
        ax.plot(
            data["x"], data["y"],
            linestyle=linestyles[i % len(linestyles)],
            color=colors[i % len(colors)],
            linewidth=linewidth,
            markersize=markersize,
            label=data.get("label", None)
        )

    # Apply labels
    apply_label_style(ax, xlabel, ylabel, title, fontsize)

    # Apply limits
    if xlim: ax.set_xlim(xlim)
    if ylim: ax.set_ylim(ylim)

    # Apply ticks
    apply_tick_style(
        ax,
        show_ticks,
        ticks_fontsize,
        major_tick_length,
        major_tick_width,
        minor_tick_length,
        minor_tick_width,
        xticks, yticks,
        xticklabels, yticklabels
    )

    # Apply grid
    apply_grid_style(
        ax,
        show=grid,
        major=True,
        minor=False,
        major_linewidth=0.25,
        major_color="0.85"
    )

    # Legend
    if legend and any("label" in c for c in curves):
        ax.legend(
            fontsize=ticks_fontsize,
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
        fontsize=7,
        ticks_fontsize=6,
        show_ticks=True,
        grid=True,
        legend=True,
        markersize=10,
        alpha=0.8,
        markerstyles=None,
        colors=None,
        edgecolors=None,
        xticks=None,
        yticks=None,
        xticklabels=None,
        yticklabels=None,
        major_tick_length=2.0,
        major_tick_width=0.45,
        minor_tick_length=1.2,
        minor_tick_width=0.35,
):
    """Unified scatter panel with consistent tick/grid/label styling."""

    ax = add_axes_cm(fig, pos_cm[0], pos_cm[1], size_cm[0], size_cm[1])

    if colors is None:
        colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    if markerstyles is None:
        markerstyles = ["o"] * len(datasets)
    if edgecolors is None:
        edgecolors = "none"

    # Plot scatter datasets
    for i, data in enumerate(datasets):
        ax.scatter(
            data["x"], data["y"],
            s=markersize,
            color=colors[i % len(colors)],
            alpha=alpha,
            marker=markerstyles[i % len(markerstyles)],
            edgecolors=edgecolors,
            label=data.get("label", None)
        )

    # Apply labels
    apply_label_style(ax, xlabel, ylabel, title, fontsize)

    # Apply limits
    if xlim: ax.set_xlim(xlim)
    if ylim: ax.set_ylim(ylim)

    # Apply ticks
    apply_tick_style(
        ax,
        show_ticks,
        ticks_fontsize,
        major_tick_length,
        major_tick_width,
        minor_tick_length,
        minor_tick_width,
        xticks, yticks,
        xticklabels, yticklabels
    )

    # Apply grid
    apply_grid_style(
        ax,
        show=grid,
        major=True,
        minor=False,
        major_linewidth=0.4,
        major_color="0.8",
        alpha=0.6
    )

    # Legend
    if legend and any("label" in d for d in datasets):
        ax.legend(
            fontsize=ticks_fontsize,
            frameon=False,
            loc="best",
            handlelength=1.8,
            handletextpad=0.4
        )

    return ax


