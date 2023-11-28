import pygame, sys
from pygame import mixer
import random

mixer.init()
pygame.init()

#wlasciwosci ekranu
WIDTH = 800
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bulls&Cows")
bg = pygame.image.load('texture/door.jpg')
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
icon = pygame.image.load("texture/ico_game.png")
pygame.display.set_icon(icon)

#wlasciwosci gry
bulls = 0
cows = 0
place_in_code = 0
win_temp = 0

#wczytaj muzyke i dzwieki
pygame.mixer.music.load("music/soundtrack.mp3")
pygame.mixer.music.set_volume(0.25)
pygame.mixer.music.play()
click_sound = pygame.mixer.Sound("music/click.mp3")
check_sound = pygame.mixer.Sound("music/waterdrop.mp3")
error_sound = pygame.mixer.Sound("music/error.mp3")
win_sound = pygame.mixer.Sound("music/win_sound.mp3")

code_no_random = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(code_no_random)
code = [None, None, None, None]
for i in range(0,4):
    code[i] = code_no_random[i]
code2 = [None, None, None, None]

#statystyki
c_rect = (15,17,66)
c_x = 10
c_y = 10
c_w_rect = 70
c_h_rect = 40

bulls_rect_score = (0, 0, 0)
b_x = 85
b_y = 10
b_w_rect = 15
b_h_rect = 15

bulls_rect_texture = (255, 255, 255)
b_x_texture = 105
b_y_texture = 10
b_w_rect_texture = 15
b_h_rect_texture = 15

cows_rect_score = (0, 0, 0)
co_x = 85
co_y = 35
co_w_rect = 15
co_h_rect = 15

cows_rect_texture = (255, 255, 255)
co_x_texture = 105
co_y_texture = 35
co_w_rect_texture = 15
co_h_rect_texture = 15

#tekstury
bulls_texture = pygame.image.load("texture/rocket.png").convert_alpha()
bulls_texture = pygame.transform.scale(bulls_texture, (15, 15))
cows_texture = pygame.image.load("texture/ufo.png").convert_alpha()
cows_texture = pygame.transform.scale(cows_texture, (15, 15))
on_speaker = pygame.image.load("texture/speaker.png").convert_alpha()
on_speaker = pygame.transform.scale(on_speaker, (70, 70))
off_speaker = pygame.image.load("texture/speaker1.png").convert_alpha()
off_speaker = pygame.transform.scale(off_speaker, (70, 70))

#czcionki
font = pygame.font.Font("font/chinese_rock.ttf", 30)
font2 = pygame.font.Font("font/LiquidCrystal.otf", 60)
font3 = pygame.font.Font("font/LiquidCrystal.otf", 20)
font4 = pygame.font.Font("font/LiquidCrystal.otf", 15)

#licznik wygranych
win_score = pygame.Rect(600,10,90,40)

#przyciski
buttonCHECK = pygame.Rect(380,500,90,40)
surf = font.render('CHECK', True, 'white')

promien_kola = 50
button1 = pygame.Rect(200, 250, promien_kola * 2, promien_kola * 2)
button2 = pygame.Rect(320, 250, promien_kola * 2, promien_kola * 2)
button3 = pygame.Rect(440, 250, promien_kola * 2, promien_kola * 2)
button4 = pygame.Rect(560, 250, promien_kola * 2, promien_kola * 2)

button1_click = 0
button2_click = 0
button3_click = 0
button4_click = 0
clicked = False

#wlaczanie i wylaczanie muzyki
mute = False 

