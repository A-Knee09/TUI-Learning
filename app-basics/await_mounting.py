"""
Textual guarantees that the mounting will be complete by the next message handler, but not immediately after the call to mount(). This may be a problem if you want to make any changes to the widget in the same message handler.

We can use await for this to load Welcome() fully before executing the next line
"""

from textual.app import App
from textual import events
from textual.widgets import Welcome, Button


class MyApp(App):

    async def on_key(self) -> None:
        await self.mount(Welcome())
        self.query_one(Button).label = "YES"


if __name__ == "__main__":
    myapp = MyApp()
    myapp.run()
