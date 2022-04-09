from pygame import *
from random import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.size_x = size_x
        self.size_y = size_y
        self.image = transform.scale(image.load(player_image), (self.size_x, self.size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height:
            self.rect.y += self.speed

    def update(self):
        keys = key.get_pressed()
        if keys[K_DOWN] and self.rect.y < win_height:
            self.rect.y += self.speed
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed

win_width = 500
win_height = 400


racket = Player('unnamed.jpg', 30,200,30, 50, 3)
racket2 = Player('unnamed.jpg', 440,200,30, 50, 3)
ball = GameSprite('10.png', 200, 200, 50, 50, 4)
back = GameSprite('m.jpg', 0, 0, 400, 500, 0)
x = 0
font.init()
font = font.Font(None, 35)
los1 = font.render(f'player {x} lose', True, (180, 0, 0))


speed_x = 3
speed_y = 3

window = display.set_mode((win_width, win_height))
game = True
clock = time.Clock()
FPS = 60
fin = False
while game:
    # Прохождение в цикле по всем событиям
    for e in event.get():
        if e.type == QUIT:
            game = False
            break

    if fin != True:
        window.fill((0, 153, 0))
        racket.update2()
        racket2.update()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > 400 - ball.rect.height or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(ball, racket) or sprite.collide_rect(ball, racket2):
            speed_x *= -1

        if ball.rect.x > 500 - ball.rect.width:
            fin = True
            x = 1

        if ball.rect.x < 0:
            fin = True
            x = 2

        racket2.reset()
        racket.reset()
        ball.reset()

    if fin:
        los1 = font.render(f'player {x} lose', True, (180, 0, 0))
        window.blit(los1, (180, 200))
    display.update()
    clock.tick(FPS)