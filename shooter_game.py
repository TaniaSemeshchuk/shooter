#Створи власний Шутер!

from pygame import *

mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')

img_back = "galaxy.jpg"
img_hero = "rocket.png"

win_width = 700
win_height = 500
display.set_caption('Шутер')
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

class GameSprite(sprite.Sprite):
    def __init__(self, player_img, player_x, player_y, size_x, 
                 size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_img), 
                                     (size_x, size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    

run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    window.blit(background, (0, 0))
    
    display.update()
    time.delay(60)




