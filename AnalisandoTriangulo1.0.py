from time import sleep
print("-=-" * 20)
print("Analisador de Triângulos")
print("-=-" * 20)
r1 = float(input("Escreva a primeira reta: "))
r2 = float(input("Escreva a segunda reta: "))
r3 = float(input("Escreva a terceira reta: "))
if  r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print("Analisando...")
    sleep(2)
    print("Tem como construir o triangulo")
else:
    print("Não tem como construir")