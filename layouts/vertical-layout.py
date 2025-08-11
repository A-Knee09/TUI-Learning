from textual.app import App, ComposeResult
from textual.widgets import Static

from textual import events


class MyApp(App):

    CSS_PATH = "vertical-layout.tcss"

    def compose(self) -> ComposeResult:

        yield Static("One", classes="box")
        yield Static("Two", classes="box")
        yield Static("Three", classes="box")

    def on_key(self, event: events.Key) -> None:
        if event.key == "q":
            self.exit()


if __name__ == "__main__":
    app = MyApp()
    app.run()
