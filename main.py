import pygame 


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
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False






    pygame.display.update()






















