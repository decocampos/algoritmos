import math

def calculo(formula,instrucoes,velocidade,computador):
  if formula=="2n^2":
    tempo= (2*instrucoes**2)/velocidade
  elif formula=="n.logn":
    tempo= (instrucoes*math.log10(instrucoes))/velocidade
  elif formula=="2^n":
    tempo= 2**instrucoes/velocidade
  elif formula=="n":
    tempo= instrucoes/velocidade
    
  print(f"Velocidade do {computador}: {tempo:.2f} segundos")
  return tempo
  

instrucoes =int(input())
info1=input().split(' - ')
velocidade1=int(info1[1])
info2=input().split(' - ')
velocidade2=int(info2[1])

tempo1 = calculo(info1[3],instrucoes,velocidade1,info1[0])
tempo2 = calculo(info2[3],instrucoes,velocidade2,info2[0])

if tempo1<tempo2:
  print(f"O {info1[0]} foi mais rápido!")
else:
  print(f"O {info2[0]} foi mais rápido!")




