from textual.app import App, ComposeResult
from textual.widgets import Static
from textual import events


TEXT = """\
Docking a widget removes it from the layout and fixes its position, aligned to either the top, right, bottom, or left edges of a container.

Docked widgets will not scroll out of view, making them ideal for sticky headers, footers, and sidebars."""


class MyApp(App):

    CSS_PATH = "./tcss/grid-docking.tcss"

    def compose(self) -> ComposeResult:

        yield Static("Sidebar", id="sidebar")
        yield Static(TEXT * 200, id="body")

    def on_key(self, event: events.Key):
        if event.key == "q":
            self.exit()


if __name__ == "__main__":
    app = MyApp()
    app.run()
