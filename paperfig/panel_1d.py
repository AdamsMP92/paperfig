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
        major_tick_length=3.0,
        major_tick_width=0.6,
        minor_tick_length=1.6,
        minor_tick_width=0.35,
):
    """
    Professional log–log panel with APS/PRB-style ticks.
    """

    # === Panel creation ===
    ax = add_axes_cm(fig, pos_cm[0], pos_cm[1], size_cm[0], size_cm[1])
    ax.set_xscale("log")
    ax.set_yscale("log")

    # === Style cycles ===
    if colors is None:
        colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    if linestyles is None:
        linestyles = ["-"] * len(curves)

    # === Plot curves ===
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

    # === Labels & limits ===
    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)
    if title:
        ax.set_title(title, fontsize=fontsize, pad=1.5)

    if xlim: ax.set_xlim(xlim)
    if ylim: ax.set_ylim(ylim)

    # === Grid ===
    if grid:
        ax.grid(which="major", linestyle="-", linewidth=0.3, color="0.85")
        ax.grid(which="minor", linestyle=":", linewidth=0.2, color="0.85")

    # === Professional tick styling ===
    if show_ticks:
        # Major ticks
        ax.tick_params(
            which="major",
            direction="in",
            length=major_tick_length,
            width=major_tick_width,
            labelsize=ticks_fontsize,
            top=True,
            right=True
        )
        # Minor ticks
        ax.tick_params(
            which="minor",
            direction="in",
            length=minor_tick_length,
            width=minor_tick_width,
            top=True,
            right=True
        )
    else:
        ax.set_xticks([]); ax.set_yticks([])

    # === Legend ===
    if legend:
        labels_present = any("label" in c for c in curves)
        if labels_present:
            ax.legend(
                fontsize=ticks_fontsize,
                frameon=False,
                loc="best",
                handlelength=2.2,
                handletextpad=0.4
            )

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
        colors=None
):
    """
    Create a fixed-size linear (x,y) panel for multiple curves.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        Target figure object.
    curves : list of dict
        Each entry: {"x": array, "y": array, "label": str (optional)}.
    pos_cm : tuple (x_cm, y_cm)
        Lower-left corner of panel in centimeters.
    size_cm : tuple (w_cm, h_cm)
        Panel size in centimeters.
    xlabel, ylabel, title : str
        Axis labels and optional title.
    xlim, ylim : tuple
        Axis limits.
    fontsize, ticks_fontsize : float
        Font sizes.
    show_ticks : bool
        Whether to show tick labels.
    grid : bool
        Show grid lines.
    legend : bool
        Display legend if any labels are given.
    linewidth, markersize : float
        Styling parameters.
    linestyles, colors : list
        Optional manual line/marker colors/styles.

    Returns
    -------
    ax : matplotlib.axes.Axes
        Created axis handle.
    """

    # === Create axes in physical units ===
    ax = add_axes_cm(fig, pos_cm[0], pos_cm[1], size_cm[0], size_cm[1])

    # === Color/style cycles ===
    if colors is None:
        colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    if linestyles is None:
        linestyles = ["-"] * len(curves)

    # === Plot curves ===
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

    # === Labels, limits, grid ===
    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)
    if title:
        ax.set_title(title, fontsize=fontsize, pad=1.5)

    if xlim: ax.set_xlim(xlim)
    if ylim: ax.set_ylim(ylim)

    if grid:
        ax.grid(True, linestyle="-", linewidth=0.25, color="0.85")

    # === Ticks ===
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

    # === Legend ===
    if legend:
        labels_present = any("label" in c for c in curves)
        if labels_present:
            ax.legend(
                fontsize=ticks_fontsize,
                frameon=False,
                loc="best",
                handlelength=2.2,
                handletextpad=0.4
            )

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
        edgecolors=None
):
    """
    Create a fixed-size 2D scatter plot panel for multiple datasets.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        Target figure object.
    datasets : list of dict
        Each entry: {"x": array, "y": array, "label": str (optional)}.
    pos_cm : tuple (x_cm, y_cm)
        Lower-left corner of panel in centimeters.
    size_cm : tuple (w_cm, h_cm)
        Panel size in centimeters.
    xlabel, ylabel, title : str
        Axis labels and optional title.
    xlim, ylim : tuple
        Axis limits.
    fontsize, ticks_fontsize : float
        Font sizes.
    show_ticks : bool
        Whether to show tick labels.
    grid : bool
        Show grid lines.
    legend : bool
        Display legend if any labels are given.
    markersize : float
        Marker size.
    alpha : float
        Transparency (0–1).
    markerstyles : list of str
        Optional list of marker symbols (e.g. ['o', 's', '^']).
    colors : list
        Optional list of colors.
    edgecolors : list or str
        Optional edge color(s) for markers.

    Returns
    -------
    ax : matplotlib.axes.Axes
        Created axis handle.
    """

    # === Create axes in physical units ===
    ax = add_axes_cm(fig, pos_cm[0], pos_cm[1], size_cm[0], size_cm[1])

    # === Color/style cycles ===
    if colors is None:
        colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    if markerstyles is None:
        markerstyles = ["o"] * len(datasets)
    if edgecolors is None:
        edgecolors = "none"

    # === Plot datasets ===
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

    # === Labels, limits, grid ===
    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)
    if title:
        ax.set_title(title, fontsize=fontsize, pad=1.5)

    if xlim: ax.set_xlim(xlim)
    if ylim: ax.set_ylim(ylim)

    if grid:
        ax.grid(True, linestyle="--", linewidth=0.4, alpha=0.6)

    # === Ticks ===
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

    # === Legend ===
    if legend:
        labels_present = any("label" in d for d in datasets)
        if labels_present:
            ax.legend(
                fontsize=ticks_fontsize,
                frameon=False,
                loc="best",
                handlelength=1.8,
                handletextpad=0.4
            )

    return ax
