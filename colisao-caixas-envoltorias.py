# Atividade - Colisão entre Caixas Envoltórias
# Caixa envoltoria é uma forma "simples" de verificar se duas figuras colidem em um espaço 2D. 
# Esse programa se há colisão entre duas caixas envoltórias.

import turtle

def principal():
  print("Coordenadas da caixa 1:")
  xc1 = float(input("xc1: "))
  yc1 = float(input("yc1: "))
  lc1 = float(input("lc1: "))
  ac1 = float(input("ac1: "))
  print("Coordenadas da caixa 2:")
  xc2 = float(input("xc2: "))
  yc2 = float(input("yc2: "))
  lc2 = float(input("lc2: "))
  ac2 = float(input("ac2: "))
  testaColisao(xc1,yc1,lc1,ac1,xc2,yc2,lc2,ac2)
  desenha(xc1,yc1,lc1,ac1,xc2,yc2,lc2,ac2)

def testaColisao(xc1,yc1,lc1,ac1,xc2,yc2,lc2,ac2):
  if (xc2 >= xc1) and (xc2 <= xc1+ac1):
    if (yc2 <= yc1) and (yc2 >= yc1-ac1):
      print("Colide!")
    elif (yc2-ac2 <= yc1) and (yc2-ac2 >= yc1-ac1):
      print("Colide!")

  elif (xc2+lc2 >= xc1) and (xc2+lc2 <= xc1+ac1):
    if (yc2 <= yc1) and (yc2 >= yc1-ac1):
      print("Colide!")
    elif (yc2-ac2 <= yc1) and (yc2-ac2 >= yc1-ac1):
      print("Colide!")

  else:
    print("Não colide!")

def desenha(xc1,yc1,lc1,ac1,xc2,yc2,lc2,ac2):
  escala = 20
  turtle.penup()
  turtle.goto(xc1*escala,yc1*escala)
  turtle.pendown()
  turtle.forward(lc1*escala)
  turtle.right(90)
  turtle.forward(ac1*escala)
  turtle.right(90)
  turtle.forward(lc1*escala)
  turtle.right(90)
  turtle.forward(ac1*escala)
  turtle.right(90)
  
  turtle.penup()
  turtle.goto(xc2*escala,yc2*escala)
  turtle.pendown()
  turtle.forward(lc2*escala)
  turtle.right(90)
  turtle.forward(ac2*escala)
  turtle.right(90)
  turtle.forward(lc2*escala)
  turtle.right(90)
  turtle.forward(ac2*escala)
  turtle.right(90)

principal()
