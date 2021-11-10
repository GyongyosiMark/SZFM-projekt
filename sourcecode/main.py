from kivy.app import App
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock

def collides(rect1, rect2):
    # sima AABB utkozes detektor: ha a negyzetek fedik egymast akkor utkoznek
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
            self.player = Rectangle(source="../animation/player.png", size=(80,80), pos=(60, 60))
            self.enemy = Rectangle(source="../animation/enemy.png", pos=(400, 100))

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

    isJump = False
    jumpCount = 12

    def move_step(self, dt):
        # mostmar a lepesek egysegesek eszkoztol fuggetlenul(idohoz van kotve)
        currentx = self.player.pos[0]
        currenty = self.player.pos[1]

        step_size = 250 * dt

        if 'a' in self.keysPressed and currentx > step_size:
            currentx -= step_size
        if 'd' in self.keysPressed and currentx < self.size[0] - self.player.size[0] - step_size:
            currentx += step_size
        if not self.isJump:
            if 'w' in self.keysPressed:
                self.isJump = True
        else:
            if self.jumpCount >= -12:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                currenty += (self.jumpCount ** 2) * 0.2 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 12
        #gravitacio
        if (not self.isJump) and currenty > self.player.size[1] - step_size:
            currenty -= 5
        # delta ertek aminek segitsegevel meg az utkozes elott erzekeljuk azt
        self.player.pos = (currentx, currenty)
        delta = (currentx + step_size, currenty + step_size)
        if collides((self.player.pos, self.player.size), (self.enemy.pos, self.enemy.size)):
            print("Collides!")
            currentx = delta[0]
            currenty = delta[1]
            self.player.pos = (currentx, currenty)


class PlatformerApp(App):
    # példányosítunk egy alkalmazást ami örököl az ősosztályból
    def build(self):
        # ez a metódus építi meg az appunkat
        return PlatformerGame()


if __name__ == "__main__":
    # app futtatása
    PlatformerApp().run()
