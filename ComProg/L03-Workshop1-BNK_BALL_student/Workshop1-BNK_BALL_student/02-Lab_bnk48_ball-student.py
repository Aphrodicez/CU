# Lab_BNK48 
from operator import ne
import pygame as pg

# TODO 1 : กำหนด width : 1000 , height : 600 และ FPS : 60
width = 1000
height = 600
FPS = 60

# TODO 2 : กำหนดค่าสีดังนี้ pink : (197,142,195) , white : (255,255,255)
pink = (197, 142, 195)
white = (255, 255, 255)

# TODO 3 : กำหนดความเร็วให้กับ member แต่ละคน [ 3 member ]

ball_speed = [[0]] * 4
ball_speed[1] = [2 * 1,2 * 1]
ball_speed[2] = [-3 * 1, 4 * 1]
ball_speed[3] = [3 * 1,-2 * 1]

# TODO 4 : initialize pygame variable and create clock
pg.init()
clock = pg.time.Clock()
running = True

# TODO 5 : create screen [pygame.display.set_mode] 
# and set caption [pygame.display.set_caption] => "BNK_BALL (Heavy Collision)"
screen = pg.display.set_mode((width, height))
pg.display.set_caption("BNK_BALL (Heavy Collision)")

# TODO 6
#Load sound [change your sound filepath according to your computer]
pg.mixer.init()
pg.mixer.music.load("source/sound.mp3")
pg.mixer.music.play(-1, 0.0)

# ใช้คำสั่ง soundeffect.play() เพื่อเล่นเสียง effect ตอนลูกบอลชนกัน
soundeffect = pg.mixer.Sound("source/effect.wav")

# Choose 3 members from BNK48 and create pygame object from  get_rect
# [ load , resize , get_rect ]

ball_rect = [0] * 4

# Member 1 [size : (150 , 150) , center : (500 , 250) ]
ball1_img = pg.image.load("source/BNK48/Orn_cc.png").convert_alpha()
ball1_img = pg.transform.scale(ball1_img, (150, 150))
ball_rect[1] = ball1_img.get_rect(center = (500, 250))

# TODO 7 : create object with attribute in each comment
# Member 2 [size : (100 , 100) , center : (250 , 120)]

ball2_img = pg.image.load("source/BNK48/Cherprang_cc.png").convert_alpha()
ball2_img = pg.transform.scale(ball2_img, (100, 100))
ball_rect[2] = ball2_img.get_rect(center = (250 , 120))

# Member 3 [size : (120 , 120) , center : (800 , 400)]

ball3_img = pg.image.load("source/BNK48/Phukkhom_cc.png").convert_alpha()
ball3_img = pg.transform.scale(ball3_img, (120 , 120))
ball_rect[3] = ball3_img.get_rect(center = (800 , 400))

def dis(x1, y1, x2, y2):
    val = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5
    return val

while running:
    # TODO 8 : set ให้ตัวเกมส์แสดงผลด้วยความเร็วที่เหมาะสม [clock.tick(...)]
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running=False
            pg.quit()

    if running:
        # TODO 9 :ใส่สี background สีชมพู (screen.fill(...))
        screen.fill(pink)

        # TODO 10 : ให้ member ทั้ง 3 คนเคลื่อนที่ตามทิศทางและความเร็วเป็นไปตาม speed ของแต่ละคน
        ball_rect[1] = ball_rect[1].move(ball_speed[1])
        ball_rect[2] = ball_rect[2].move(ball_speed[2])
        ball_rect[3] = ball_rect[3].move(ball_speed[3])
        
        # TODO 11 : วาด text คำว่า "Heavy Collision" [size : 150 , center :(width/2 , height/3), สีขาว]
        font_name = pg.font.match_font('arial')  # กำหนดชื่อ Font
        font = pg.font.Font(font_name, 150)  # กำหนดขนาด font
        text_surface = font.render("Heavy Collision", True, white) # กำหนด Text และ สี
        text_rect = text_surface.get_rect() # แปลง Surface เป็น object
        text_rect.midtop = (width / 2, height / 3) # ระบุตำแหน่งของ text
        screen.blit(text_surface, text_rect) # เอา Text ใส่ลงใน object ของ Text นั้น

        
        # TODO 12 : วาด text รหัสนิสิต ลงไป ข้างใต้คำว่า "Heavy Collision" [size : 100 ,center :(width/2 , height/1.5), สีขาว]
        # [ขนาดและตำแหน่งสามารถปรับได้ตามความเหมาะสม]
        font_name = pg.font.match_font('arial')  # กำหนดชื่อ Font
        font = pg.font.Font(font_name, 100)  # กำหนดขนาด font
        text_surface = font.render("6532035021", True, white) # กำหนด Text และ สี
        text_rect = text_surface.get_rect() # แปลง Surface เป็น object
        text_rect.midtop = (width / 2, height / 1.5) # ระบุตำแหน่งของ text
        screen.blit(text_surface, text_rect) # เอา Text ใส่ลงใน object ของ Text นั้น

        # TODO 13 : เขียนเงื่อนไขไม่ให้ตกกรอบทุกด้านให้กับ member ทั้ง 3 คน
        if ball_rect[1].left < 0 or ball_rect[1].right > width:
            ball_speed[1][0] = -ball_speed[1][0]
        if ball_rect[1].top < 0 or ball_rect[1].bottom > height:
            ball_speed[1][1] = -ball_speed[1][1]

        if ball_rect[2].left < 0 or ball_rect[2].right > width:
            ball_speed[2][0] = -ball_speed[2][0]
        if ball_rect[2].top < 0 or ball_rect[2].bottom > height:
            ball_speed[2][1] = -ball_speed[2][1]

        if ball_rect[3].left < 0 or ball_rect[3].right > width:
            ball_speed[3][0] = -ball_speed[3][0]
        if ball_rect[3].top < 0 or ball_rect[3].bottom > height:
            ball_speed[3][1] = -ball_speed[3][1]      
        
        # Special point ทำให้ลูกบอลชนกันแล้วเด้งในทิศตรงกันข้าม

        for i in range(1, len(ball_rect)):
            for j in range(i + 1, len(ball_rect)):
                d = dis(ball_rect[i].centerx, ball_rect[i].centery, ball_rect[j].centerx, ball_rect[j].centery)
                r = (ball_rect[i].width + ball_rect[j].width) / 2
                next_speed = ball_speed
                if d <= r:
                    soundeffect.play()
                    for k in range(2):
                        next_speed[i][k] = -ball_speed[i][k]
                        next_speed[j][k] = -ball_speed[j][k]
                    ball_speed = next_speed

        ################################################

        # TODO 14 : เอาภาพของ member แต่ละคนใส่ลงใน object ของตนเอง
        screen.blit(ball1_img, ball_rect[1])
        screen.blit(ball2_img, ball_rect[2])
        screen.blit(ball3_img, ball_rect[3])

        ##########################################################
        
        pg.display.flip()

