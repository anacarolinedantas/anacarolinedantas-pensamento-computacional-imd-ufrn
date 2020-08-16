#Pontos mais próximos
#Esse programa lê do usuário um conjunto de pontos e imprime as coordenadas dos dois pontos mais próximos.
#Além de verificar visualmente o conjunto de pontos, destacando os pontos mais próximos.

import math
import turtle

def principal():
  vetor_pontos = []
  vetor_distancias = []
  n = int(input("Quantos pontos?"))
  
  for i in range(n):
    p = lerPonto("Digite o " + str(i+1) + "º ponto: ")
    vetor_pontos = vetorPontos(vetor_pontos, p)
  
  a,b = PontoMaisProximo(vetor_pontos,n)
  print("Pontos mais próximos: " + str(vetor_pontos[a]) + " e " + str(vetor_pontos[b]))
  desenhaPoligono(vetor_pontos,a,b)
  
def lerPonto(msg):
  p = []
  ponto = input(msg).split()
  for i in ponto:
    p.append(int(i))
  return p
  
def vetorPontos(vetor_pontos, p):
  vetor_pontos.append(p)
  return vetor_pontos

def PontoMaisProximo(vetor_pontos,n):
  md = calculaDistancia(vetor_pontos[0],vetor_pontos[1])
  for i in range(n-1):
    for j in range(i+1, n):
      if calculaDistancia(vetor_pontos[i],vetor_pontos[j]) < md:
        md = calculaDistancia(vetor_pontos[i],vetor_pontos[j])
        a = i
        b = j
  return a,b

def calculaDistancia(p0,p1):
  d = math.sqrt((p0[0]-p1[0])**2 + (p0[1]-p1[1])**2)
  return d

def desenhaPoligono(vetor_pontos,a,b):
  turtle.hideturtle()
  turtle.penup()
  for i, v in enumerate(vetor_pontos):
    if i == a or i == b:
      turtle.goto(v)
      turtle.color("red")
      #turtle.pendown()
      turtle.dot(5)
      turtle.color("black")
    else:
      turtle.goto(v)
      #turtle.pendown()
      turtle.dot(5)

principal()
