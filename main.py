#Imports y variables 
from pygame import *
from random import randint, random
win_width = 700
win_height = 500
game = True
clock= time.Clock()

FPS = 60
player_x = 150
player_y = 425
speed = 5.5
finish = False
run = True
lost = 0
img_enemy = 'ufo.png'
#Superclase y clases 
class GameSprite(sprite.Sprite):
    def __init__(self, playerimage, player_x, player_y, size_x, size_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(playerimage), (size_x,size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.zpeed = speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.zpeed
        if keys_pressed[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.zpeed
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.zpeed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - 267:
            self.rect.y += self.zpeed
    def shoot(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15)
        #bullets.add(bullet)
          
class Enemy(GameSprite): 
    def update(self):
        self.rect.y += self.zpeed   
        if self.rect.y >= win_height -200:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = -10
        global lost
        if self.rect.y >= win_height - 200:
            lost = lost + 1
        

class Bullet(GameSprite):
    def move(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_SPACE]:  
            mixer.init()
            mixer.music.load('fire.ogg')
            mixer.music.play()
            self.rect.y -= self.zpeed 
        
    def collision(self):
        pass

#Pantalla y musica
window = display.set_mode((win_width, win_height))
display.set_caption("Shooter")
glxy = transform.scale(
    image.load("galaxy.jpg"),
    (win_width, win_height)
    )

mixer.init()
mixer.music.load('Metalmania.mp3')
mixer.music.play()

#Creacion de personajes
p = Player("rocket.png", player_x, player_y, 70, 85, speed )
#n = Player("bullet.png", player_x, player_x, speed=0.1)

monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy(img_enemy, randint( 80, win_width - 80), -40 ,80, 50, randint(1,5))
    monsters.add(monster)
#Ciclo de juego
while game:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish :
        window.blit(glxy,(0, 0))
        
        p.update()
        monsters.update()

        monsters.draw(window)
        p.reset()

        font.init()
        font1 = font.Font(None, 36)

        text_lose = font1.render(
            "Fallados: " + str(lost), 1, (255, 255, 255)
        )

        display.update()
    clock.tick(FPS)
