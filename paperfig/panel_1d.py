import numpy as np
import matplotlib.pyplot as plt
from .figure import add_axes_cm


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
        major_tick_length=3.0,
        major_tick_width=0.6,
        minor_tick_length=1.6,
        minor_tick_width=0.35,
):
    """
    Unified log–log panel with consistent tick styling.
    """

    ax = add_axes_cm(fig, pos_cm[0], pos_cm[1], size_cm[0], size_cm[1])
    ax.set_xscale("log")
    ax.set_yscale("log")

    if colors is None:
        colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    if linestyles is None:
        linestyles = ["-"] * len(curves)

    # Plot curves
    for i, data in enumerate(curves):
        x = np.asarray(data["x"])
        y = np.asarray(data["y"])
        label = data.get("label", None)
        ax.plot(
            x, y,
            linestyle=linestyles[i % len(linestyles)],
            color=colors[i % len(colors)],
            linewidth=linewidth,
            markersize=markersize,
            label=label
        )

    # Labels + limits
    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)
    if title:
        ax.set_title(title, fontsize=fontsize, pad=1.5)
    if xlim: ax.set_xlim(xlim)
    if ylim: ax.set_ylim(ylim)

    # Custom ticks
    if xticks is not None: ax.set_xticks(xticks)
    if yticks is not None: ax.set_yticks(yticks)

    # Grid
    if grid:
        ax.grid(which="major", linestyle="-", linewidth=0.3, color="0.85")
        ax.grid(which="minor", linestyle=":", linewidth=0.2, color="0.85")

    # Tick styling (unified)
    if show_ticks:
        ax.tick_params(which="major",
                       direction="in",
                       labelsize=ticks_fontsize,
                       length=major_tick_length,
                       width=major_tick_width,
                       top=True, right=True)

        ax.tick_params(which="minor",
                       direction="in",
                       length=minor_tick_length,
                       width=minor_tick_width,
                       top=True, right=True)

    else:
        ax.set_xticks([]); ax.set_yticks([])

    # Legend
    if legend and any("label" in c for c in curves):
        ax.legend(fontsize=ticks_fontsize, frameon=False,
                  loc="best", handlelength=2.2, handletextpad=0.4)

    return ax



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
        major_tick_length=2.0,
        major_tick_width=0.45,
        minor_tick_length=1.2,
        minor_tick_width=0.35,
):
    """
    Unified linear panel with consistent tick styling.
    """

    ax = add_axes_cm(fig, pos_cm[0], pos_cm[1], size_cm[0], size_cm[1])

    if colors is None:
        colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    if linestyles is None:
        linestyles = ["-"] * len(curves)

    # Plot curves
    for i, data in enumerate(curves):
        x = np.asarray(data["x"])
        y = np.asarray(data["y"])
        label = data.get("label", None)

        ax.plot(
            x, y,
            linestyle=linestyles[i % len(linestyles)],
            color=colors[i % len(colors)],
            linewidth=linewidth,
            markersize=markersize,
            label=label
        )

    # Labels & limits
    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)
    if title:
        ax.set_title(title, fontsize=fontsize, pad=1.5)

    if xlim: ax.set_xlim(xlim)
    if ylim: ax.set_ylim(ylim)

    # Custom ticks
    if xticks is not None: ax.set_xticks(xticks)
    if yticks is not None: ax.set_yticks(yticks)

    # Grid
    if grid:
        ax.grid(True, linestyle="-", linewidth=0.25, color="0.85")

    # Tick styling (unified)
    if show_ticks:
        ax.tick_params(which="major",
                       direction="in",
                       labelsize=ticks_fontsize,
                       length=major_tick_length,
                       width=major_tick_width,
                       top=True, right=True)

        ax.tick_params(which="minor",
                       direction="in",
                       length=minor_tick_length,
                       width=minor_tick_width,
                       top=True, right=True)

        ax.minorticks_on()
    else:
        ax.set_xticks([]); ax.set_yticks([])

    # Legend
    if legend and any("label" in c for c in curves):
        ax.legend(fontsize=ticks_fontsize, frameon=False,
                  loc="best", handlelength=2.2, handletextpad=0.4)

    return ax



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
        major_tick_length=2.0,
        major_tick_width=0.45,
        minor_tick_length=1.2,
        minor_tick_width=0.35,
):
    """
    Unified scatter panel with consistent tick styling.
    """

    ax = add_axes_cm(fig, pos_cm[0], pos_cm[1], size_cm[0], size_cm[1])

    if colors is None:
        colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    if markerstyles is None:
        markerstyles = ["o"] * len(datasets)
    if edgecolors is None:
        edgecolors = "none"

    # Plot datasets
    for i, data in enumerate(datasets):
        x = np.asarray(data["x"])
        y = np.asarray(data["y"])
        label = data.get("label", None)

        ax.scatter(
            x, y,
            s=markersize,
            color=colors[i % len(colors)],
            alpha=alpha,
            marker=markerstyles[i % len(markerstyles)],
            edgecolors=edgecolors,
            label=label
        )

    # Labels
    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)
    if title:
        ax.set_title(title, fontsize=fontsize, pad=1.5)

    if xlim: ax.set_xlim(xlim)
    if ylim: ax.set_ylim(ylim)

    # Custom ticks
    if xticks is not None: ax.set_xticks(xticks)
    if yticks is not None: ax.set_yticks(yticks)

    # Grid
    if grid:
        ax.grid(True, linestyle="-", linewidth=0.4, alpha=0.6)

    # Tick styling
    if show_ticks:
        ax.tick_params(which="major",
                       direction="in",
                       labelsize=ticks_fontsize,
                       length=major_tick_length,
                       width=major_tick_width,
                       top=True, right=True)

        ax.tick_params(which="minor",
                       direction="in",
                       length=minor_tick_length,
                       width=minor_tick_width,
                       top=True, right=True)

        ax.minorticks_on()
    else:
        ax.set_xticks([]); ax.set_yticks([])

    # Legend
    if legend and any("label" in d for d in datasets):
        ax.legend(fontsize=ticks_fontsize, frameon=False,
                  loc="best", handlelength=1.8, handletextpad=0.4)

    return ax

