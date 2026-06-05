from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import paperfig as pf


OUTPUT = Path(__file__).with_suffix(".png")

x = np.linspace(0, 10, 300)
curves = [
    {"x": x, "y": np.sin(x), "linewidth": 0.8, "label": r"$\sin(x)$"},
    {"x": x, "y": np.cos(x), "linewidth": 0.8, "label": r"$\cos(x)$"},
    {"x": x, "y": np.exp(-0.2 * x), "linewidth": 0.8, "label": r"$e^{-0.2x}$"},
]

fig = pf.create_paper_figure(width_cm=13.5, height_cm=8.0)

pf.add_label_cm(fig, "(a)", x_cm=0.35, y_cm=7.3, weight="bold")
pf.add_color_box_cm(fig, x_cm=10.2, y_cm=5.9, w_cm=2.0, h_cm=0.75, color="0.93")
pf.add_label_cm(fig, r"$\mathrm{demo}$", x_cm=11.2, y_cm=6.27, centered=True)

pf.plotLinLin_panel_core(
    fig,
    curves,
    pos_cm=(2.0, 1.35),
    size_cm=(6.8, 5.4),
    xlabel=r"$x$",
    ylabel=r"$f(x)$",
)

fig.savefig(OUTPUT, dpi=600)
print(f"Saved {OUTPUT}")
