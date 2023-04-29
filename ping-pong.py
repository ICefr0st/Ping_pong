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
        if keys[K_DOWN] and self.rect.y <window_h - 110:
            self.rect.y += self.speed
    def move_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <window_h - 110:
            self.rect.y += self.speed

def point_l():
      
    if ball.rect.x < 0:
        left_poitn global 
        left_poitn += 1


fon = (200,150,180)


window_w = 700
window_h = 500
window = display.set_mode((window_w,window_h))
window.fill(fon)

game =True
finish = False
clock= time.Clock()
fps= 80

left_poitn =0
right_point = 0

ball = GameSprite('moon.png',200,200,4,50,50)
player_l = Player('player.png',0,200,5,20,120)
player_r = Player('player.png',680,200,5,20,120)
font.init()
font1 = font.Font(None,40)
font2 = font.Font(None,80)
losel = font1.render('LEFT player LOSE!',True, (180,0,0)) 
loser = font1.render('RIGHT player LOSE!',True,(145,42,4)) 
point = font2.render(str(left_poitn)+' : '+str(right_point),True,(255,255,255))
speed_x = 3
speed_y = 3



while game:
    for e in event.get():
        if e.type == QUIT:
            game =False

    if finish != True:
        window.fill(fon)
        
        player_l.move_l()
        player_r.move_r()

        ball.rect.x += speed_x
        ball.rect.y += speed_y
        ball.reset()
        if sprite.collide_rect(player_l,ball) or sprite.collide_rect(player_r,ball):
            speed_x *= -1
            speed_y *= 1
           
        if ball.rect.y > window_h-50 or ball.rect.y <0:
            speed_y *= -1

        point_l()
            
        player_r.reset()
        player_l.reset()
        window.blit(point,(300,0))
    display.update()
    clock.tick(fps)