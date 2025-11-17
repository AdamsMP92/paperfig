import numpy as np
import paperfig as pf

# ------------------------------
# Example vector field: vortex
# ------------------------------
N = 15
x = np.linspace(-1, 1, N)
y = np.linspace(-1, 1, N)
z = np.linspace(-1, 1, N)

X, Y, Z = np.meshgrid(x, y, z)


# Vortex field
Hx = -Y
Hy = X
Hz = np.zeros_like(X) + 0.5

H = np.sqrt(Hx**2 + Hy**2 + Hz**2)
Hx = Hx/H
Hy = Hy/H
Hz = Hz/H

C = Hz  # color by y-component

# Flatten to 1D
xv = X.ravel()
yv = Y.ravel()
zv = Z.ravel()
Hxv = Hx.ravel()
Hyv = Hy.ravel()
Hzv = Hz.ravel()
Cv  = C.ravel()

# ------------------------------
# Create figure
# ------------------------------
x_shift = + 0.5
y_shift = - 0.5

fig = pf.create_paper_figure(width_cm=8.5, height_cm=6.0, fontsize=7)

pf.add_label_cm(fig, "(a)", 0.2+x_shift, 5.3+y_shift, 8.5, 6.0)

pf.add_label_cm(fig, r"$x$", 1.2+x_shift, 1.0+y_shift, 8.5, 6.0)
pf.add_label_cm(fig, r"$z$", 0.3+x_shift, 2.75+y_shift, 8.5, 6.0)

# ------------------------------
# 3D Panel
# ------------------------------
ax, img = pf.quiver3_advanced_panel(
    fig,
    xv, yv, zv, Hxv, Hyv, Hzv, Cv,
    Cmin=np.min(Cv), Cmax=np.max(Cv),
    cmap="coolwarm",
    scale=0.075,
    subsample=1,
    view="custom",
    cam_pos=(3, -3, 1),
    focal_point=(0, 0, 0),
    up_direction=(0, 0, 1),
    axes_width_cm=6.5,
    axes_pos_x_cm=0.5+x_shift,
    axes_pos_y_cm=0.5+y_shift,
    dpi=600
)

fig.savefig("example_quiver3d.png", dpi=600)
print("Saved example_quiver3d.png")
