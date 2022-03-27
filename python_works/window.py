from tkinter import *   
import tkinter as tk
import pygame


pygame.mixer.init()            #инициализаия микшера pygame

clicks = 0                     #кликер в названии окна

c = 0                          #кликер в окне кликера

def play3():
                pygame.mixer.music.load("3.mp3")       #смех Бэна
                pygame.mixer.music.play(loops=0)       #повторение звука (в дпно случае = 0)

def move(event):                  #слежка за положенем курсора в окне
        x = event.x
        y = event.y
        s = "|o_0| {}x{}".format(x, y)
        window.title(s)
        
def click_b3():                         #окно с кринжовым вопросом и функция для 1-й кнопки
        window = Tk()      
        window.geometry("400x300")
                
        label = Label(window,           #сам вопрос
                text="Ты дыбил?)",
                font = ("Helvetica", 40),
                background="#203",
                foreground="#900")
        label.pack()
        label.place(x=45, y=70)

        btn = Button(window,               #кнопка 3
                text = "ДА",
                width = 6,                
                height = 2,
                background="#599",
                command = lambda: [play3(), click_b4()],    #релизация бинда двух функций на одну кнопку
                activebackground = "#390",
                font = ("Helvetica", 20))  
        btn.pack()
        btn.place(y=200, x=20)

        classButton = HoverButton(window,                   #кнопка 4
                text = "НЕТ", 
                width = 6,                
                height = 2,
                background="#900",
                command = lambda: [play3(), click_b4()],
                activebackground = "#390",                  #эта строка меняет визуал кнопки
                font = ("Helvetica", 20))
        classButton.pack()
        classButton.place(y=200, x=260)

        window["bg"]="#203"
        window.resizable(False, False)
        window.mainloop()

def click_b4():                              #функция для 4-й кнопки
        window = Tk()
        window.geometry("300x200")
            
        label = Label(window,
                text = "Я так и знал!!!",
                font = ("Helvetica", 30),
                background="#203",
                foreground="#390",)         
        label.pack()
        label.place(x=10, y=70)

        window["bg"]="#203"
        window.resizable(False, False)
        window.mainloop()

def click_b5():                              #функция для 2-й кнопки
        def play1():
                pygame.mixer.music.load("2.mp3")
                pygame.mixer.music.play(loops=0)

        def play2():
                pygame.mixer.music.load("1.mp3")
                pygame.mixer.music.play(loops=0)

        def click_b1():
                global clicks              #тыркалка в названии окна
                clicks += 1
                window.title("Clicks {}".format(clicks))

                global c                   #тыркалка в окне
                c += 1
                label['text'] = str(c)

        def click_b2():
                global clicks
                clicks -= 1
                window.title("Clicks {}".format(clicks))

                global c
                c -= 1
                label['text'] = str(c)      

        window = Tk()
        window.geometry("300x200")

        label = Label(window,              #конфиг тыркалки
                text= str(c),              #для отображения цифр кликера в окне
                font = ("Helvetica", 60),
                background="#203",
                foreground="#900")
        label.pack()

        btn = Button(window,               
                text = "YES",
                width = 7,                
                height = 1,
                background="#390",
                command = lambda: [play1(), click_b1()],
                font = ("Helvetica", 20))
        btn.pack()
        btn.place(y=145, x=0)

        btn = Button(window,               
                text = "NO",
                width = 7,
                height = 1,
                background="#900",
                command = lambda: [play2(), click_b2()],
                font = ("Helvetica", 20))
        btn.pack()
        btn.place(y=145, x=163)

        window["bg"]="#203"
        window.resizable(False, False)
        window.mainloop()

class HoverButton(tk.Button):                                 #для подмены кнопки
        def __init__(self, master, **kw):
                tk.Button.__init__(self,master=master,**kw)   #изначальный фон
                self.defaultBackground = self["background"]   #изначальный текст
                self.defaultText = self["text"]
                self.bind("<Enter>", self.on_enter)
                self.bind("<Leave>", self.on_leave)

        def on_enter(self, e):
                self['background'] = self['activebackground'] #для подмены фона
                self['text'] = "ДА"                           #для подмены текста

        def on_leave(self, e):
                self['background'] = self.defaultBackground   #что бы вернуть дефолтный фон
                self['text'] = self.defaultText               #что бы вернуть дефолтный текст

window = Tk()                      #окно
window.geometry("300x400")  

window.bind('<Motion>', move)      #для слежки за курсором

label = Label(window,
        text = "MENU",
        font = ("Helvetica", 30),
        background="#203",
        foreground="#390")         
label.pack()
label.place(x=85, y=70)

btn = Button(window,               
        text = "have a qestion for YOU!",
        width = 19,                #ширина
        height = 2,                #высота
        background="#458",
        command = click_b3,
        font = ("Helvetica", 18))        #цвет кнопки
btn.pack()
btn.place(y=300, x=3) 

btn = Button(window,               
        text = "Clicker",
        width = 19,                #ширина
        height = 2,                #высота
        background="#458",
        command = click_b5,
        font = ("Helvetica", 18))        #цвет кнопки
btn.pack()
btn.place(x=3, y=200)

window.resizable(False, False)     #заморозка разрешения окна
window["bg"]="#203"
window.mainloop()  
