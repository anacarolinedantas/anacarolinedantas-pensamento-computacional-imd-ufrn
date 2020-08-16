# Atividade - Caixa Envoltória
# Caixa envoltoria é uma forma "simples" de verificar se duas figuras colidem em um espaço 2D. 
# Esse programa calcula e desenha a caixa envoltória de um polígono.

import turtle

def principal():
  N = int(input("Número N de pontos do polígono: "))
  
  for i in range(N):
    if i == 0:
      xp = float(input("x"))
      yp = float(input("y"))
      xi = xmaior = xc = xp
      yi = ymenor = yc = yp
      turtle.penup()
      desenhaPoligono(xp,yp)
    else:
      xp = float(input("x"))
      yp = float(input("y"))
      desenhaPoligono(xp,yp)
      if xp < xc:
        xc = xp
      elif xp > xmaior:
        xmaior = xp
      if yp > yc:
        yc = yp
      elif yp < ymenor:
        ymenor = yp
  
  A = yc - ymenor
  L = xmaior - xc
  print("Caixa: X1, Y1 = " + str(xc) + "," + str(yc) + " ; A=" + str(A) + ", L=" + str(L))
  desenhaPoligono(xi,yi)
  desenhaCaixaEnv(xc, yc, A, L)
  
def desenhaPoligono(x,y):
  escala = 20
  turtle.color("blue")
  turtle.goto(x*escala,y*escala)
  turtle.pendown()
  turtle.color("red")
  turtle.dot(5)
  
def desenhaCaixaEnv(xc, yc, A, L):
  escala = 20
  turtle.penup()
  turtle.goto(xc*escala,yc*escala)
  turtle.pendown()
  turtle.color("red")
  turtle.dot(6)
  turtle.color("black")
  turtle.forward(L*escala)
  turtle.right(90)
  turtle.forward(A*escala)
  turtle.right(90)
  turtle.forward(L*escala)
  turtle.right(90)
  turtle.forward(A*escala)
  turtle.right(90)
  
principal()
