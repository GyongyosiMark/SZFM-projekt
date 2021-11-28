
import pygame
from pygame.locals import *
from pygame import mixer
import tkinter as tk
import mysql.connector
import getpass
import os

current_player = "guest"

################################################################################################
def init_database():
    try:
        database_username = os.environ["database_name"]
        database_password = os.environ["database_password"]
    except:
        database_username = input("Database username: ")
        database_password = getpass.getpass("Database password: ")

    my_database = mysql.connector.connect(
        host="localhost",
        user=database_username,
        passwd=database_password
    )

    my_cursor = my_database.cursor()
    my_cursor.execute("CREATE DATABASE IF NOT EXISTS loginSystem;")

    my_database = mysql.connector.connect(
        host="localhost",
        user=database_username,
        passwd=database_password,
        database="loginSystem"
    )

    my_cursor = my_database.cursor()

    my_cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        id MEDIUMINT NOT NULL AUTO_INCREMENT,
        username VARCHAR(30) NOT NULL,
        password VARCHAR(30) NOT NULL,
        email VARCHAR(30) NOT NULL,
        PRIMARY KEY (id, username),
        UNIQUE (id),
        UNIQUE (username),
        UNIQUE(email)
    );""")

    return my_database, my_cursor

try:
    my_database, my_cursor = init_database()
except mysql.connector.errors.ProgrammingError:
    print("Invalid username or password.")
    exit()

window = tk.Tk()
window.title('Hello Python')
window.geometry("600x600")

tk.Label(window, text="Username").pack()
e1 = tk.Entry(window)
e1.pack()
tk.Label(window, text="Password").pack()
e2 = tk.Entry(window, show="*")
e2.pack()

def login():
    my_cursor.execute(f"SELECT password FROM users WHERE username = '{e1.get()}'")
    result = my_cursor.fetchall()
    if len(result) == 0:
        print("This username does not exist.")
    else:
        if result[0][0] == e2.get():
            current_player = e1.get()
            print("Login successful")
        else:
            print("Invalid username or password")

tk.Button(window, text="Login", command=login).pack()
tk.Label(window, text="").pack()
tk.Label(window, text="Username").pack()
r1 = tk.Entry(window)
r1.pack()
tk.Label(window, text="Password").pack()
r2 = tk.Entry(window, show="*")
r2.pack()
tk.Label(window, text="Email").pack()
r3 = tk.Entry(window)
r3.pack()

def register():
    try:
        my_cursor.execute("SELECT MAX(id + 1) FROM users")
        id = my_cursor.fetchall()[0][0]
        if not id:
            id = 1
        my_cursor.execute(f"""
        INSERT INTO users (id, username, password, email)
        VALUES ({id}, '{r1.get()}', '{r2.get()}', '{r3.get()}')
        """)
        my_database.commit()
        print("Successfully registered.")
    except mysql.connector.errors.IntegrityError:
        print("The username or email is already taken.")
        my_database.rollback()

tk.Button(window, text="Register", command=register).pack()
tk.Label(window, text="").pack()
tk.Button(window, text="Play", command=window.destroy).pack()
window.mainloop()

################################################################################################

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()

#rogzitunk egy frissites szamlalot, hogy egyenlo legyen kulonbozo gepeken
clock = pygame.time.Clock()
fps = 60

#screen merete
screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')

# a jatekbeli blokkok merete
tile_size = 50
main_manu = True
game_over = 0

# blokkok aniamacioja
bg_img = pygame.image.load('../animation/bg1.png')

# kepek betoltese
start_img = pygame.image.load('../animation/start_button.png')
exit_img = pygame.image.load('../animation/exit_button.png')
highscore_img = pygame.image.load('../animation/highscore_button.png')
restart_img = pygame.image.load('../animation/restart_btn.png')

#jatek zene
pygame.mixer.music.load('../sound/bgrm.wav')
pygame.mixer.music.play(-1, 0.0, 5000)
pygame.mixer.music.set_volume(0.05)
coin_fx = pygame.mixer.Sound('../sound/coin.wav')
coin_fx.set_volume(0.1)
death_fx = pygame.mixer.Sound('../sound/death.wav')
death_fx.set_volume(0.1)
jump_fx = pygame.mixer.Sound('../sound/jump.wav')
jump_fx.set_volume(0.05)
win_fx = pygame.mixer.Sound('../sound/win.wav')
win_fx.set_volume(0.1)



#negyzethalo a fejleszteshez
def draw_grid():
    for line in range(0, 20):
        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):
        action = False

        #egér pozicio
        pos = pygame.mouse.get_pos()

        #egérmutató/kattintas
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #gomb megrajzolasa
        screen.blit(self.image, self.rect)

        return action

#player osztaly
class Player:
    def __init__(self, x, y):
        # a resetbe lett áthelyezve
        self.reset(x, y)

    def update(self, game_over):
        dx = 0
        dy = 0
        if game_over == 0:
            # input a billentyukrol
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and self.jumped == False and self.in_air == False:
                jump_fx.play()
                self.vel_y = -15
                self.jumped = True
            if not key[pygame.K_SPACE]:
                self.jumped = False
            if key[pygame.K_LEFT]:
                dx -= 5
                self.flip = True
                self.direction = -1
            if key[pygame.K_RIGHT]:
                dx += 5
                self.flip = False
                self.direction = 1

            # gravitacio
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y

            #utkozes
            self.in_air = True
            for tile in world.tile_list:
                # vizsszintes utkozes
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                # fuggoleges utkozes
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    # alulrol utkozes blokkal, ugrasnal
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    # felulrol utkozes blokkal, esesnel
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
                        self.in_air = False

            # lavaval utkozes
            if pygame.sprite.spritecollide(self, lava_group, False):
                death_fx.play()
                game_over = -1

            # csapdakkal utkozes
            if pygame.sprite.spritecollide(self, trap_group, False):
                game_over = -1
                death_fx.play()

            #enemyvel utkozes
            if pygame.sprite.spritecollide(self, enemy_group, False):
                death_fx.play()
                game_over = -1

            # player poziziojanak frissittese
            self.rect.x += dx
            self.rect.y += dy

            if self.rect.bottom > screen_height:
                self.rect.bottom = screen_height
                dy = 0
        elif game_over == -1:
            self.image = self.dead_image
            if self.rect.y > 200:
                self.rect.y -= 5

        # player rajzolasa a kepenyore
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

        return game_over

    def reset(self, x , y):
        #player animacio, pozicio, mozgas
        img = pygame.image.load('../animation/p1_stand.png')
        self.dead_image = pygame.image.load('../animation/ghost.png')
        self.image = pygame.transform.scale(img, (40, 80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.in_air = True
        self.direction = 1
        self.flip = False


#palya osztalya
class World:
    def __init__(self, data):
        self.tile_list = []
        self.gold_list = []
        self.silver_list = []
        self.bronze_list = []

        # blokk aniamciok
        dirt_img = pygame.image.load('../animation/dirt.png')
        grass_img = pygame.image.load('../animation/grass.png')
        gold_img = pygame.image.load('../animation/coinGold.png')
        silver_img = pygame.image.load('../animation/coinSilver.png')
        bronze_img = pygame.image.load('../animation/coinBronze.png')

#feldolgozza az arrayt ami a map infot tartalmazza
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    enemy = Enemy(col_count * tile_size, row_count * tile_size)
                    enemy_group.add(enemy)
                if tile == 4:
                    trap = Trap(col_count * tile_size, row_count * tile_size + tile_size // 2)
                    trap_group.add(trap)
                if tile == 5:
                    img = pygame.transform.scale(gold_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    gold = (img, img_rect)
                    self.gold_list.append(gold)
                if tile == 6:
                    lava = Lava(col_count * tile_size, row_count * tile_size + tile_size // 2)
                    lava_group.add(lava)
                if tile == 7:
                    img = pygame.transform.scale(silver_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    silver = (img, img_rect)
                    self.silver_list.append(silver)
                if tile == 8:
                    img = pygame.transform.scale(bronze_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    bronze = (img, img_rect)
                    self.bronze_list.append(bronze)

                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
        for gold in self.gold_list:
            screen.blit(gold[0], gold[1])
        for silver in self.silver_list:
            screen.blit(silver[0], silver[1])
        for bronze in self.bronze_list:
            screen.blit(bronze[0], bronze[1])


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('../animation/blockerMad.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1


class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('../animation/lava.png')
        self.image = pygame.transform.scale(img, (tile_size, tile_size*2 - 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Trap(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('../animation/spikes.png')
        self.image = pygame.transform.scale(img, (tile_size, tile_size*2 - 25))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# a map abrazolasa
world_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1],
    [1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 2, 2, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 7, 0, 5, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1],
    [1, 7, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 1],
    [1, 0, 2, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 8, 5, 0, 2, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 2, 2, 2, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

]

#peldanyositas az osztalyokbol
player = Player(100, screen_height)
enemy_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
trap_group = pygame.sprite.Group()

world = World(world_data)

#gombok létrehozása
start_button = Button(screen_width // 2 - 300, screen_height // 2, start_img)
exit_button = Button(screen_width // 2 + 100, screen_height // 2, exit_img)
highscore_button = Button(screen_width // 2 - 100, screen_height // 2 + 150, highscore_img)
restart_button = Button(screen_width // 2 - 50, screen_height // 2 + 100, restart_img)
font = pygame.font.SysFont('Comic Sans MS', 30)

start_time = 0
gold_copy = world.gold_list.copy()
silver_copy = world.silver_list.copy()
bronze_copy = world.bronze_list.copy()

run = True
while run:

    clock.tick(fps)
    screen.blit(bg_img, (0, 0))

    if main_manu == True:
        if start_button.draw() == True:
            start_time = pygame.time.get_ticks()
            main_manu = False
        if exit_button.draw() == True:
            run = False
        if highscore_button.draw() == True:
            pass
    else:
        world.draw()
        if game_over == 0:
            enemy_group.update()
            minutes = (pygame.time.get_ticks() - start_time) // 60000
            seconds = (pygame.time.get_ticks() - start_time) // 1000 % 60
            timer = font.render(str(minutes) + ':' + str(seconds), False, (0, 0, 0))

            for gold in world.gold_list:
                if gold[1].colliderect(player):
                    world.gold_list.remove(gold)
            for silver in world.silver_list:
                if silver[1].colliderect(player):
                    world.silver_list.remove(silver)
            for bronze in world.bronze_list:
                if bronze[1].colliderect(player):
                    world.bronze_list.remove(bronze)

        screen.blit(timer, (screen_width // 2 - 15, 45))
        lava_group.draw(screen)
        trap_group.draw(screen)
        enemy_group.draw(screen)
        game_over = player.update(game_over)

        if game_over == -1:
            if restart_button.draw():
                player.reset(100, screen_height)
                game_over = 0
                start_time = pygame.time.get_ticks()
                world.gold_list = gold_copy.copy()
                world.silver_list = silver_copy.copy()
                world.bronze_list = bronze_copy.copy()

        #draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
