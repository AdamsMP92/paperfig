from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import paperfig as pf


OUTPUT = Path(__file__).with_suffix(".png")

x = np.linspace(-2, 2, 200)
y = np.linspace(-2, 2, 150)
X, Y = np.meshgrid(x, y)
Z = np.exp(-(X**2 + 2 * Y**2))

fig = pf.create_paper_figure(width_cm=13.5, height_cm=8.0)

pf.add_label_cm(fig, "(a)", x_cm=0.35, y_cm=7.3, weight="bold")

ax, im = pf.plot2D_panel_core(
    fig,
    x,
    y,
    Z,
    pos_cm=(2.0, 1.25),
    size_cm=(5.7, 5.7),
    cmap="magma",
    xlabel=r"$x$",
    ylabel=r"$y$",
    title=r"$2\mathrm{D}\ \mathrm{Gaussian}$",
    vmin=0,
    vmax=1,
)

pf.add_colorbar_cm(
    fig,
    pos_cm=(8.2, 1.25),
    size_cm=(0.22, 5.7),
    vmin=0,
    vmax=1,
    cmap="magma",
    clabel=r"$I$",
    ticks=[0, 0.5, 1.0],
)

fig.savefig(OUTPUT, dpi=600)
print(f"Saved {OUTPUT}")
