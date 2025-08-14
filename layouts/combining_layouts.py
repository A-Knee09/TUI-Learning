from textual.app import App, ComposeResult
from textual.widgets import Static, Header
from textual import events
from textual.containers import Container, Horizontal, VerticalScroll

from textual.app import App, ComposeResult
from textual.widgets import Header, Static
from textual.containers import Container, VerticalScroll


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

    def on_mount(self) -> None:
        """Set border titles after widgets are mounted"""
        # Getting references to containers and set titles
        left_pane = self.query_one("#left-pane")
        left_pane.border_title = "Scrollable List"
        left_pane.border_subtitle = "Vertical Navigation"

        top_right = self.query_one("#top-right")
        top_right.border_title = "Header Bar"
        top_right.border_subtitle = "Horizontal Items"

        bottom_right = self.query_one("#bottom-right")
        bottom_right.border_title = "Control Panel"
        bottom_right.border_subtitle = "Grid of Buttons"


if __name__ == "__main__":
    app = MyApp()
    app.run()
