from textual.app import App, ComposeResult
from textual.widgets import Static
from textual.color import Color


class WidgetApp(App):
    def compose(self) -> ComposeResult:
        self.widget1 = Static("Static Widget 1")
        yield self.widget1

        self.widget2 = Static("Static Widget 2")
        yield self.widget2

        self.widget3 = Static("Static Widget 3")
        yield self.widget3

    def on_mount(self) -> None:
        self.screen.styles.background = "#e6e7f7"
        self.widget1.styles.background = "#9595de"
        self.widget2.styles.background = "#8fb59f"
        self.widget2.styles.color = "#4e6113"
        self.widget3.styles.background = "hsl(150,42.9%,49.4%)"
        self.widget3.styles.background = Color(191, 78, 96)


if __name__ == "__main__":
    app = WidgetApp()
    app.run()
