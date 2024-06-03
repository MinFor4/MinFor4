import pygame as pg
import sys 
from random import randint

window=1010
pg.init()
screen=pg.display.set_mode((window,700))
background=pg.image.load("tloclicker.png")
background=pg.transform.scale(background,(window,window))
add_cookie=pg.USEREVENT+1
add_click_cookie=pg.USEREVENT+2
#cookie
cookie_image=pg.image.load("cookieclicker.png")
cookie_image=pg.transform.scale(cookie_image,(300,300))
cookie_rect=cookie_image.get_rect()
cookie_rect.center=(470,150)
cookie=0
#Przyciski
button2=pg.image.load("clickercursor.png")
button2=pg.transform.scale(button2,(91,70))
button2_rect=button2.get_rect()
button2_rect.center=(852,39)
background_button=pg.image.load("clickerbaner.jpg")
background_button=pg.transform.scale(background_button,(250,150))
background_button_rect=background_button.get_rect()
background_button_rect.center=(930,25)
button3=pg.image.load("cookiebox.png")
button3=pg.transform.scale(button3,(96,94))
background_button3=pg.image.load("banerclicker1.jpg")
background_button3=pg.transform.scale(background_button3,(210,110))
background_button3_rect=background_button3.get_rect()
background_button3_rect.center=(910,158)
button4=pg.image.load("minionek.png")
button4=pg.transform.scale(button4,(66,94))
background_button4=pg.image.load("clickerbaner3.jpg")
background_button4=pg.transform.scale(background_button4,(210,110))
background_button4_rect=background_button4.get_rect()
background_button4_rect.center=(912,271)
background_button5=pg.image.load("clickerbaner6.jpg")
background_button5=pg.transform.scale(background_button5,(210,100))
background_button5_rect=background_button5.get_rect()
background_button5_rect.center=(912,380)
button5=pg.image.load("factory.png")
button5=pg.transform.scale(button5,(170,120))
#Przycisk home
home_image=pg.image.load("DogHome1.png")
home_image=pg.transform.scale(home_image,(366,107))
home_image_rect=home_image.get_rect()
home_image_rect.center=(467,485)
frame_home=pg.image.load("ramka.png")
frame_home=pg.transform.scale(frame_home,(450,410))
frame_home_rect=frame_home.get_rect()
frame_home_rect.center=(466,485)
#grawitacja
class Physic:
    def __init__(self):
        self.speed_y=0
    def tick(self):
        self.speed_y+=0.2
#spadające ciastka 
cookiesky_image=pg.image.load("cookiesky.png")
cookiesky_image=pg.transform.scale(cookiesky_image,(70,70))
class Cookiesky(Physic):
    def __init__(self):
        super().__init__()
        self.spawn_x = randint(170, 800)
        self.spawn_y = -100  

    def gravity(self):
        self.spawn_y += self.speed_y 

    def draw(self):
        cookie_rect = cookiesky_image.get_rect()
        cookie_rect.center = (self.spawn_x, self.spawn_y)
        screen.blit(cookiesky_image, cookie_rect)

    def update(self):
        
        self.gravity()
        self.tick()
        self.draw()
        if self.spawn_y > 700: 
            cookie_in_sky.remove(self)
cookie_in_sky=[]       
x1=0
x2=0
x3=0
x4=0
plusx2=0
cookie_per1s=0

price4=2500
price3=150

price2=800

