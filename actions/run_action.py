from textual.app import App
from textual import events


class MyApp(App):

    def action_set_background(self, color: str) -> None:

        self.screen.styles.background = color

    async def on_key(self, event: events.Key) -> None:
        if event.key == "b":
            await self.run_action("set_background('cornflowerblue')")


if __name__ == "__main__":
    app = MyApp()
    app.run()
