from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import paperfig as pf


OUTPUT = Path(__file__).with_suffix(".png")

rng = np.random.default_rng(2)
rho = [np.sort(rng.uniform(0.02, 0.98, 180)) for _ in range(4)]

m_phi = [np.tanh(4.4 * r) + rng.normal(0.0, 0.045, r.size) for r in rho]
m_z = [1.0 / np.cosh(4.4 * r) + rng.normal(0.0, 0.045, r.size) for r in rho]
m_rho = [rng.normal(0.0, 0.045, r.size) for r in rho]

rho_lin = np.linspace(0, 1, 500)
datasets = [
    {
        "x": rho,
        "y": m_rho,
        "plottype": "scatter",
        "label": r"$m_{\rho}$",
        "color": "#1f77b4",
        "markersize": 3,
        "marker": "o",
    },
    {
        "x": rho,
        "y": m_phi,
        "plottype": "scatter",
        "label": r"$m_{\phi}$",
        "color": "#ff7f0e",
        "markersize": 3,
        "marker": "o",
    },
    {
        "x": rho,
        "y": m_z,
        "plottype": "scatter",
        "label": r"$m_z$",
        "color": "#2ca02c",
        "markersize": 3,
        "marker": "o",
    },
    {
        "x": rho_lin,
        "y": np.tanh(4.4 * rho_lin),
        "plottype": "line",
        "label": r"$\mathrm{tanh}(\nu\rho/R)$",
        "linewidth": 1.0,
        "color": "k",
        "marker": None,
    },
    {
        "x": rho_lin,
        "y": 1.0 / np.cosh(4.4 * rho_lin),
        "plottype": "line",
        "label": r"$\mathrm{sech}(\nu\rho/R)$",
        "linewidth": 1.0,
        "color": "k",
        "marker": None,
        "linestyle": "--",
    },
]

fig = pf.create_paper_figure(width_cm=13.5, height_cm=6.15)
pf.add_label_cm(fig, "(a)", x_cm=0.2, y_cm=5.7, fontsize=14)

ax = pf.plotGeneral1D_panel_core(
    fig,
    datasets,
    pos_cm=(1.3, 0.95),
    size_cm=(5.1, 4.8),
    xlabel=r"$\rho/R$",
    ylabel=r"$m$",
    xlim=[-0.05, 1.05],
    ylim=[-1.1, 1.1],
    xticks=[0.0, 0.25, 0.5, 0.75, 1.0],
    yticks=[-1.0, -0.5, 0.0, 0.5, 1.0],
    alpha=0.8,
)

handles, labels = ax.get_legend_handles_labels()
order = [0, 1, 2, 3, 4]
ax.legend(
    [handles[i] for i in order],
    [labels[i] for i in order],
    ncol=2,
    frameon=True,
    edgecolor="none",
    loc="center left",
    bbox_to_anchor=(0.0, 0.17),
    handlelength=1.2,
    handletextpad=0.4,
    columnspacing=1.2,
)

fig.savefig(OUTPUT, dpi=600)
print(f"Saved {OUTPUT}")
