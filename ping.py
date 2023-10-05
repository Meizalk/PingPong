from pygame import *

clock = time.Clock()

back = (200,255,255)
display.set_caption('Пинг-понг')
win_width = 700
win_height = 500
win = display.set_mode((win_width,win_height))
win.fill(back)




class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        win.blit(self.image,(self.rect.x, self.rect.y))




class Player(GameSprite):
    def update_right(self):
        key_pressed = key.get_pressed()

        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if key_pressed[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


    def update_left(self):
        key_pressed = key.get_pressed()

        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if key_pressed[K_s] and self.rect.y < 520:
            self.rect.y += self.speed



racket_1 = Player('raketka_1.png',30,200,4,50,5)
racket_2 = Player('raketka_2.png',520,200,4,50,5)
ball = GameSprite('ball.png',200,200,4,50,100)


font.init()
font = font.Font(None,35)
lose1 = font.render('PLAYER 1 LOSE!',True,(180,0,0))
lose2 = font.render('PLAYER 2 LOSE!',True,(180,0,0))


speed_x = 1
speed_y = 1



game = True
finish = False

FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        win.fill(back)
        racket_1.update_left()
        racket_2.update_right()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket_1,ball) or sprite.collide_rect(racket_2,ball):
            speed_x *= -1
            speed_y *= 1

        
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            win.blit(lose1,(200,200))
            game_over = True

        if ball.rect.x > win_width:
            finish = True
            win.blit(lose2,(200,200))
            game_over = True


        racket_1.reset()
        racket_2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)