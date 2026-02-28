import pygame 
pygame.init()

WIDTH=600
HEIGHT=600
TITLE="PAQUETA CRISPS"

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("PAQUETA CRISPS")
run=True

bg1=pygame.image.load(r"birthdayanimation\cake.jpg")
bg2=pygame.image.load(r"birthdayanimation\candles.jpg")
bg3=pygame.image.load(r"birthdayanimation\balloons.jpg")

while run==True:
    screen.blit(bg1,(0,0))
    font=pygame.font.SysFont("arial",50)
    text=font.render("happy bday, i hope u have a goodday ", True,"green")
    screen.blit(text,(300,300))
    pygame.display.update()
    pygame.time.delay(7000)
    screen.blit(bg2,(0,0))
    font=pygame.font.SysFont("arial",50)
    bg2t=font.render("make a wish",True,"black")
    screen.blit(bg2t,(300,350))
    pygame.display.update()
    pygame.time.delay(7000)
    screen.blit(bg3,(0,0))
    font=pygame.font.SysFont("arial",50)
    bg3t=font.render(" yay",True,"yellow")
    screen.blit(bg3t,(200,350))
    pygame.display.update()
    pygame.time.delay(7000)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False






    pygame.display.update()






















