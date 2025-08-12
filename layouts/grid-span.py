from textual.app import App, ComposeResult
from textual.widgets import Static
from textual import events


class MyApp(App):

    CSS_PATH = "./tcss/grid-cell-span.tcss"

    def compose(self) -> ComposeResult:

        yield Static("One", classes="box")
        yield Static("Two", classes="box", id="two")
        yield Static("Three", classes="box")
        yield Static("Four", classes="box")
        yield Static("Five", classes="box")
        yield Static("Six", classes="box")

    def on_key(self, event: events.Key):

        if event.key == "q":
            self.exit()


if __name__ == "__main__":
    app = MyApp()
    app.run()
