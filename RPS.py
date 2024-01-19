import random
from guizero import *
import pygame
import playsound
# ==============================
def results(b):
    r = "Rock"
    p = "Paper"
    s = "Scissors"
    a = [r, p, s]
    c = random.choice(a)
    yr.hide()
    er.hide()
    if c == r:
        erock1.show()
        epaper1.hide()
        escissors1.hide()
        if b == r:
            yrock1.show()
            ypaper1.hide()
            yscissors1.hide()
            resulttxt.value = "Draw ! try again."
            playsound.playsound("sounds/rock.wav")
        elif b == s:
            yrock1.hide()
            ypaper1.hide()
            yscissors1.show()
            resulttxt.value = "You lose!"
            playsound.playsound("sounds/scissors.wav")
        elif b == p:
            yrock1.hide()
            ypaper1.show()
            yscissors1.hide()
            resulttxt.value = "You win!"
            playsound.playsound("sounds/paper.wav")
    elif c == p:
        epaper1.show()
        erock1.hide()
        escissors1.hide()
        if b == r:
            yrock1.show()
            ypaper1.hide()
            yscissors1.hide()
            resulttxt.value = "You lose!"
            playsound.playsound("sounds/rock.wav")
        elif b == p:
            yrock1.hide()
            ypaper1.show()
            yscissors1.hide()
            resulttxt.value = "Draw ! try again."
            playsound.playsound("sounds/paper.wav")
        elif b == s:
            yrock1.hide()
            ypaper1.hide()
            yscissors1.show()
            resulttxt.value = "You win!"
            playsound.playsound("sounds/scissors.wav")
    elif c == s:
        escissors1.show()
        epaper1.hide()
        erock1.hide()
        if b == r:
            yrock1.show()
            ypaper1.hide()
            yscissors1.hide()
            resulttxt.value = "You win!"
            playsound.playsound("sounds/rock.wav")
        elif b == p:
            yrock1.hide()
            ypaper1.show()
            yscissors1.hide()
            resulttxt.value = "You lose!"
            playsound.playsound("sounds/paper.wav")
        elif b == s:
            yrock1.hide()
            ypaper1.hide()
            yscissors1.show()
            resulttxt.value = "Draw ! try again."
            playsound.playsound("sounds/scissors.wav")
def rockbutt():
    b = "Rock"
    results(b)
def scbutt():
    b = "Scissors"
    results(b)
def paperb():
    b = "Paper"
    results(b)
#=====================================
pygame.init()
pst=App(title="Rock Paper Scissors", width=730, height=440, bg="brown", layout="grid")
box1=Box(pst, grid=[0 , 0], layout="grid")
text1 =Text(box1, text="  Choose your move to start the game!", size=24, font="Bowlby One SC", grid=[0,0])
box2=Box(box1, grid=[0 , 1], layout="grid")
box3=Box(box2, grid=[1 , 2])
box4=Box(box2, grid=[2 , 2])
box5=Box(box2, grid=[3 , 2])
rb = PushButton(box3, command=rockbutt, image="images/rock1.png", height=88, width=88)
pb = PushButton(box4, command=paperb, image="images/paper1.png", height=88, width=88)
sb = PushButton(box5, command=scbutt, image="images/scissors1.png", height=88, width=88)
box7=Box(box1, grid=[0,2])
spacetext=Text(box7, text=" ")
box6=Box(box1, layout="grid", grid=[0, 3])
textvs=Text(box6, size= 24, font="Bowlby One SC", grid=[2,0], text="VS")
yr= Picture(box6, grid=[1,0] ,image="images/yq.png", visible=True, width=64, height=64)
er= Picture(box6, grid=[3,0] ,image="images/eq.png", visible=True, width=64, height=64)
yrock1= Picture(box6, grid=[1,0] ,image="images/rock12.png", visible=False, width=64, height=64)
ypaper1= Picture(box6, grid=[1,0] ,image="images/paper14.png", visible=False, width=64, height=64)
yscissors1= Picture(box6, grid=[1,0] ,image="images/scissors13.png", visible=False, width=64, height=64)
erock1= Picture(box6, grid=[3,0] ,image="images/rock24.png", visible=False, width=64, height=64)
epaper1= Picture(box6, grid=[3,0] ,image="images/paper22.png", visible=False, width=64, height=64)
escissors1= Picture(box6, grid=[3,0] ,image="images/scissors23.png", visible=False, width=64, height=64)
urmv = Picture(box6, image="images/character.png", height=86,width=88, grid=[0,0])
opmv = Picture(box6, image="images/cpu.png", height=86,width=86, grid=[4,0])
box8=Box(box1, layout="grid", grid=[0,4])
resulttxt = Text(box8, text="", size=40, grid=[0,0], font="Bowlby One SC")
audio_files = ["sounds/lofi0.mp3"]
for file_path in audio_files:
    sound = pygame.mixer.Sound(file_path)
    sound.set_volume(0.3)
    sound.play()
pst.display()
pygame.quit()
