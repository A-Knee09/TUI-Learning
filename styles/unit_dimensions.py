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

        self.widget1.styles.background = "purple"
        self.widget2.styles.background = "green"

        self.widget1.styles.color = "black"

        self.widget1.styles.width = "30"

        self.widget1.styles.height = "2fr"
        self.widget2.styles.height = "1fr"

        self.widget1.styles.padding = (2, 4)
        self.widget2.styles.padding = 2

    def on_key(self) -> None:
        self.exit()


if __name__ == "__main__":
    app = MyApp()
    app.run()
