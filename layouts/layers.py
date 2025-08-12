from textual.app import App, ComposeResult
from textual.widgets import Static
from textual import events


class MyApp(App):

    CSS_PATH = "./tcss/layers.tcss"

    def compose(self) -> ComposeResult:

        yield Static("box 1 (layer = above)", id="box1")
        yield Static("box 2 (layer = below)", id="box2")

    def on_key(self, event: events.Key) -> None:
        if event.key == "q":
            self.exit()


if __name__ == "__main__":
    app = MyApp()
    app.run()
