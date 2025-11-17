import numpy as np
import paperfig as pf

# ------------------------------
# Example data: 2D Gaussian
# ------------------------------
x = np.linspace(-2, 2, 200)
y = np.linspace(-2, 2, 150)
X, Y = np.meshgrid(x, y)
Z = np.exp(-(X**2 + 2*Y**2))

# ------------------------------
# Create figure
# ------------------------------
fig = pf.create_paper_figure(width_cm=8.5, height_cm=6.0, fontsize=7)

# Panel label
pf.add_label_cm(fig,
                "(a)",
                x_cm=0.2,
                y_cm=5.5,
                fig_width_cm=8.5,
                fig_height_cm=6.0)

# ------------------------------
# Panel
# ------------------------------
ax, im = pf.plot2D_panel_core(
    fig, x, y, Z,
    pos_cm=(1.5, 1.0),
    size_cm=(4.5, 4.5),
    cmap="cool",
    xlabel=r"$x$",
    ylabel=r"$y$",
    title="2D Gaussian",
    aspect="equal"
)

# ------------------------------
# Colorbar
# ------------------------------
pf.add_colorbar_cm(
    fig,
    im,
    pos_cm=(6.2, 1.0),
    size_cm=(0.15, 4.5),
    clabel="Intensity"
)

fig.savefig("example_2dmap.png", dpi=600)
print("Saved example_2dmap.png")
