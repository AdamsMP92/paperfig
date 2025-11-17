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


def add_label_cm(fig, text, x_cm, y_cm, fig_width_cm, fig_height_cm, **kwargs):
    fig.text(x_cm / fig_width_cm, y_cm / fig_height_cm, text, **kwargs)