price1=55
while True:   
    
    plus_cookie=1+x1+x2
    mouse_pos=pg.mouse.get_pos()
    
    for event in pg.event.get():
        if event.type==pg.QUIT:
            sys.exit()
        if event.type==add_click_cookie:
            cookie+=plus_cookie
        if event.type==add_cookie:
            cookie+=cookie_per1s
        if event.type ==pg.MOUSEBUTTONDOWN:
            if cookie_rect.collidepoint(mouse_pos):
                cookie+=+1+x1+x2
                new_cookie=Cookiesky()
                cookie_in_sky.append(new_cookie)
            if home_image_rect.collidepoint(mouse_pos):
                print("Opcja tymczasowo nie dostęna")

            if background_button_rect.collidepoint(mouse_pos)  :
                
                if price1=="Max":
                    print("Masz maksymalną ilośc ulepszeń ")
                elif cookie>= price1:
                    x1+=1
                    cookie-=price1
                    if x1>=1:
                        price1=70
                    if x1>=2:
                        price1=90
                    if x1>=3:
                        price1=120
                    if x1>=4:
                        price1=150
                    if x1>=5:
                        price1=250
                    if x1>=6:
                        price1=300
                    if x1>=7:
                        price1=350
                    if x1>=8:
                        price1=450
                    if x1>=9:
                        price1=650
                    if x1>=10:
                        price1=1000
                    if x1>=11:
                        price1*=2
                    if x1>11:
                        price1=str("Max")
                else:
                    print("Nie masz wystarczającej ilości ciastek")
                
            if background_button3_rect.collidepoint(mouse_pos):
                if cookie=="Max":
                    print("Masz maksymalną ilość ciastek")
                elif cookie>=price2:
                    x2+=10
                    plusx2+=1
                    cookie-=price2
                    if plusx2>=1:
                        price2=1500
                    if plusx2>=2:
                        price2=2500
                    if plusx2>=3:
                        price2=4000
                    if plusx2>=4:
                        price2=6000
                    if plusx2>=5:
                        price2=8000
                    if plusx2>=6:
                        price2=10000
                    if plusx2>=7:
                        price2=12000
                    if plusx2>=8:
                        price2=15000
                    if plusx2>=9:
                        price2=18000
                    if plusx2>=10:
                        price2=21300
                    if plusx2>=11:
                        price2=str("Max")
                else:
                    print("Nie masz wystarczającej ilości ciastek")
            if background_button4_rect.collidepoint(mouse_pos):
                if price3=="Max":
                    print("Masz maksymalną ilośc ulepszeń")
                elif cookie >=price3:
                    cookie-=price3
                    x3+=1
                    cookie_per1s+=1
                    pg.time.set_timer(add_cookie,1000)
                      
                    if x3>=1:
                        price3=200
                    if x3>=2:
                        price3=260
                    if x3>=3:
                        price3=340
                    if x3>=4:
                        price3=400
                    if x3>=5:
                        price3=520
                    if  x3>=6:
                        price3=665
                    if x3>=7:
                        price3=745
                    if x3>=8:
                        price3=875
                    if x3>=9:
                        price3=1000
                    if x3>=10:
                        price3*=2  
                    if x3>=11:
                        price3="Max"
                else: 
                    print("Nie masz wystarczającej ilości ciastek")
            if background_button5_rect.collidepoint(mouse_pos):
                if price4=="Max":
                    print("Masz maksymalną ilość ulepszeń ")
                elif cookie>=price4:
                    cookie-=price4
                    x4+=1
                    plus_cookie=1+x1+x2+x3
                    pg.time.set_timer(add_click_cookie,1000)
                    if x4>=1:
                        price4="Max"
                    
                else:
                   print( "Nie masz wystarczająco ciastek")
                
                      
    score_txt=pg.font.Font.render(pg.font.SysFont(None,70),f"Liczba ciastek: {cookie}",True,"black")
    plus1_txt=pg.font.Font.render(pg.font.SysFont(None,45),"+1",True,"white")
    plus1x_txt=pg.font.Font.render(pg.font.SysFont(None,80),f"+{x1}",True,"white")
    price1_txt=pg.font.Font.render(pg.font.SysFont(None,37),f"Price:{price1}",True,"white")
    plus2x_txt=pg.font.Font.render(pg.font.SysFont(None,85),f"+{int(x2/10)}",True,"white")
    plus2_txt=pg.font.Font.render(pg.font.SysFont(None,45),"+10",True,"white")
    price2_txt=pg.font.Font.render(pg.font.SysFont(None,37),f"Price:{price2}",True,"white")
    plus3x_txt=pg.font.Font.render(pg.font.SysFont(None,80),f"+{x3}",True,"white")
    plus3_txt=pg.font.Font.render(pg.font.SysFont(None,45),"+1/s",True,"white")
    price3_txt=pg.font.Font.render(pg.font.SysFont(None,37),f"Price:{price3}",True,"white")
    plus4_txt=pg.font.Font.render(pg.font.SysFont(None,45),f"+{plus_cookie}/s",True,"white")
    price4_txt=pg.font.Font.render(pg.font.SysFont(None,37),f"Price:{price4}",True,"white")
    plus4x_txt=pg.font.Font.render(pg.font.SysFont(None,85),f"+{x4}",True,"white")
    screen.blit(background,(0,0))
    screen.blit(cookie_image,cookie_rect)
    screen.blit(score_txt,(285,335))
    screen.blit(frame_home,frame_home_rect)
    screen.blit(home_image,home_image_rect)
    screen.blit(background_button,background_button_rect)
    screen.blit(background_button3,background_button3_rect)
    screen.blit(button3,(800,95))
    screen.blit(background_button4,background_button4_rect)
    screen.blit(button4,(810,210))
    screen.blit(background_button5,background_button5_rect)
    screen.blit(button5,(770,305))
    screen.blit(price4_txt,(879,400))
    screen.blit(plus4_txt,(810,400))
    screen.blit(plus4x_txt,(900,330))
    screen.blit(plus1_txt,(837,70))
    screen.blit(plus1x_txt,(900,5))
    screen.blit(price1_txt,(879,70))
    screen.blit(price2_txt,(879,185))
    screen.blit(plus2_txt,(817,182))
    screen.blit(plus2x_txt,(900,110))
    screen.blit(button2,button2_rect)
    screen.blit(plus3_txt,(812,300))
    screen.blit(plus3x_txt,(900,230))
    screen.blit(price3_txt,(879,300))
    for cookie1 in cookie_in_sky:
        cookie1.update()
    pg.display.update()
