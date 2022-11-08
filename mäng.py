import pygame
import random

pygame.init()

põhivärv = (255, 255, 255)
laius = 800
pikkus = 600

ekraan = pygame.display.set_mode((laius, pikkus))
pygame.display.set_caption("Reaktsioonimäng")

sisu = "Start"
fontisuurus = 64
leht = 0

värvid = [0, 0, 0]
for i in range(3):
    
    while True:
        värvid[i] = ((random.randint(0, 3)*85)), (random.randint(0, 3)*85), ((random.randint(0, 3)*85))
        if värvid[i] in värvid[:i] or värvid[i] == (255, 255, 255): continue
        else: break

def valik():
    
    suvaline1 = [0, 0, 0]
    värvid4 = [0, 0, 0, 0]
    lugeja = 0
    kastlai, kastpikk = laius // 2, pikkus // 2
    while lugeja < 10:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                kast11 =  pygame.Surface((kastlai, kastpikk)).get_rect()
                kast11.bottomleft = (0, pikkus)
                õige_värv = random.choice(värvid)
                värvid4[random.randint(0,3)] = õige_värv
                k = 0 
                for i in range(3):
                    while True:
                        suvaline1[i] = ((random.randint(0, 3)*85)), (random.randint(0, 3)*85), ((random.randint(0, 3)*85))
                        if suvaline1[i] in suvaline1[:i] or suvaline1[i] == (255, 255, 255) or suvaline1[i] in värvid: continue
                        else: break
                        
                    
                for i in range(4):
                    if värvid4[i] == õige_värv:
                        continue
                    else:
                        värvid4[i] = suvaline1[k]
                        k += 1
                
                if kast11.collidepoint(pos): 
                            lugeja += 1  
                
                    
        

        kast1 = (0, 0, kastlai, kastpikk)
        kast2 = (0, pikkus // 2, kastlai, kastpikk)
        kast3 = (laius // 2, 0, kastlai, kastpikk)
        kast4 = (laius // 2, pikkus // 2, kastlai, kastpikk)

        
        

        pygame.draw.rect(ekraan, värvid4[0], kast1)
        pygame.draw.rect(ekraan, värvid4[1], kast2)
        pygame.draw.rect(ekraan, värvid4[2], kast3)
        pygame.draw.rect(ekraan, värvid4[3], kast4)
        
        pygame.display.update()


    
    
while True:
    ekraan.fill(põhivärv)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if tekstikast.collidepoint(pos):
                sisu = "Jäta meelde need kolm värvi"
            if tekstikast1.collidepoint(pos):
                if leht == 0:
                    sisu = "Ekraanile tuleb 4 värvi. Ainult 1 on õige ning selle valimisel +1 punkti. Vale korral -1 punkti"
                    fontisuurus = 25
                    leht += 1
                elif leht == 1:
                    valik()
                    sisu = "Sa võitsid!"
                    fontisuurus = 64
                    leht += 1
                elif leht == 2:
                    sisu = "Start"
                    leht = 0
                    
    font = pygame.font.Font(None, fontisuurus)
    tekst = font.render(sisu, True, (0, 0, 0), (0, 255, 0))
    tekstikast = tekst.get_rect() 
    tekstikast.center = (laius // 2, pikkus // 2)
    
    ekraan.blit(tekst, tekstikast)
    
    tekst1 = font.render("Jätka", True, (0, 0, 0), (0, 255, 0))
    tekstikast1 = tekst1.get_rect()
    tekstikast1.center = (laius // 2, 540)
    
    if sisu == "Jäta meelde need kolm värvi":
        pygame.draw.rect(ekraan, värvid[0], (150, 110, 150, 150))
        pygame.draw.rect(ekraan, värvid[1], (500, 110, 150, 150))
        pygame.draw.rect(ekraan, värvid[2], (325, 340, 150, 150))
        ekraan.blit(tekst1, tekstikast1)
    
    if sisu == "Ekraanile tuleb 4 värvi. Ainult 1 on õige ning selle valimisel +1 punkti. Vale korral -1 punkti" or "Sa võitsid!":
        ekraan.blit(tekst1, tekstikast1)
                
    pygame.display.update()