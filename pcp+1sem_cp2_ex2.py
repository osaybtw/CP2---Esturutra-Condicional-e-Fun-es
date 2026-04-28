#Entrada de dados
A = float(input("Digite o lado A: "))
B = float(input("Digite o lado B: "))
C = float(input("Digite o lado C: "))

# Ordem decrescente
lados = [A, B, C]
lados.sort(reverse=True) #Organiza do maior para o menor

A, B, C = lados  #garente que A é o maior

#Verificar os triangulos

if A >= B + C:
    print("NÃO FORMA TRIANGULO")
else:
    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")
    elif A**2 > B**2 + C**2:
        print("TRIANGULO OBTUSANGULO")
    elif A**2 < B**2 + C**2:
        print("TRIANGULO ACUTANGULO")

    if A == B == C:
        print("TRIANGULO EQUILATERO")
    elif A == B or A == C or B==C:
        print("TRIANGULO ISOSCELES")