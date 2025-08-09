from textual.app import App, ComposeResult
from textual.widgets import Static
from textual import events

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

    def on_mount(self) -> None:
        self.widget1.styles.background = "purple"
        self.widget1.styles.width = 30
        # self.widget1.styles.height = 10
        self.widget1.styles.height = "auto"

    def on_key(self) -> None:
        self.exit()


if __name__ == "__main__":
    app = MyApp()
    app.run()
