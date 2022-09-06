"""
Universidade Federal do Pará (UFPA)
Engenharia de Computação
Campus Tucuruí
Computação Gráfica e Processamento Digital de Imagem
Professor Dr. Marcos Tulio Amaris
Aluno: Danilo de Sousa Lopes        Mat: 201833840019
-----------------------------------------------------
Atividade: Desenvolva uma GUI que desenha as letras de
seu nome, além de conter quatro menus e em cada um colocar
as letras da seguinte forma: Primeiro Nome, Segundo Nome,
Primeiro Sobrenome e Segundo Sobrenome. Extra: ao clicar
as letras devem ser desenhadas usando o módulo Turtle Graphics. 
"""
from importlib.util import find_spec
from tkinter import *
from turtle import *
import turtle

def f_name (i,j):
    t = turtle.Turtle()
    t.shape("turtle")
    t.speed(5)
    t.pen(fillcolor="green", pencolor="blue", pensize=20)
    #-------------- Letra D
    t.penup()
    t.setposition(-300,0)
    t.pendown()
    t.right(90)
    t.fd(130)
    t.left(90)
    t.circle(65,180)
    t.left(180)
    t.penup()
    t.fd(110)
    t.pendown()
    #-------------- Letra A
    t.right(70)
    t.fd(130)
    t.bk(130)
    t.right(35)
    t.fd(130)
    t.bk(65)
    t.left(105)
    t.fd(40)
    t.right(70)
    t.bk(65)
    t.left(70)
    t.penup()
    t.fd(80)
    t.pendown()
    #-------------- Letra N
    t.right(90)
    t.fd(130)
    t.bk(130)
    t.left(30)
    t.fd(150)
    t.left(150)
    t.fd(130)
    t.right(90)
    t.penup()
    t.fd(30)
    t.pendown()
    #-------------- Letra I
    t.right(90)
    t.fd(130)
    t.bk(130)
    t.left(90)
    t.penup()
    t.fd(30)
    t.pendown()
    #-------------- Letra L
    t.right(90)
    t.fd(130)
    t.left(90)
    t.fd(60)
    t.left(90)
    t.penup()
    t.fd(130)
    t.right(90)
    t.fd(80)
    #-------------- Letra O
    t.right(90)
    t.fd(130)
    t.left(90)
    t.pendown()
    t.circle(60,400)

def first_name():
    # configurações iniciais
    screen = turtle.Screen()
    turtle.title("Danilo")
    screen.onclick(f_name)

def s_name (i,j):
    t = turtle.Turtle()
    t.shape("turtle")
    t.speed(5)
    t.pen(fillcolor="green", pencolor="blue", pensize=20)
    #-------------- Letra S
    t.penup()
    t.setposition(-300,0)
    t.pendown()
    t.fd(30)
    t.bk(30)
    t.circle(-40,-170)
    t.circle(40,-235)
    t.penup()
    t.right(295)
    t.fd(200)
    t.pendown()
    #-------------- Letra O
    t.circle(70,400)
    t.penup()
    t.right(40)
    t.fd(60)
    t.left(90)
    t.fd(120)
    t.left(180)
    t.pendown()
    #-------------- Letra U
    t.fd(100)
    t.circle(50,180)
    t.fd(95)
    t.penup()
    t.right(90)
    t.fd(100)
    t.pendown()
    #-------------- Letra S
    t.fd(30)
    t.bk(30)
    t.circle(-40,-170)
    t.circle(40,-235)
    t.penup()
    t.right(295)
    t.fd(120)
    t.left(70)
    t.bk(20)
    t.pendown()
    #-------------- Letra A
    t.fd(150)
    t.right(140)
    t.fd(150)
    t.bk(70)
    t.right(110)
    t.fd(55)
    t.penup()
    t.bk(100)

def second_name():
    # configurações iniciais
    screen = turtle.Screen()
    turtle.title("Sousa")
    screen.onclick(s_name)

def l_name (i,j):
    t = turtle.Turtle()
    t.shape("turtle")
    t.speed(5)
    t.pen(fillcolor="green", pencolor="blue", pensize=20)
   #-------------- Letra L
    t.penup()
    t.setposition(-300,0)
    t.pendown()
    t.right(90)
    t.fd(130)
    t.left(90)
    t.fd(80)
    t.penup()
    t.fd(90)
    t.pendown()
    #-------------- Letra O
    t.circle(70,400)
    t.penup()
    t.right(40)
    t.fd(60)
    t.left(90)
    t.fd(120)
    t.left(180)
    t.pendown()
    #-------------- Letra P
    t.fd(140)
    t.bk(140)
    t.left(90)
    t.circle(-50,180)
    t.right(180)
    t.penup()
    t.fd(100)
    t.left(90)
    t.fd(100)
    t.right(90)
    t.pendown()
    #-------------- Letra E
    t.fd(60)
    t.bk(60)
    t.right(90)
    t.fd(70)
    t.left(90)
    t.fd(60)
    t.bk(60)
    t.right(90)
    t.fd(70)
    t.left(90)
    t.fd(60)
    t.penup()
    t.left(90)
    t.fd(140)
    t.right(90)
    t.fd(100)
    t.pendown()
    #-------------- Letra S
    t.fd(30)
    t.bk(30)
    t.circle(-40,-170)
    t.circle(40,-235)

def last_name():
    # configurações iniciais
    screen = turtle.Screen()
    turtle.title("Lopes")
    screen.onclick(l_name)

app=Tk()
app.title('Atividade 2 CG - Danilo Lopes')
app.geometry('720x480')

menu_bar=Menu(app)
menu_File=Menu(menu_bar,tearoff=0)
menu_File.add_command(label='First Name',command=first_name)
menu_File.add_command(label='Second Name',command=second_name)
menu_File.add_command(label='Last Name',command=last_name)
menu_File.add_command(label='Fechar',command=app.quit)
menu_bar.add_cascade(label='File',menu=menu_File)
app.config(menu=menu_bar)
app.mainloop()

