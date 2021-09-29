from kivy.app import App
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import ObjectProperty


class PlatformerGame(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        # keyboard objektum, ez altal veszunk be keyboard inputot

        self._keyboard.bind(on_key_down=self._on_key_down)
        # bindoljuk hozza azt, hogy ha van lenyomott billentyu csinaljon valamit

        with self.canvas:
            self.player = Rectangle(source="player.png", pos=(0, 0), size=(100, 100))

    def _on_keyboard_closed(self):
        # ha nincs mar input akkor unbindoljuk
        self._keyboard_unbind(on_key_down=self._on_key_down)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        # mi tortenik ha lenyomjuk
        currentx = self.player.pos[0]
        currenty = self.player.pos[1]

        if text == "w":
            currenty += 1
        if text == 's':
            currenty -= 1
        if text == 'a':
            currentx -= 1
        if text == 'd':
            currentx += 1

        self.player.pos = (currentx, currenty)

        # példányosítunk egy alkalmazást ami örököl az ősosztályból


class PlatformerApp(App):
    def build(self):  # ez a metódus építi meg az appunkat
        return PlatformerGame()


if __name__ == "__main__":
    PlatformerApp().run()
