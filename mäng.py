import pygame
import random
import time

pygame.init()

def erinevad_värvid(õige_värv):  #Genereerib neli erinevat värvi, millest 1 on õige  
    k = 0
    suvaline1 = [0, 0, 0]
    värvid4 = [0, 0, 0, 0]
    värvid4[random.randint(0,3)] = õige_värv
    for i in range(3):
        while True:
            suvaline1[i] = (((random.randint(0, 3)*85)), ((random.randint(0, 3)*85)), ((random.randint(0, 3)*85)))
            if suvaline1[i] in suvaline1[:i] or suvaline1[i] == (255, 255, 255) or suvaline1[i] in värvid: continue
            else: break
    for i in range(4):
        if värvid4[i] == õige_värv: 
            continue
        else:
            värvid4[i] = suvaline1[k]
            k += 1
    return värvid4
   
def värvi_valik(n):
    for i in range(n):
        värvid.append(0)
    for i in range(n):
        while True:
            värvid[i] = ((random.randint(0, 3)*85), (random.randint(0, 3)*85), (random.randint(0, 3)*85))
            if värvid[i] in värvid[:i] or värvid[i] == (255, 255, 255) or värvid[i] == 0: continue
            else: break
    return n
        
def valik(): #Genereerib 4 ruutu, millest tuleb valida õige
    lugeja = 0
    kastlai, kastpikk = laius // 2, pikkus // 2
    õige_värv = random.choice(värvid)
    värvid4 = erinevad_värvid(õige_värv) 
        
    while lugeja < 10:
        time.sleep(0.01)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                #Võtab konkreetse kasti õige värvi peale, et kontrollida, kas hiirevajutus oli õige kasti sees
                kast11 = pygame.Surface((kastlai, kastpikk)).get_rect()
                for i in range(4):
                    if värvid4[i] == õige_värv:
                        if i == 0: kast11.topleft = (0, 0)
                        elif i == 1: kast11.bottomleft = (0, pikkus)
                        elif i == 2: kast11.topright = (laius, 0)
                        elif i == 3: kast11.bottomright = (laius, pikkus) 
                
                pos = pygame.mouse.get_pos()
                if kast11.collidepoint(pos): lugeja += 1
                else: lugeja -= 1  
                
                õige_värv = random.choice(värvid)
                värvid4 = erinevad_värvid(õige_värv)
                
        #Joonistab kastid
        kast1 = (0, 0, kastlai, kastpikk)
        kast2 = (0, pikkus // 2, kastlai, kastpikk)
        kast3 = (laius // 2, 0, kastlai, kastpikk)
        kast4 = (laius // 2, pikkus // 2, kastlai, kastpikk)
        kastid = [kast1, kast2, kast3, kast4]
        for i in range(4):
            pygame.draw.rect(ekraan, värvid4[i], kastid[i])               
        
        #Loendur
        font = pygame.font.Font(None, 80)
        tekst = font.render(str(lugeja), True, (0, 0, 0), (0, 255, 0))
        tekstikast = tekst.get_rect() 
        tekstikast.center = (laius // 2, 20)
        ekraan.blit(tekst, tekstikast)
        
        pygame.display.update()

numbritaustad  = [None, None, None, None]
numbrikastid = []
sõnataust = (181, 181, 181)
sõnataust1 = (181, 181, 181)
põhivärv = (255, 255, 255)
laius = 800
pikkus = 600
a = 0
sisu = "Start"
fontisuurus = 64
leht = 0
värvid = []

ekraan = pygame.display.set_mode((laius, pikkus))
pygame.display.set_caption("Reaktsioonimäng")
                    
while True:
    time.sleep(0.01)
    ekraan.fill(põhivärv)
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if tekstikast.collidepoint(pos) and sisu == "Start":
                sisu = "Vali mitu erinevat värvi soovid meelde jätta"
                fontisuurus  = 40
            if tekstikast1.collidepoint(pos):
                if leht == 0:
                    sisu = "Ekraanile tuleb 4 värvi. Ainult 1 on õige ning selle valimisel +1 punkti."
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
            for i in range(4):
                try:
                    if numbrikastid[i].collidepoint(pos):
                        a = värvi_valik(i+1)
                        sisu = "Jäta meelde see värv"
                        fontisuurus = 64
                except: continue
    
    #Esimene tekstikast                
    font = pygame.font.Font(None, fontisuurus)
    tekst = font.render(sisu, True, (0, 0, 0), sõnataust)
    tekstikast = tekst.get_rect() 
    tekstikast.center = (laius // 2, pikkus // 2)
    
    #Joonistab esimese tekstikasti
    ekraan.blit(tekst, tekstikast)
    
    #Teine tekstikast
    font1 = pygame.font.Font(None, 64)
    tekst1 = font1.render("Jätka", True, (0, 0, 0), sõnataust1)
    tekstikast1 = tekst1.get_rect()
    tekstikast1.center = (laius // 2, 540)
                        
    #sõnakastivärv
    pos = pygame.mouse.get_pos()
    if tekstikast.collidepoint(pos) and sisu == "Start":
        sõnataust = (181, 181, 181)
    else:
        sõnataust = None
    if tekstikast1.collidepoint(pos):
        sõnataust1 = (181, 181, 181)
    else:
        sõnataust1 = None
    
    if sisu == "Jäta meelde see värv":
        ekraan.blit(tekst1, tekstikast1) #Joonistab "jätka" tekstikasti
        
        värviasukohad = [(laius//4-75, pikkus//4-75, 150, 150), (laius//4*3-75, pikkus//4-75, 150, 150), (laius//4-75, pikkus//4*3-75, 150, 150), (laius//4*3-75, pikkus//4*3-75, 150, 150)]
        for i in range(a):
            pygame.draw.rect(ekraan, värvid[i], (värviasukohad[i]))
    
    elif sisu == "Ekraanile tuleb 4 värvi. Ainult 1 on õige ning selle valimisel +1 punkti." or sisu == "Sa võitsid!":
        ekraan.blit(tekst1, tekstikast1) #Joonistab "jätka" tekstikasti
        
    elif sisu == "Vali mitu erinevat värvi soovid meelde jätta":
        font = pygame.font.Font(None, 100)
        numbriasukohad = [(laius//4, pikkus//4), (laius//4*3, pikkus//4), (laius//4, pikkus//4*3), (laius//4*3, pikkus//4*3)]
        
        for i in range(4):
            number = font.render(str(i+1), True, (0, 0, 0), numbritaustad[i])
            numbrikast = number.get_rect()
            numbrikast.center = (numbriasukohad[i])
            numbrikastid.append(numbrikast) 
            ekraan.blit(number, numbrikast)
        
        for i in range(4):
            if numbrikastid[i].collidepoint(pos):
                numbritaustad[i] = (181, 181, 181)
            else:
                numbritaustad[i] = None    
            
    pygame.display.update()