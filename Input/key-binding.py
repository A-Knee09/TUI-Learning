"""
Keys may be associated with actions for a given widget. This association is known as a key binding.

To create bindings, add a BINDINGS class variable to your app or widget. This should be a list of tuples of three strings. The first value is the key, the second is the action, the third value is a short human readable description.
"""

from textual.app import App, ComposeResult
from textual.color import Color
from textual.widgets import Footer, Static


class Bar(Static):
    pass


class BindingApp(App):
    CSS_PATH = "./tcss/key-bind.tcss"
    BINDINGS = [
        ("r", "add_bar('red')", "Add Red"),
        ("g", "add_bar('green')", "Add Green"),
        ("b", "add_bar('blue')", "Add Blue"),
    ]

    def compose(self) -> ComposeResult:
        yield Footer()

    def action_add_bar(self, color: str) -> None:
        bar = Bar(color)
        bar.styles.background = Color.parse(color).with_alpha(0.5)
        self.mount(bar)
        self.call_after_refresh(self.screen.scroll_end, animate=False)


if __name__ == "__main__":
    app = BindingApp()
    app.run()