on = SCREEN.blit(on_speaker, (720, 510))
off = SCREEN.blit(off_speaker, (720, 510))
#petla gry
root = True
while True:
    if root == True:
        SCREEN.blit(bg, (0,0))
        root = False
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #wyciszanie i właczanie muzyki    
        if mute == False:
            SCREEN.blit(on_speaker, (720, 510))
        else:
            SCREEN.blit(off_speaker, (720, 510))
        if events.type == pygame.MOUSEBUTTONDOWN:
            if on.collidepoint(events.pos) and mute == False:
                pygame.mixer.music.stop()
                mute=True
            elif off.collidepoint(events.pos) and mute == True:
                pygame.mixer.music.play()
                mute=False
        if events.type == pygame.MOUSEBUTTONDOWN:
            if buttonCHECK.collidepoint(events.pos):
                #cała mechanika gry (liczby nie moga sie powtarzac, wyswietlanie liczb na ekranie, sprawdzanie ilosci krow i bykow)
                if button1_click != button2_click and button1_click != button3_click and button1_click != button4_click and button2_click != button3_click and button2_click != button4_click and button3_click != button4_click:              
                    check_sound.play()
                    code2[0] = button1_click
                    code2[1] = button2_click
                    code2[2] = button3_click                                                                       
                    code2[3] = button4_click
                    for i, element1 in enumerate(code):
                        for j, element2 in enumerate(code2):
                            if element1 == element2:
                                if i == j:
                                    bulls += 1
                                else:
                                    cows += 1
                                break    
                    # print("byki: ", bulls)   
                    # print("krowy: ", cows)
                    if bulls == 4:
                        #wyswietlanie ilosci wygranych
                        win_temp += 1
                        random.shuffle(code_no_random)
                        for i in range(0,4):
                            code[i] = code_no_random[i]

                        win_sound.play()
                        SCREEN.blit(bg, (0,0))
                        info_score = font.render(f'win score: {win_temp}', True, 'white')
                        pygame.draw.rect(SCREEN,(0,0,0),win_score, border_radius = 20)
                        SCREEN.blit(info_score,(win_score.x+12, win_score.y+2))
                        
                        #aktulizacja historii
                        c_x = 10
                        c_y = 10
                        c_w_rect = 70
                        c_h_rect = 40

                        b_x = 85
                        b_y = 10
                        b_w_rect = 15
                        b_h_rect = 15

                        b_x_texture = 105
                        b_y_texture = 10
                        b_w_rect_texture = 15
                        b_h_rect_texture = 15

                        co_x = 85
                        co_y = 35
                        co_w_rect = 15
                        co_h_rect = 15

                        co_x_texture = 105
                        co_y_texture = 35
                        co_w_rect_texture = 15
                        co_h_rect_texture = 15
                       
                            

                    #history_bulls = pygame.draw.rect(SCREEN, bulls_rect_score, (b_x, b_y, b_w_rect, b_h_rect))
                    #pygame.draw.rect(SCREEN, bulls_rect_texture, (b_x_texture, b_y_texture, b_w_rect_texture, b_h_rect_texture))
                    if bulls != 4:
                        bulls_con = str(bulls) 
                        bulls_rect = font4.render(bulls_con, True, (255, 255, 255))
                        SCREEN.blit(bulls_rect, (b_x+4, b_y))
                        SCREEN.blit(bulls_texture, (b_x_texture, b_y_texture))
                        
                        #pygame.draw.rect(SCREEN, cows_rect_texture, (co_x_texture, co_y_texture, co_w_rect_texture, co_h_rect_texture))
                        #history_cows = pygame.draw.rect(SCREEN, cows_rect_score, (co_x, co_y, co_w_rect, co_h_rect))
                        cows_con = str(cows) 
                        cows_rect = font4.render(cows_con, True, (255, 255, 255))
                        SCREEN.blit(cows_rect, (co_x+4, co_y))
                        SCREEN.blit(cows_texture, (co_x_texture, co_y_texture))

                        code2_con = " ".join(map(str, code2)) 
                        code2_rect = font3.render(code2_con, True, (255, 255, 255))
                        history = pygame.draw.rect(SCREEN, c_rect, (c_x, c_y, c_w_rect, c_h_rect), border_radius = 10)
                    
                        
                        #aktualizacja miejsca wsywietalnia poprzednich prob
                        c_y = c_y + c_h_rect + 10  
                        b_y = b_y + c_h_rect + 10
                        co_y = co_y + c_h_rect + 10
                        b_y_texture = b_y_texture + c_h_rect + 10
                        co_y_texture = co_y_texture + c_h_rect + 10
                        
                        SCREEN.blit(code2_rect, (history.x+5 , history.y+8 ))
                else:
                    #komunikat o złym wprowadxzeniu kodu
                    error_sound.play()
                    pygame.time.delay(500)
                bulls = 0
                cows = 0
                    

    #przycisk sprawdzania (zmiana wygladu przycisku po najechaniu)
    a,b = pygame.mouse.get_pos()
    if buttonCHECK.x <= a <= buttonCHECK.x + 100 and buttonCHECK.y <= b <= buttonCHECK.y + 40:
        pygame.draw.rect(SCREEN,(88,89,132),buttonCHECK, border_radius = 20)
    else:
        pygame.draw.rect(SCREEN, (47,48,102),buttonCHECK, border_radius = 20)
    SCREEN.blit(surf,(buttonCHECK.x+12, buttonCHECK.y+2))
    
    #przycisk 1 liczby w kodzie (zmiana wygladu przycisku po najechaniu i mozliwosc wyboru liczby 1-9)
    if button1.x <= a <= button1.x + 100 and button1.y <= b <= button1.y + 100:
        pygame.draw.circle(SCREEN, (24,26,86), button1.center, promien_kola)
    else:
        pygame.draw.circle(SCREEN, (15,17,66), button1.center, promien_kola)
    
    surf1 = font2.render(f'{button1_click}', True, (255, 255, 255))    
    SCREEN.blit(surf1,(button1.x+35, button1.y+20)) 
    
    if events.type == pygame.MOUSEBUTTONDOWN and clicked == False:
        if button1.collidepoint(events.pos):
            click_sound.play()        
            button1_click = button1_click + 1
            clicked = True
    if events.type == pygame.MOUSEBUTTONUP:
        clicked = False
    if button1_click == 10:
        button1_click = 0

    #przycisk 2 liczby w kodzie (zmiana wygladu przycisku po najechaniu i mozliwosc wyboru liczby 1-9)
    if button2.x <= a <= button2.x + 100 and button2.y <= b <= button2.y + 100:
        pygame.draw.circle(SCREEN, (24,26,86), button2.center, promien_kola)
    else:
        pygame.draw.circle(SCREEN, (15,17,66), button2.center, promien_kola)

    surf2 = font2.render(f'{button2_click}', True, (255, 255, 255))    
    SCREEN.blit(surf2,(button2.x+35, button2.y+20))

    if events.type == pygame.MOUSEBUTTONDOWN and clicked == False:
        if button2.collidepoint(events.pos):
            click_sound.play()        
            button2_click = button2_click + 1
            clicked = True
    if events.type == pygame.MOUSEBUTTONUP:
        clicked = False
    if button2_click == 10:
        button2_click = 0     

    #przycisk 3 liczby w kodzie (zmiana wygladu przycisku po najechaniu i mozliwosc wyboru liczby 1-9)
    if button3.x <= a <= button3.x + 100 and button3.y <= b <= button3.y + 100:
        pygame.draw.circle(SCREEN, (24,26,86), button3.center, promien_kola)
    else:
        pygame.draw.circle(SCREEN, (15,17,66), button3.center, promien_kola)

    surf3 = font2.render(f'{button3_click}', True, (255, 255, 255))    
    SCREEN.blit(surf3,(button3.x+35, button3.y+20))

    if events.type == pygame.MOUSEBUTTONDOWN and clicked == False:
        if button3.collidepoint(events.pos):
            click_sound.play()        
            button3_click = button3_click + 1
            clicked = True
    if events.type == pygame.MOUSEBUTTONUP:
        clicked = False
    if button3_click == 10:
        button3_click = 0        

    #przycisk 4 liczby w kodzie 
    if button4.x <= a <= button4.x + 100 and button4.y <= b <= button4.y + 100:
        pygame.draw.circle(SCREEN, (24,26,86), button4.center, promien_kola)
    else:
        pygame.draw.circle(SCREEN, (15,17,66), button4.center, promien_kola)  

    surf4 = font2.render(f'{button4_click}', True, (255, 255, 255))    
    SCREEN.blit(surf4,(button4.x+35, button4.y+20))

    if events.type == pygame.MOUSEBUTTONDOWN and clicked == False:
        if button4.collidepoint(events.pos):
            click_sound.play()        
            button4_click = button4_click + 1
            clicked = True
    if events.type == pygame.MOUSEBUTTONUP:
        clicked = False
    if button4_click == 10:
        button4_click = 0        


    #czyszczenie ekranu w przypadku zapełenia hisotrii
    if c_y > HEIGHT+35:
        SCREEN.blit(bg, (0,0))
        
        #aktulizacja historii
        c_x = 10
        c_y = 10
        c_w_rect = 70
        c_h_rect = 40

        b_x = 85
        b_y = 10
        b_w_rect = 15
        b_h_rect = 15

        b_x_texture = 105
        b_y_texture = 10
        b_w_rect_texture = 15
        b_h_rect_texture = 15

        co_x = 85
        co_y = 35
        co_w_rect = 15
        co_h_rect = 15

        co_x_texture = 105
        co_y_texture = 35
        co_w_rect_texture = 15
        co_h_rect_texture = 15
        

        #wyswietlenie ostatniej proby
        history = pygame.draw.rect(SCREEN, c_rect, (c_x, c_y, c_w_rect, c_h_rect), border_radius = 10)
        SCREEN.blit(code2_rect, (history.x+5 , history.y+8 ))

        SCREEN.blit(bulls_rect, (b_x+4, b_y))
        SCREEN.blit(bulls_texture, (b_x_texture, b_y_texture))

        SCREEN.blit(cows_rect, (co_x+4, co_y))
        SCREEN.blit(cows_texture, (co_x_texture, co_y_texture))

        if(win_temp != 0):
            pygame.draw.rect(SCREEN,(0,0,0),win_score, border_radius = 20)
            SCREEN.blit(info_score,(win_score.x+12, win_score.y+2))

        c_y = c_y + c_h_rect + 10  
        b_y = b_y + c_h_rect + 10
        co_y = co_y + c_h_rect + 10
        b_y_texture = b_y_texture + c_h_rect + 10
        co_y_texture = co_y_texture + c_h_rect + 10
    
    pygame.display.update()


