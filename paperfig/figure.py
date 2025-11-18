import matplotlib as mpl
import matplotlib.pyplot as plt

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

