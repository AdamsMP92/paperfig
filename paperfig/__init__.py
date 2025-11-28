"""
paperfig: A publication-quality Python figure toolkit with cm-accurate layout,
LaTeX typography, high-end 1D/2D panels, and PyVista-powered 3D rendering.
"""

# --- Options system ---
from .options import PaperFigOptions, global_options

# --- Figure creation & layout helpers ---
from .figure import (
    create_paper_figure,
    add_axes_cm,
    add_label_cm,
    add_folder_box_cm,
    add_line_cm
)

# --- Utility helpers ---
from .utils import (
    crop_image,
    Show_Axes_Margins,
    add_reference_axes,
    apply_tick_style,
    apply_label_style,
    apply_grid_style
)

# --- 1D panel tools ---d
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
    # Options
    "PaperFigOptions",
    "global_options",

    # Figure/axes
    "create_paper_figure",
    "add_axes_cm",
    "add_label_cm",
    "add_folder_box_cm",
    "add_line_cm"

    # Utilities
    "crop_image",
    "Show_Axes_Margins",
    "add_reference_axes",
    "apply_tick_style",
    "apply_label_style",
    "apply_grid_style",

    # 1D
    "plotLinLin_panel_core",
    "plotLogLog_panel_core",
    "plotScatter2D_panel_core",

    # 2D
    "plot2D_panel_core",
    "plot2D_pcolormesh_panel_core",
    "add_colorbar_cm",

    # 3D
    "quiver3_advanced",
    "quiver3_advanced_panel",

    # Vectorfield
    "PlotVectorfieldPanel",
    "plot_vectorfield_panels"
]
