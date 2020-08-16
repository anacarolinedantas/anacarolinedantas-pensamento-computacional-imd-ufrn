#Atividade - Ponto em polígono
#Essa programa testa a colisão entre um ponto e um polígono (côncavo ou convexo). Além disso, utilizando a bilioteca turtle, desenha o polígono e o ponto.

import turtle

def principal():
  x = leituraValores("Valores de x: ")
  x.append(int(x[0]))
  y = leituraValores("Valores de y: ")
  y.append(int(y[0]))
  pt = leituraValores("Qual o ponto a ser verificado?")
  desenhaPoligono(x,y)
  convexo = verificaConcavoConvexo(x,y)
  
  if verificaColisao(x,y,pt,convexo) == False:
    print("O ponto está fora do polígono")
    turtle.color("red")
    desenhaPonto(pt)
  else:
    print("O ponto está dentro do polígono")
    turtle.color("green")
    desenhaPonto(pt)

def leituraValores(msg):
  valores = input(msg).split()
  lista = []
  for i in valores:
    lista.append(int(i))
  return lista

def produtoVetorial(x0, y0, x1, y1):
  vz = x0*y1 - y0*x1
  return vz

def desenhaPoligono(x,y):
  turtle.speed(20)
  turtle.hideturtle()
  turtle.penup()
  turtle.goto(x[0],y[0])
  for i in range(1, len(y)):
    turtle.pendown()
    turtle.goto(x[i],y[i])
    turtle.dot(8)

def desenhaPonto(pt):
  turtle.penup()
  turtle.goto(pt)
  turtle.dot(8)

def verificaConcavoConvexo(x,y):
  convexo = True
  for i in range(1, len(x)-1):
    if produtoVetorial(x[i]-x[i-1], y[i]-y[i-1], x[i+1]-x[i], y[i+1]-y[i]) > 0:
      convexo = False
  return convexo

def verificaColisao(x,y,pt,convexo):
  colisao = True
  
  #se o polígono for convexo, verifica o produto vetorial entre P(i-1).P(i) e pt.(i)
  if convexo == True:
    for i in range(1, len(x)):
      if produtoVetorial(x[i]-x[i-1], y[i]-y[i-1], x[i]-pt[0], y[i]-pt[1]) < 0:
        colisao = False
        break
  
  #se o polígono for côncavo, muda a ordem do produto vetorial: pt.P(i) e P(i-1).P(i)
  else:
    for i in range(1, len(x)):
      if produtoVetorial(x[i]-pt[0], y[i]-pt[1], x[i]-x[i-1], y[i]-y[i-1]) < 0:
        colisao = False
        break
  
  return colisao

principal()