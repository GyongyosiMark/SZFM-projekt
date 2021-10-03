from kivy.app import App
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock


def collides(rect1, rect2):
    #sima AABB utkozes detektor: ha a negyzetek fedik egymast akkor utkoznek
    r1x = rect1[0][0]
    r1y = rect1[0][1]
    r2x = rect2[0][0]
    r2y = rect2[0][1]
    r1w = rect1[1][0]
    r1h = rect1[1][1]
    r2w = rect2[1][0]
    r2h = rect2[1][1]

    if r1x < r2x + r2w and r1x + r1w > r2x and r1y < r2y + r2h and r1y + r1h > r2y:
        return True
    else:
        return False


class PlatformerGame(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        # keyboard objektum, ez altal veszunk be keyboard inputot

        self._keyboard.bind(on_key_down=self._on_key_down)
        # bindoljuk hozza azt, hogy ha van lenyomott billentyu csinaljon valamit
        self._keyboard.bind(on_key_up=self._on_key_up)
        # ha elengedjuk a billentyut

        with self.canvas:
            # letrehozzuk a karakter, alakitjuk a kv fileba
            self.player = Rectangle(source="player.png")
            self.enemy = Rectangle(source="enemy.png",pos=(400,400))

        self.keysPressed = set()
        # halmazban taroljuk az aktualisan lenyomott billentyuket

        Clock.schedule_interval(self.move_step, 0)
        # minden frameben tortenik valami (ezesetben a mozgas)

    def _on_keyboard_closed(self):
        # ha nincs mar input akkor unbindoljuk
        self._keyboard_unbind(on_key_down=self._on_key_down)
        self._keyboard_unbind(on_key_up=self._on_key_up)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        # mi tortenik ha lenyomjuk
        self.keysPressed.add(text)

    def _on_key_up(self, keyboard, keycode):
        # ha mar nem nyomjuk akkor elvesszuk a halmazbol
        text = keycode[1]
        if text in self.keysPressed:
            self.keysPressed.remove(text)

    def move_step(self, dt):
        #mostmar a lepesek egysegesek eszkoztol fuggetlenul(idohoz van kotve)
        currentx = self.player.pos[0]
        currenty = self.player.pos[1]

        step_size = 100 * dt

        if 'w' in self.keysPressed:
            currenty += step_size
        if 's' in self.keysPressed:
            currenty -= step_size
        if 'a' in self.keysPressed:
            currentx -= step_size
        if 'd' in self.keysPressed:
            currentx += step_size

        self.player.pos = (currentx, currenty)

        if collides((self.player.pos,self.player.size),(self.enemy.pos,self.enemy.size)):
            print("Collides!")


class PlatformerApp(App):
    # példányosítunk egy alkalmazást ami örököl az ősosztályból
    def build(self):
        # ez a metódus építi meg az appunkat
        return PlatformerGame()


if __name__ == "__main__":
    PlatformerApp().run()
