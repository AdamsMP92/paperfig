# paperfig

`paperfig` is a small Python toolkit for publication-style Matplotlib figures with
centimeter-accurate layout, shared styling options, 1D/2D panel helpers, and
PyVista-backed 3D vector-field rendering.

## Install

```bash
pip install -e .
```

## Quick Start

```python
import numpy as np
import paperfig as pf

x = np.linspace(0, 10, 300)
curves = [
    {"x": x, "y": np.sin(x), "linewidth": 0.8, "label": r"$\sin(x)$"},
    {"x": x, "y": np.cos(x), "linewidth": 0.8, "label": r"$\cos(x)$"},
]

fig = pf.create_paper_figure(width_cm=8.5, height_cm=6.0)
pf.add_label_cm(fig, "(a)", x_cm=0.35, y_cm=5.55, weight="bold")

pf.plotLinLin_panel_core(
    fig,
    curves,
    pos_cm=(1.25, 0.85),
    size_cm=(5.0, 4.5),
    xlabel=r"$x$",
    ylabel=r"$f(x)$",
)

fig.savefig("figure.png", dpi=600)
```

## Examples

Run the scripts from the repository root:

```bash
python examples/example_linlin.py
python examples/example_2dmap.py
python examples/example_article_style.py
python examples/example_quiver3d.py
```

The examples cover line plots, 2D maps with cm-placed colorbars, article-style
scatter/fit panels, cm-based labels and annotation boxes, and fast PyVista glyph
rendering for 3D vector fields.

## Core Helpers

- `create_paper_figure(...)`: create a figure using cm dimensions and paper-style rcParams.
- `add_axes_cm(...)`: place Matplotlib axes in cm coordinates.
- `add_label_cm(...)`: place labels in cm coordinates, including centered labels.
- `add_line_cm(...)`: add figure-level lines in cm coordinates.
- `add_color_box_cm(...)`: add figure-level colored rectangles in cm coordinates.
- `add_folder_box_cm(...)`: add simple folder-shaped annotation boxes.

## Notes

LaTeX text rendering is enabled by default. `paperfig` does not change the global
font size in `create_paper_figure`; use explicit text kwargs only for intentional
annotations such as panel labels.
