# Atividade - Côncavo ou convexo
# Esse programa lê duas sequências de coordenadas, uma para x e outra para y, desenha o polígono e informa se o polígono é côncavo ou convexo.

import turtle

def produtoVetorial(x0, y0, x1, y1):
  vz = x0*y1 - y0*x1
  return vz

def desenhaPoligono(x_lista,y_lista):
  turtle.penup()
  turtle.goto(x_lista[0],y_lista[0])
  for i in range(1, len(y_lista)):
    turtle.pendown()
    turtle.goto(x_lista[i],y_lista[i])
    turtle.dot(5)

def leituraValores(comp):
  valores = input("Valores de " + str(comp) + ":")
  valores_List = valores.split()
  lista = []
  for i in valores_List:
    lista.append(int(i))
  lista.append(int(valores_List[0]))
  return lista

def principal():
  x_lista = leituraValores('x')
  y_lista = leituraValores('y')
  
  desenhaPoligono(x_lista,y_lista)
  
  convexo = True
  for i in range(1, len(x_lista)-1):
    if produtoVetorial(x_lista[i]-x_lista[i-1], y_lista[i]-y_lista[i-1], x_lista[i+1]-x_lista[i], y_lista[i+1]-y_lista[i]) < 0:
      convexo = False
  
  if convexo == True:
    print("Convexo")
  else:
    print("Côncavo")

principal()
  
