# paperfig
Python Figure Plot package




# LaTeX–PGF Environment Setup (pixi + Matplotlib)

This document explains how to set up a fully reproducible LaTeX/PGF figure environment using:

- pixi (isolated Python environments)
- macOS LaTeX distribution (MacTeX or BasicTeX)
- Matplotlib PGF backend
- Latin Modern / CM-Super fonts

---

## 1. Install pixi

```bash
curl -fsSL https://pixi.sh/install.sh | bash
```

Check installation:

```bash
pixi --version
```

---

## 2. Create a pixi environment

In the project root:

```bash
pixi init
```

Add dependencies:

```bash
pixi add python
pixi add matplotlib
pixi add numpy
pixi add pillow
```

Activate the environment:

```bash
pixi shell
```

---

## 3. Install LaTeX on macOS

### Option A (recommended): Install MacTeX

Download:

https://tug.org/mactex/

### Option B (lightweight): Install BasicTeX

```bash
brew install --cask basictex
```

Update TeXLive:

```bash
sudo tlmgr update --self
sudo tlmgr update --all
```

---

## 4. Install required LaTeX fonts

```bash
sudo tlmgr install lmodern
sudo tlmgr install cm-super
sudo tlmgr install ec
sudo tlmgr install collection-fontsrecommended
```

Verify fonts:

```bash
kpsewhich lmroman10-regular.otf
kpsewhich cmr10.tfm
```

---

## 5. Configure Matplotlib to use PGF

```python
import matplotlib as mpl

mpl.use("pgf")

mpl.rcParams.update({
    "text.usetex": True,
    "pgf.texsystem": "xelatex",
    "pgf.preamble": r"""
        \usepackage{lmodern}
        \usepackage[T1]{fontenc}
    """,
    "font.family": "serif",
})
```

---

## 6. Test PGF export

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(3, 2))
plt.plot([1, 2, 3], [1, 4, 9])
plt.xlabel(r"$y = x^2$")
plt.title("PGF Test")

plt.savefig("test_pgf.pdf")
print("PGF export OK")
```

---

## 7. Setup script

Place in `scripts/setup_latex_pgf.sh`:

```bash
#!/usr/bin/env bash
set -e

echo "=== PGF / LaTeX Setup ==="

if ! command -v pdflatex >/dev/null 2>&1; then
    echo "❌ pdflatex not found. Install MacTeX or BasicTeX first."
    exit 1
fi

echo "Updating tlmgr..."
sudo tlmgr update --self || true

echo "Installing required fonts..."
sudo tlmgr install lmodern || true
sudo tlmgr install cm-super || true
sudo tlmgr install ec || true
sudo tlmgr install collection-fontsrecommended || true

echo "Checking font installation…"
kpsewhich lmroman10-regular.otf || echo "⚠️ Latin Modern missing"
kpsewhich cmr10.tfm || echo "⚠️ Computer Modern missing"

echo "Setup complete."
```

Make executable:

```bash
chmod +x scripts/setup_latex_pgf.sh
```

---

## 8. pixi integration

Add to `pixi.toml`:

```toml
[tool.latex_setup]
cmd = "sh scripts/setup_latex_pgf.sh"
```

Run with:

```bash
pixi run latex_setup
```

---

## 9. Optional environment check

`paperfig/check_env.py`:

```python
import shutil
import matplotlib.font_manager as fm

print("pdflatex:", shutil.which("pdflatex"))
print("xelatex:", shutil.which("xelatex"))

for f in fm.findSystemFonts():
    if "lm" in f.lower() or "latin" in f.lower():
        print("LATEX FONT:", f)
```

Run:

```bash
pixi run python paperfig/check_env.py
```

---

## 10. Summary

After completing this setup:

- pixi manages a clean reproducible Python environment  
- LaTeX (MacTeX/BasicTeX) is installed correctly  
- Latin Modern & CM-Super fonts are available  
- Matplotlib PGF backend works without warnings  
- Figures are perfectly reproducible across machines  
