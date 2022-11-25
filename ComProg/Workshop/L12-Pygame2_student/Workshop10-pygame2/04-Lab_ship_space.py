import pygame as pg
import random
from os import path

img_dir = path.join('source\img')

# define screen resolution [width 480 , height 600 , FPS 60 ]
width = 480
height = 600
FPS = 60
# define colors
green = (20, 255, 140)
white = (255, 255, 255)
black = (0, 0, 0)
teal = (0, 128, 128)

# initialize pg and create window
pg.init()
screen = pg.display.set_mode((width, height))
pg.display.set_caption("ShipSpace!")
clock = pg.time.Clock()

# load game graphics
bg = pg.image.load(path.join(img_dir, "space.png")).convert()
bg_rect = bg.get_rect()
ship_img = pg.image.load(path.join(img_dir, "Ship.png")).convert()
meteor_img = pg.image.load(path.join(img_dir, "meteor_med.png")).convert()
bullet_img = pg.image.load(path.join(img_dir, "red_bullet.png")).convert()

#################################################################################################
# Class ที่เพิ่มเข้ามาใหม่ -> Ship , Meteor , Bullet ; Function ที่เพิ่มเข้ามาใหม่ -> newmeteor()

# Class ของผู้เล่นภายในมี method __init__ , update , shoot


class Ship(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(ship_img, (50, 38))
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.centerx = width / 2
        self.rect.bottom = height - 10
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT]:
            self.speedx = -8
        if keystate[pg.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.left < 0:
            self.rect.left = 0

        if keystate[pg.K_UP]:
            self.speedy = -8
        if keystate[pg.K_DOWN]:
            self.speedy = 8
        self.rect.y += self.speedy
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > height:
            self.rect.bottom = height

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top, 0, -1, 0)
        all_sprites.add(bullet)
        bullets.add(bullet)

    def ult(self):
        ults = []
        ults.append(Bullet(self.rect.centerx, self.rect.top, 0, -1, 0, 1))
        ults.append(Bullet(self.rect.left, self.rect.top, -1, -1, 45, 1))
        ults.append(Bullet(self.rect.left, self.rect.centery, -1, 0, 90, 1))
        ults.append(Bullet(self.rect.left, self.rect.bottom, -1, 1, 135, 1))
        ults.append(Bullet(self.rect.centerx, self.rect.bottom, 0, 1, 180, 1))
        ults.append(Bullet(self.rect.right, self.rect.bottom, 1, 1, 225, 1))
        ults.append(Bullet(self.rect.right, self.rect.centery, 1, 0, 270, 1))
        ults.append(Bullet(self.rect.right, self.rect.top, 1, -1, 315, 1))
        for bullet in ults:
            all_sprites.add(bullet)
            bullets.add(bullet)

# Class ของของหินภายในมี method __init__ , update


class Meteor(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = meteor_img
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > height + 10 or self.rect.left < -25 or self.rect.right > width + 20:
            self.rect.x = random.randrange(width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

# Class ของลูกกระสุนภายในมี method __init__ , update


class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y, dx, dy, deg, isUlt=0):
        pg.sprite.Sprite.__init__(self)
        self.image = bullet_img
        if isUlt == 1:
            self.image = ship_img
        self.image = pg.transform.rotate(self.image, deg)
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedx = dx * 10
        self.speedy = dy * 10

        #self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # ทำลายลูกกระสุนทิ้งถ้าลูกกระสุนออกจากหน้าจอ
        if self.rect.bottom < 0 or self.rect.top > height:
            self.kill()
        if self.rect.right < 0 or self.rect.left > width:
            self.kill()

# function ที่สร้างหินขึ้นมา 1 ก้อน


def newmeteor():
    m = Meteor()
    all_sprites.add(m)
    meteors.add(m)
#################################################################################################


d = list()

new_game = True

while True:

    # set ให้ตัวเกมส์แสดงผลด้วยความเร็วที่เหมาะสม
    clock.tick(FPS)

    if new_game:
        new_game = False

        #################################################################################################
        # TO DO 1-1 : สรา้ง sprite Group ให้กับ all_sprites, meteors, bullets, ship

        all_sprites = pg.sprite.Group()
        meteors = pg.sprite.Group()
        bullets = pg.sprite.Group()

        # TO DO 1-2 : สร้าง Object ให้กับ ship

        myShip = Ship()

        # TO DO 1-3 : เพิ่ม ship ลงใน all_sprites

        all_sprites.add(myShip)

        #################################################################################################
        # TO DO 2 : สร้าง Object Meteor ขึ้นมา 8 ก้อนโดยผ่านการเรียกใช้ฟังก์ชัน newmeteor()

        for i in range(8):
            newmeteor()

        #################################################################################################

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        #################################################################################################
        # TO DO 3 : ตรวจสอบว่าถ้ามีการกดปุ่ม spacebar (K_SPACE) ให้ ship เรียกฟังก์ชั่นสำหรับการยิงกระสุน

        if pg.key.get_pressed()[pg.K_SPACE]:
            myShip.shoot()

        #################################################################################################

        # Feature
        if pg.key.get_pressed()[pg.K_g]:
            myShip.ult()

    # Update
    all_sprites.update()

    #################################################################################################
    # TO DO 5 : ตรวจสอบว่าลูกกระสุนชนหินหรือไม่
    # ถ้าชนให้สร้างหินขึ้นมาใหม่เท่ากับจำนวนที่ถูกชนไป
    hits = pg.sprite.groupcollide(meteors, bullets, True, True)
    for i in range(len(hits)):
        newmeteor()

    #################################################################################################
    # TO DO 6 : ตรวจสอบว่าหินชนยานผู้เล่นหรือไม่
    # ถ้าชนให้เริ่มเกมใหม่
    hits = pg.sprite.spritecollide(myShip, meteors, True)

    if len(hits) > 0:
        new_game = True
        continue

    #################################################################################################
    # TO DO 4 : clear screen ด้วยสีดำ จากนั้น เอา bg ใส่ใน bg_rect
    screen.fill(black)
    screen.blit(bg, bg_rect)

    #################################################################################################
    # TO DO 7 : วาด element ใน all_sprites ลงใน screen
    all_sprites.draw(screen)
    d.append(all_sprites)

    #################################################################################################
    # after drawing everything, flip the display
    pg.display.flip()

pg.quit()
