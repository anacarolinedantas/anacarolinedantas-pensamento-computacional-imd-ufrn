# Atividade - Padrão
# Na área de Bioinformática, uma situação comum é procurar por padrões em sequenciamentos genéticos. Podemos assim descobrir se um sequênciamento possui ou não um determinado "código" nos seus gens. Essa tarefa é similar à busca por padrões numa sequência numérica. Isto é, procuramos ver se há uma sequência (menor) dentro de outra sequência (maior).
# Esse programa verifica se uma sequência se encontra em outra sequência

def leituraValores(msg):
  valores = input(msg).split()
  list = []
  for i in valores:
    list.append(int(i))
  return list

def VerificaIgualdade(seq1,seq2):
  iguais = False
  for i in range(len(seq1)):
    for j in range(len(seq2)):
      if seq1[i] == seq2[j]:
        iguais = True
      else:
        iguais = False
  return iguais

def principal():
  lista1 = leituraValores("Qual a 1ª sequência? ")
  lista2 = leituraValores("Qual a 2ª sequência? ")
  
  seqTeste = []
  padrao = False
  
  for i in range(len(lista2)-len(lista1)+1):
    if lista2[i] == lista1[0]:
      indice = i
      
      #quando existe um elemento na segunda sequencia igual ao primeiro elemento da primeira sequencia, 
      #ele cria uma lista com o 3 elementos seguintes da segunda sequencia.
      for j in range(i, i+len(lista1)):
        seqTeste.append(lista2[j])
      
      #verifica se a sequencia criada é igual à primeira sequência
      if VerificaIgualdade(lista1,seqTeste) == True:
        padrao = True
        break
      else:
        padrao = False
  
  if padrao == True:
    print("Há um casamento de padrão no índice " + str(indice))
  else:
    print("Não há casamento de padrão")

principal()