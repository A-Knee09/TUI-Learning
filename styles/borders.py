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

    CSS = """
    Screen {
        align: center middle
    }
    """

    def compose(self) -> ComposeResult:

        self.widget1 = Static(TEXT)
        yield self.widget1

    def on_mount(self) -> None:

        # self.widget1.styles.align = ("center", "middle")

        self.widget1.styles.background = "darkslategray"
        self.widget1.styles.width = "60"
        self.widget1.styles.height = "15"

        self.widget1.styles.padding = (2, 4)
        self.widget1.styles.margin = (0, 0)

        self.widget1.styles.border = ("round", "teal")
        self.widget1.border_title = "TUI Learning using Textual"
        self.widget1.border_subtitle = "By Ani"
        self.widget1.styles.border_title_align = "center"

    def on_key(self) -> None:
        self.exit()


if __name__ == "__main__":

    app = MyApp()
    app.run()
