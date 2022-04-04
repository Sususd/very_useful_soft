import turtle
import colorsys
from tkinter import *
import tkinter as tk
from pygame import mixer
import os
import sys
from tkinter import ttk
from tkinter.messagebox import showinfo
import tkinter.font as tkFont
import time
import fnmatch


mixer.init()

clicks = 0                     #кликер в названии окна

c = 0                          #кликер в окне кликера

def play3():
        pygame.mixer.music.load("3.mp3")       #смех Бэна
        pygame.mixer.music.play(loops=0)       #повторение звука (в дпно случае = 0)

def move(event):                #слежка за положенем курсора в окне
        x = event.x
        y = event.y
        s = "|o_O| {}x{}".format(x, y)
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

def click_b7():

        window = Tk()
        window.geometry("550x250")

        label = Label(window,
                text = "DigitaL",
                foreground="#390",
                background="#203",
                font = ("Helvetica", 30))
        label.pack()

        def timing():                     #часы
                current_time = time.strftime("%H : %M : %S")
                clock.config(text=current_time)
                clock.after(200,timing)

        clock=tk.Label(window,             #конфиг часов
                font=("times",80,"bold"),
                background="#203",
                foreground="#499")
        clock.pack()
        clock.place(x=5, y=70)
        timing()

        window["bg"]="#203"
        window.resizable(False, False)
        window.mainloop()

def music():
	window = tk.Tk()
	window.title("Music Player")
	window.geometry("800x520")
	window.config(bg = "black")

	rootpath = "Музыка"
	pattern = "*.mp3"

	def select():
		label.config(text = listBox.get("anchor"))
		mixer.music.load(rootpath + "//" + listBox.get("anchor"))
		mixer.music.play()

	def stop():
		mixer.music.stop()
		listBox.select_clear("active")

	def play_next():
		next_song = listBox.curselection()
		next_song = next_song[0] + 1
		next_song_name = listBox.get(next_song)
		label.config(text = next_song_name)
		mixer.music.load(rootpath + "//" + next_song_name)
		mixer.music.play()
		listBox.select_clear(0, "end")
		listBox.activate(next_song)
		listBox.select_set(next_song)

	def play_prev():
		next_song = listBox.curselection()
		next_song = next_song[0] - 1
		next_song_name = listBox.get(next_song)
		label.config(text = next_song_name)
		mixer.music.load(rootpath + "//" + next_song_name)
		mixer.music.play()
		listBox.select_clear(0, "end")
		listBox.activate(next_song)
		listBox.select_set(next_song)

	def pause_song():
		if pauseButton["text"] == "Pause":
			mixer.music.pause()
			pauseButton["text"] = "Play"
		else:
			mixer.music.unpause()
			pauseButton["text"] = "Pause"

	listBox = tk.Listbox(window, fg = "cyan",  bg = "black", width = 100, font = ("ds-digital", 14))
	listBox.pack(padx = 15, pady = 15)

	label = tk.Label(window, text = "", bg = "black", fg = "yellow", font = ("ds-digital", 18))
	label.pack(pady = 15)
	top = tk.Frame(window, bg = "black")
	top.pack(padx = 10, pady = 5, anchor = "center")

	prev = tk.Button(window, text = "Попередній", command = play_prev)
	prev.pack(pady = 15, in_ = top, side = "left")

	stop = tk.Button(window, text = "Стоп", command = stop)
	stop.pack(pady = 15,in_ = top, side = "left" )

	play = tk.Button(window, text = "Грати", command = select)
	play.pack(pady = 15,in_ = top, side = "left" )

	pause = tk.Button(window, text = "Пауза", command = pause_song)
	pause.pack(pady = 15,in_ = top, side = "left" )

	next = tk.Button(window, text = "Наступний", command = play_next)
	next.pack(pady = 15,in_ = top, side = "left" )

	for root, dirs, files, in os.walk(rootpath):
		for filename in fnmatch.filter(files, pattern):
			listBox.insert("end", filename)

	window.resizable(False, False)
	window.mainloop()

class HoverButton(tk.Button):                          #для подмены кнопки
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

class HoverButton1(tk.Button):
        def __init__(self, master, **kw):
                tk.Button.__init__(self,master=master,**kw)
                self.defaultBackground = self["background"]
                self.bind("<Enter>", self.on_enter)
                self.bind("<Leave>", self.on_leave)

        def on_enter(self, e):
                self['background'] = self['activebackground']

        def on_leave(self, e):
                self['background'] = self.defaultBackground



window = Tk()                      #окно
window.geometry("300x800")

window.bind('<Motion>', move)      #для слежки за курсором

label = Label(window,
        text = "MENU",
        font = ("Helvetica", 30),
        background="#203",
        foreground="#390")
label.pack()
label.place(x=85, y=20)

#fourloadimage = PhotoImage(file = "b4.png")

btn = Button(window,
	#image = fourloadimage,
        text = "have a qestion for YOU!",
        width = 19,                #ширина
        height = 2,                #высота
        background="#458",
        command = click_b3,
        font = ("Helvetica", 18))        #цвет кнопки
btn.pack()
btn.place(y=480, x=25)

#sloadimage = PhotoImage(file = "b2.png")

btn = Button(window,
	#image = sloadimage,
        text = "Clicker",
        width = 19,                #ширина
        height = 2,                #высота
        background="#458",
        command = click_b5,
        font = ("Helvetica", 18))        #цвет кнопки
btn.pack()
btn.place(x=25, y=370)

def Close():
        window.destroy()

classButton = HoverButton1(window,
        text = "Exit",
        width = 7,                #ширина
        height = 1,                #высота
        background = "#458",
        activebackground = "#900",
        foreground = "#500",
        font = ("Helvetica", 16),
        command = Close)
classButton.pack()
classButton.place(x=165, y=740)

classButton = HoverButton1(window,
        text = "About us",
        width = 7,                #ширина
        height = 1,                #высота
        background = "#458",
        activebackground = "#390",
        foreground = "#500",
        font = ("Helvetica", 16))
classButton.pack()
classButton.place(x=25, y=740)

#floadimage = PhotoImage(file = "b11.png")

btn = Button(window,
	#image = floadimage,
        text = "time widget",
        command = click_b7,
        width = 19,
        height = 2,
        background = "#458",
        font = ("Helvetica", 18))
btn.pack()
btn.place(x=25, y=260)

def epic_moment():
	t = turtle.Turtle()
	s = turtle.Screen()

	s.bgcolor("black")
	t.speed(0)

	n = 36
	h = 0

	for i in range(460):
        	c = colorsys.hsv_to_rgb(h, 1, 0.9)
        	h += 1
        	t.color(c)
        	t.left(145)
        	for j in range(5):
                	t.forward(300)
                	t.left(150)

#tloadimage = PhotoImage(file = "b3.png")

btn = Button(window,
	#image = tloadimage,
        text = "Epic",
        command = epic_moment,
        width = 19,
        height = 2,
        background = "#458",
        font = ("Helvetica", 18))
btn.pack()
btn.place(x=25, y=150)

btn = Button(window,
	text = "Player",
	width = 19,
	height = 2,
	background = "#458",
	font = ("Helvetica", 18),
	command = music)
btn.pack()
btn.place(x=25, y=50)

window.resizable(False, False)     #заморозка разрешения окна
window["bg"]="#203"
window.mainloop()
