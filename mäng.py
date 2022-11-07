# Vajalike moodulite importimine
import pygame
import random

# Kõigi imporditud pygame moodulite tööle panemine

pygame.init()

# Tausta defineerimine

põhivärv = (255, 255, 255)
laius = 800
pikkus = 600

ekraan = pygame.display.set_mode((laius, pikkus))

# Algse sisu kirjutamine ekraanile

pygame.display.set_caption("Reaktsioonimäng")

sisu = "Start"
fontisuurus = 64

# Värvide defineerimine ja genereerimine

värvid = [0, 0, 0]
for i in range(3):
    while True:
        värvid[i] = ((random.randint(0, 5)*51)), (random.randint(0, 5)*51), ((random.randint(0, 5)*51))
        if värvid[i] in värvid[:i] and värvid[i] != (0, 0, 0): continue
        else: break

# Järgmine vaheleht, genereeritud värvidega

def teineleht():
        pygame.draw.rect(ekraan, värvid[0], (150, 110, 150, 150))
        pygame.draw.rect(ekraan, värvid[1], (500, 110, 150, 150))
        pygame.draw.rect(ekraan, värvid[2], (325, 340, 150, 150))

# Lõpmatu tsükkel, mis lõppeb tingimuslause täitumisel

while True:

    # Tausta täitmine eelnevalt defineeritud värviga

    ekraan.fill(põhivärv)
    
    # Tingimuslause, mis võimaldab pygame sulgeda

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    # Tsüklisisene fondi defineerimine ja tekstikasti defineerimine

    font = pygame.font.Font(None, fontisuurus)
    tekst = font.render(sisu, True, (0, 0, 0), (0, 255, 0))
    tekstikast = tekst.get_rect() 
    tekstikast.center = (laius // 2, pikkus // 2)
    
    # Teksti kirjutamine tekstikasti peale

    ekraan.blit(tekst, tekstikast)
    
    # Uue kasti tekitamine

    tekst1 = font.render("Jätka", True, (0, 0, 0), (0, 255, 0))
    tekstikast1 = tekst1.get_rect()
    tekstikast1.center = (laius // 2, 540)
    
    # Tingimuslause, mis rakendub kuvab ekraanile "Jätka", kui sisu võrdub alloleva lausega ning liigub edasi teisele lehele

    if sisu == "Jäta meelde need kolm värvi":
        teineleht()
        ekraan.blit(tekst1, tekstikast1)
    
    # //, kuid ei liigu uuele lehele

    if sisu == "Ekraanile tuleb 4 värvi. Ainult 1 on õige ning selle valimisel +1 punkti. Vale korral -1 punkti":
        ekraan.blit(tekst1, tekstikast1)
        
    # Defineerib ära, et kui hiirel vajutatakse vasakut nuppu, siis võtab hiire asukoha ning kui see asub asukohal tekstikast või tekstikast1, siis võtab selle asukoha ning salvestab sisu uueks väärtuseks uue sisu
    
    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        if tekstikast.collidepoint(pos):
            sisu = "Jäta meelde need kolm värvi"
        if tekstikast1.collidepoint(pos):
            sisu = "Ekraanile tuleb 4 värvi. Ainult 1 on õige ning selle valimisel +1 punkti. Vale korral -1 punkti"
            fontisuurus = 25
            
    # Uuendab ekraanil olevat
    
    pygame.display.update()