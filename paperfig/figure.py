import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.lines import Line2D

def create_paper_figure(
        width_cm=8.5,
        height_cm=6.0,
        fontsize=7,
        dpi=600,
        use_latex=True,
        use_pgf=False,
        fontfamily="serif",
        fontserif="Computer Modern Roman"
):
    cm = 1 / 2.54

    rc = {
        "figure.dpi": dpi,
        "savefig.dpi": dpi,
        "axes.linewidth": 0.5,
        "lines.linewidth": 0.6,
        "axes.labelsize": fontsize,
        "axes.titlesize": fontsize,
        "xtick.labelsize": fontsize - 1,
        "ytick.labelsize": fontsize - 1,
        "legend.fontsize": fontsize - 1,
    }

    if use_latex:
        rc.update({
            "text.usetex": True,
            "font.family": "serif",
            "font.serif": [fontserif],
            "axes.unicode_minus": False,
        })
        if use_pgf:
            rc.update({
                "pgf.texsystem": "pdflatex",
                "pgf.preamble": r"\usepackage{amsmath,amssymb}\usepackage{siunitx}",
            })
    else:
        rc.update({
            "text.usetex": False,
            "font.family": fontfamily,
        })

    mpl.rcParams.update(rc)

    fig = plt.figure(figsize=(width_cm * cm, height_cm * cm))
    return fig


def add_axes_cm(fig, left_cm, bottom_cm, width_cm, height_cm):
    W, H = fig.get_size_inches()
    return fig.add_axes([
        left_cm / (W * 2.54),
        bottom_cm / (H * 2.54),
        width_cm / (W * 2.54),
        height_cm / (H * 2.54)
    ])

# add_label_cm ########################################
def add_label_cm(fig, text, x_cm, y_cm, **kwargs):
    """
    Add a text label using cm coordinates relative to the figure size.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        The figure to draw on.
    text : str
        Label text.
    x_cm, y_cm : float
        Position in cm relative to figure size.
    **kwargs : dict
        Additional styling arguments passed to fig.text().
    """

    # --- 1) Get figure size in cm ---
    w_in, h_in = fig.get_size_inches()
    w_cm = w_in * 2.54
    h_cm = h_in * 2.54

    # --- 2) Normalize cm → figure coordinates ---
    x_rel = x_cm / w_cm
    y_rel = y_cm / h_cm

    # --- 3) Add text ---
    fig.text(x_rel, y_rel, text, **kwargs)




def add_folder_box_cm(fig, x_cm, y_cm, w_cm, h_cm,
                      text="", tab_w_cm=1.0, tab_h_cm=0.4,
                      facecolor="white", edgecolor="black",
                      linewidth=1.2, text_kwargs=None):
    """
    Zeichnet einen folder-artigen Box-Kasten (mit Tab) in cm-Koordinaten
    relativ zur gesamten Figure.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        Die Figure, auf der gezeichnet wird.
    x_cm, y_cm : float
        Linke untere Ecke in cm.
    w_cm, h_cm : float
        Breite und Höhe der Box in cm.
    text : str
        Beschriftung innerhalb der Box.
    tab_w_cm : float
        Breite des Tabs oben links.
    tab_h_cm : float
        Höhe des Tabs.
    facecolor : str
        Innenfarbe.
    edgecolor : str
        Randfarbe.
    linewidth : float
        Linienbreite.
    text_kwargs : dict
        Style-Einstellungen für den Text.
    """

    if text_kwargs is None:
        text_kwargs = dict(ha="center", va="center", fontsize=11)

    # --- 1) Figuregröße in cm ---
    fig_w_cm = fig.get_size_inches()[0] * 2.54
    fig_h_cm = fig.get_size_inches()[1] * 2.54

    # --- 2) Umrechnung cm → relative fig-Koordinaten ---
    def rel(x_cm, y_cm):
        return (x_cm / fig_w_cm, y_cm / fig_h_cm)

    # --- 3) Folder-Polygon definieren (mit Tab oben links) ---
    folder_pts_cm = [
        (x_cm,             y_cm),                # unten links
        (x_cm,             y_cm + h_cm - tab_h_cm),
        (x_cm + tab_w_cm,  y_cm + h_cm),         # Tab oben links
        (x_cm + w_cm,      y_cm + h_cm),
        (x_cm + w_cm,      y_cm),
    ]

    # In fig-relativ umrechnen
    folder_pts_rel = [rel(x, y) for x, y in folder_pts_cm]

    # --- 4) Polygon zeichnen ---
    poly = patches.Polygon(
        folder_pts_rel,
        closed=True,
        facecolor=facecolor,
        edgecolor=edgecolor,
        linewidth=linewidth,
        transform=fig.transFigure
    )
    fig.patches.append(poly)

    # --- 5) Text in die Mitte ---
    text_x_rel = (x_cm + w_cm/2) / fig_w_cm
    text_y_rel = (y_cm + h_cm/2) / fig_h_cm
    fig.text(text_x_rel, text_y_rel, text, **text_kwargs)


def add_line_cm(fig, x1_cm, y1_cm, x2_cm, y2_cm, **kwargs):

    # Figure size in cm
    w_in, h_in = fig.get_size_inches()
    w_cm = w_in * 2.54
    h_cm = h_in * 2.54

    # Convert to figure coords
    x1 = x1_cm / w_cm
    y1 = y1_cm / h_cm
    x2 = x2_cm / w_cm
    y2 = y2_cm / h_cm

    # Create line artist
    line = Line2D([x1, x2], [y1, y2], **kwargs)

    # Add directly to figure (not to an Axes)
    fig.add_artist(line)