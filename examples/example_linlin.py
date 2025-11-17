import numpy as np
import paperfig as pf

# ------------------------------
# Example data
# ------------------------------
x = np.linspace(0, 10, 300)
curves = [
    {"x": x, "y": np.sin(x), "label": r"$\sin(x)$"},
    {"x": x, "y": np.cos(x), "label": r"$\cos(x)$"},
    {"x": x, "y": np.exp(-0.2 * x), "label": r"$e^{-0.2x}$"}
]

# ------------------------------
# Create figure
# ------------------------------
fig = pf.create_paper_figure(width_cm=8.5,
                             height_cm=6.0,
                             fontsize=7)

pf.add_label_cm(fig,
                "(a)",
                x_cm=0.2,
                y_cm=5.5,
                fig_width_cm=8.5,
                fig_height_cm=6.0)

pf.plotLinLin_panel_core(
    fig,
    curves,
    pos_cm=(1.5, 1.0),
    size_cm=(4.5, 4.5),
    xlabel=r"$x$",
    ylabel=r"$f(x)$",
    grid=True,
    legend=True
)

fig.savefig("example_linlin.png", dpi=600)
print("Saved example_linlin.png")
