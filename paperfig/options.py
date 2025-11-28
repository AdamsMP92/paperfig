class PaperFigOptions:
    def __init__(
        self,
        # ---- Tick config ----
        major_tick_length=2.0,
        major_tick_width=0.3,
        minor_tick_length=1.0,
        minor_tick_width=0.15,
        ticks_fontsize=6,
        tick_direction="in",

        # ---- Colors ----
        colors=["#D55E00", "#0072B2", "#009E73"],

        # ---- Fonts ----
        fontsize=7,
        #font_family="sans-serif",
        #math_font="stixsans",
        #use_tex=False,
        font_family="serif",
        math_font="cm",
        use_tex=True,
        fontserif="Computer Modern Roman",

        # ---- Axis frame ----
        spine_width=0.6,
        spine_color="black",

        # ---- Lines ----
        linewidth=0.8,

        # ---- Grid ----
        grid_color="0.85",

        # ---- Background ----
        facecolor="white",

        # ---- DPI ----
        dpi=600
    ):
        # Copy all values into attributes
        self.major_tick_length = major_tick_length
        self.major_tick_width = major_tick_width
        self.minor_tick_length = minor_tick_length
        self.minor_tick_width = minor_tick_width
        self.tick_direction = tick_direction
        self.ticks_fontsize = ticks_fontsize

        self.colors = colors

        self.fontsize = fontsize
        self.font_family = font_family
        self.math_font = math_font
        self.use_tex = use_tex
        self.fontserif=fontserif

        self.spine_width = spine_width
        self.spine_color = spine_color

        self.linewidth = linewidth
        self.grid_color = grid_color

        self.facecolor = facecolor
        self.dpi = dpi


# --- Global defaults ---
global_options = PaperFigOptions()
