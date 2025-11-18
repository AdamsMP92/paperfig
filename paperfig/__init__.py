# paperfig/__init__.py

"""
paperfig: A publication-quality Python figure toolkit with cm-accurate layout,
LaTeX typography, high-end 1D/2D panels, and PyVista-powered 3D rendering.
"""

# --- Figure creation & layout helpers ---
from .figure import (
    create_paper_figure,
    add_axes_cm,
    add_label_cm
)

# --- Utility helpers ---
from .utils import (
    crop_image,
    Show_Axes_Margins,
    add_reference_axes,
    apply_tick_style
)

# --- 1D panel tools ---
from .panel_1d import (
    plotLinLin_panel_core,
    plotLogLog_panel_core,
    plotScatter2D_panel_core
)

# --- 2D panel tools ---
from .panel_2d import (
    plot2D_panel_core,
    plot2D_pcolormesh_panel_core,
    add_colorbar_cm
)

# --- 3D panel tools ---
from .panel_3d import (
    quiver3_advanced,
    quiver3_advanced_panel
)

# --- High-level vector-field panel ---
from .vectorfield_panel import (
    PlotVectorfieldPanel,
    plot_vectorfield_panels
)

__all__ = [
    "create_paper_figure",
    "add_axes_cm",
    "add_label_cm",
    "crop_image",
    "Show_Axes_Margins",
    "add_reference_axes",
    "plotLinLin_panel_core",
    "plotLogLog_panel_core",
    "plotScatter2D_panel_core",
    "plot2D_panel_core",
    "plot2D_pcolormesh_panel_core",
    "add_colorbar_cm",
    "quiver3_advanced",
    "quiver3_advanced_panel",
    "PlotVectorfieldPanel",
    "plot_vectorfield_panels",
    "apply_tick_style"
]
