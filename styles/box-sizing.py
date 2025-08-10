from textual.app import App, ComposeResult
from textual.widgets import Static

TEXT = """I must not fear.
Fear is the mind-killer.
Fear is the little-death that brings total obliteration.
I will face my fear.
I will permit it to pass over me and through me.
And when it has gone past, I will turn the inner eye to see its path.
Where the fear has gone there will be nothing. Only I will remain."""


class MyApp(App):

    def compose(self) -> ComposeResult:

        self.widget1 = Static(TEXT)
        yield self.widget1

        self.widget2 = Static(TEXT)
        yield self.widget2

    def on_mount(self) -> None:

        self.screen.styles.background = "darkslategray"

        self.widget1.styles.background = "darkslategray"
        self.widget1.styles.width = "30"
        self.widget1.styles.height = "6"

        self.widget1.styles.padding = 1
        self.widget1.styles.margin = 2

        self.widget1.styles.border = ("panel", "black")
        self.widget1.border_title = "Default border box"
        self.widget1.border_subtitle = "By Frank Hubert, in 'Dune'"
        self.widget1.styles.border_title_align = "center"

        self.widget2.styles.background = "darkslategray"
        self.widget2.styles.width = "30"
        self.widget2.styles.height = "6"

        self.widget2.styles.padding = 1
        self.widget2.styles.margin = 2

        self.widget2.styles.border = ("panel", "black")
        self.widget2.border_title = "Content Box"
        self.widget2.border_subtitle = "By Frank Hubert, in 'Dune'"
        self.widget2.styles.border_title_align = "center"

        self.widget2.styles.box_sizing = "content-box"

    def on_key(self) -> None:
        self.exit()


if __name__ == "__main__":

    app = MyApp()
    app.run()
