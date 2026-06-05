from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import paperfig as pf


OUTPUT = Path(__file__).with_suffix(".png")

N = 11
x = np.linspace(-1, 1, N)
y = np.linspace(-1, 1, N)
z = np.linspace(-1, 1, N)
X, Y, Z = np.meshgrid(x, y, z)

Hx = -Y
Hy = X
Hz = np.full_like(X, 0.5)

H = np.sqrt(Hx**2 + Hy**2 + Hz**2)
Hx = Hx / H
Hy = Hy / H
Hz = Hz / H
C = Hz

xv = X.ravel()
yv = Y.ravel()
zv = Z.ravel()
Hxv = Hx.ravel()
Hyv = Hy.ravel()
Hzv = Hz.ravel()
Cv = C.ravel()

fig = pf.create_paper_figure(width_cm=6.5, height_cm=6.15)

pf.add_label_cm(fig, "(a)", x_cm=0.2, y_cm=5.7, fontsize=14)
pf.add_label_cm(fig, r"$x$", x_cm=1.15, y_cm=0.5, fontsize=12)
pf.add_label_cm(fig, r"$z$", x_cm=0.3, y_cm=2.2, fontsize=12)

ax, img = pf.quiver3_advanced_panel_fast(
    fig,
    xv,
    yv,
    zv,
    Hxv,
    Hyv,
    Hzv,
    Cv,
    Cmin=np.min(Cv),
    Cmax=np.max(Cv),
    cmap="coolwarm",
    head_length=0.35,
    stick_radius=0.07,
    head_radius=0.15,
    arrow_scale=0.18,
    subsample=1,
    view="custom",
    cam_pos=(3, -3, 1.3),
    focal_point=(0, 0, 0),
    up_direction=(0, 0, 1),
    axes_width_cm=6.9,
    axes_pos_x_cm=0.35,
    axes_pos_y_cm=-0.15,
    dpi=300,
)

fig.savefig(OUTPUT, dpi=600)
print(f"Saved {OUTPUT}")
