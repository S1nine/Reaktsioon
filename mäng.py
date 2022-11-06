import os
import pygame
import random

path = os.path.dirname(__file__)

pygame.init()

põhivärv = (255, 255, 255)
laius = 800
pikkus = 600

ekraan = pygame.display.set_mode((laius, pikkus))
pygame.display.set_caption("Reaktsioonimäng")

sisu = "Start"
font = pygame.font.Font(None, 64)

värvid = [0, 0, 0]
for i in range(3):
    while True:
        värvid[i] = ((random.randint(0, 5)*51)), (random.randint(0, 5)*51), ((random.randint(0, 5)*51))
        if värvid[i] in värvid[:i] and värvid[i] != (0, 0, 0): continue
        else: break

print(värvid)

def teineleht():
        pygame.draw.rect(ekraan, värvid[0], (150, 110, 150, 150))
        pygame.draw.rect(ekraan, värvid[1], (500, 110, 150, 150))
        pygame.draw.rect(ekraan, värvid[2], (325, 340, 150, 150))

while True:
    ekraan.fill(põhivärv)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    tekst = font.render(sisu, True, (0, 0, 0), (0, 255, 0))
    tekstikast = tekst.get_rect() 
    tekstikast.center = (laius // 2, pikkus // 2)
    
    ekraan.blit(tekst, tekstikast)
    
    if sisu == "Jäta meelde need kolm värvi":
        teineleht()
        tekst1 = font.render("Jätka", True, (0, 0, 0), (0, 255, 0))
        tekstikast1 = tekst1.get_rect()
        tekstikast1.center = (laius // 2, 540)
        ekraan.blit(tekst1, tekstikast1)
                
    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        if tekstikast.collidepoint(pos):
            sisu = "Jäta meelde need kolm värvi"
            
    pygame.display.update()