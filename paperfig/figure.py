import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.lines import Line2D

def create_paper_figure(
        width_cm=8.5,
        height_cm=6.0,
        use_latex=True,
        fontfamily="serif",
        fontserif="Computer Modern Roman"
):
   
    mpl.use("pdf")
    cm = 1 / 2.54

    rc = {
        "axes.linewidth": 0.5,
        "lines.linewidth": 0.6
    }

    if use_latex:
        rc.update({
            "text.usetex": True,
            "font.family": "serif",
            "font.serif": [fontserif],
            "axes.unicode_minus": False,

            # Optional für perfekte PDF-Fonts
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
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
def add_label_cm(
        fig,
        text,
        x_cm,
        y_cm,
        fig_width_cm=None,
        fig_height_cm=None,
        centered=False,
        **kwargs
):
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
    fig_width_cm, fig_height_cm : float, optional
        Explicit figure dimensions in cm. These keep older examples working;
        by default the size is read from ``fig``.
    centered : bool, default False
        If True, (x_cm, y_cm) is interpreted as the text center.
    **kwargs : dict
        Additional styling arguments passed to fig.text().
    """

    # --- 1) Get figure size in cm ---
    w_in, h_in = fig.get_size_inches()
    w_cm = fig_width_cm if fig_width_cm is not None else w_in * 2.54
    h_cm = fig_height_cm if fig_height_cm is not None else h_in * 2.54

    # --- 2) Normalize cm → figure coordinates ---
    x_rel = x_cm / w_cm
    y_rel = y_cm / h_cm

    # --- 3) Optional center anchoring ---
    if centered:
        kwargs.setdefault("ha", "center")
        kwargs.setdefault("va", "center")
        kwargs.setdefault("rotation_mode", "anchor")

    # --- 4) Add text ---
    return fig.text(x_rel, y_rel, text, **kwargs)




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
        text_kwargs = dict(ha="center", va="center")

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
    text_artist = fig.text(text_x_rel, text_y_rel, text, **text_kwargs)
    return poly, text_artist


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
    return line


def add_color_box_cm(
        fig,
        x_cm,
        y_cm,
        w_cm,
        h_cm,
        color,
        alpha=1.0,
        edgecolor="black",
        linewidth=0.5,
        zorder=None
):
    """
    Add a colored rectangle using cm coordinates relative to the figure.
    """

    fig_w_cm = fig.get_size_inches()[0] * 2.54
    fig_h_cm = fig.get_size_inches()[1] * 2.54

    rect = patches.Rectangle(
        (x_cm / fig_w_cm, y_cm / fig_h_cm),
        w_cm / fig_w_cm,
        h_cm / fig_h_cm,
        transform=fig.transFigure,
        facecolor=color,
        edgecolor=edgecolor,
        linewidth=linewidth,
        alpha=alpha,
        zorder=zorder
    )

    fig.patches.append(rect)
    return rect
