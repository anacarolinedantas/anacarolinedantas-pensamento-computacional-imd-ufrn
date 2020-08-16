# Atividade - Guess 2/3
# O "Guess 2/3" é um jogo simples que é explorado na área de Teoria dos Jogos para estudar, entre outros, comportamentos sociais e econômicos.
# As regras do jogo são simples. Podem participar vários jogadores. Cada um escolhe um número real entre 0 e 100 sem que os demais saibam do seu palpite. Depois de todos escolherem seus valores, ganha quem escolheu o número mais próximo de 2/3 da média dos valores escolhidos.

palpites = input("Digite os palpites dos jogadores (0 a 100): ")
palpitesList = palpites.split()
intList = []
for t in palpitesList:
  intList.append(float(t))

#calcular média
soma = 0
for i in intList:
  if i < 0 and i > 100:
    print("Erro, possui um palpite acima de 100")
    break
  else:
    soma = soma + i
media = soma/len(intList)

#verifica a menor diferença
menorDif = abs(media*1/2 - intList[0])
for v in intList:
  if abs(media*1/2 - v) <= menorDif:
    menorDif = abs(media*1/2 - v)

#imprime os ganhadores
for i, v in enumerate(intList):
  if abs(media*1/2 - v) == menorDif and verificaPar(v):
    print("Ganhadores: " + str(i))

def verificaPar(a):
  if a % 2 == 0:
    return True
  else:
    return False
