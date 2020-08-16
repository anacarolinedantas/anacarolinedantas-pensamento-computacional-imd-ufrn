# Atividade - Boxplot-ish
# O boxplot é uma forma interessante de visualizar um conjunto de dados, pois mostra em um único gráfico informações estatísticamente relevantes para um conjunto de números.
# O programa lê do usuário uma sequência de valores ordenados. Com esses valores em mãos, seu programa deve desenhar o boxplot utilizando a biblioteca turtle.

import math
import turtle

def principal():
  N = int(input("Número N de elementos: "))
  
  for i in range(N):
    if i == 0: #primeiro e menor elemento
      e = float(input("Elemento " + str(i+1)))
      e_ant = e
      menor = e
    
    else:
      e = float(input("Elemento " + str(i+1)))
      
      #verifica se o elemento anterior é maior que o atual
      if e_ant > e:
        print("Erro! Conjunto tem de estar em ordem crescente")
        break
      
      # quartil 1 e 3
      if i == round(N*(1/4)):
        quartil1 = e
      if i == round(N*(3/4)):
        quartil3 = e
      
      # mediana
      if N % 2 == 0:
        if i == N/2:
          mediana = (e_ant + e)/2
      else:
        if i == (N-1)/2:
          mediana = e
      
      #maior e último elemento
      if i == N-1:
        maior = e
        
      e_ant = e
  
  print("menor: " + str(menor))
  print("1º quartil: " + str(quartil1))
  print("mediana: " + str(mediana))
  print("3º quartil: " + str(quartil3))
  print("maior: " + str(maior))
  eixoY(menor,maior)
  desenhaBoxplot(menor, maior, quartil1, quartil3, mediana)

def eixoY(menor, maior):
  turtle.left(90)
  escala = 20
  t_num = turtle.Turtle()
  t_num.speed(20)
  turtle.speed(20)
  for i in range(round(menor),round(maior)+1):
    t_num.hideturtle()
    t_num.penup()
    t_num.goto(-40,i*escala)
    t_num.write(str(i), False, "center", ("Comic Sans", 10, "italic"))
    turtle.goto(0,i*escala)
    turtle.pendown()
    desenhaRetangulo(3,20)

def desenhaRetangulo(altura,largura):
  turtle.begin_fill()
  turtle.forward(altura)
  turtle.right(90)
  turtle.forward(largura)
  turtle.right(90)
  turtle.forward(altura)
  turtle.right(90)
  turtle.forward(largura)
  turtle.forward(largura)
  turtle.right(90)
  turtle.forward(altura)
  turtle.right(90)
  turtle.forward(largura)
  turtle.left(90)
  turtle.end_fill()

def desenhaBoxplot(menor, maior, quartil1, quartil3, mediana):
  escala = 20
  turtle.penup()
  turtle.goto(100,menor*escala)
  desenhaRetangulo(3,50)
  desenhaRetangulo((quartil1-menor)*escala,3)
  turtle.color("blue")
  desenhaRetangulo((quartil3-quartil1)*escala,50)
  turtle.color("black")
  desenhaRetangulo((maior-quartil3)*escala,3)
  desenhaRetangulo(3,50)
  turtle.penup()
  turtle.goto(100,mediana*escala)
  desenhaRetangulo(3,50)
  
principal()
