from pygame import *
from random import randint
from time import sleep
# Классы
class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, player_speed,size_x,size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def move_r(self):
        keys = key.get_pressed() 
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y <window_w - 80:
            self.rect.y += self.speed
    def move_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <window_w - 80:
            self.rect.y += self.speed


fon = (200,150,180)

win_width = 700
win_height = 500
window = display.set_mode((win_width,win_height))
window.fill(fon)

game =True
finish = False
clock= time.Clock()
fps= 60

ball = GameSprite('moon.png',200,200,4,50,50)

while game:
    for e in event.get():
        if e.type == QUIT:
            game =False

    if finish != True:
        window.fill(fon)
        ball.reset()

    display.update()
    clock.tick(fps)