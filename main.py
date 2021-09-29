from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window


class PlatformerGame(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.keyboard = Window.request_keyboard(self._on_keyboard_closed, self)


# példányosítunk egy alkalmazást ami örököl az ősosztályból
class PlatformerApp(App):
    def build(self):  # ez a metódus építi meg az appunkat
        return PlatformerGame()


if __name__ == "__main""":
    PlatformerApp().run()
