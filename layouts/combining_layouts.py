from textual.app import App, ComposeResult
from textual.widgets import Static, Header
from textual import events
from textual.containers import Container, Horizontal, VerticalScroll


class MyApp(App):

    CSS_PATH = "./tcss/combining.tcss"

    def compose(self) -> ComposeResult:

        yield Header()
        with Container(id="app-grid"):
            with VerticalScroll(id="left-pane"):
                for number in range(15):
                    yield Static(f"Vertical Layout: Child {number}")

            with Container(id="top-right"):
                yield Static("Horizontal")
                yield Static("Positioned")
                yield Static("Children")
                yield Static("Here")

            with Container(id="bottom-right"):
                yield Static("This")
                yield Static("Panel")
                yield Static("Is")
                yield Static("Using")
                yield Static("Grid Layout")

    def on_key(self, event: events.Key) -> None:

        if event.key == "q":
            self.exit()


if __name__ == "__main__":
    app = MyApp()
    app.run()
