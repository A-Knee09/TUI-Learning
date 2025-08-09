from textual.app import App


class MyApp(App):
    def on_mount(self) -> None:
        self.screen.styles.background = "#737399"

        self.screen.styles.border = ("heavy", "white")


if __name__ == "__main__":
    app = MyApp()
    app.run()
