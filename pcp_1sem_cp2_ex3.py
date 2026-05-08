NotasCp = []
NotasCp.append(float(input("Digite sua nota do Checkpoint 1:")))
NotasCp.append(float(input("Digite sua nota do Checkpoint 2:")))
NotasCp.append(float(input("Digite sua nota do Checkpoint 3:")))
NotasCp.sort(reverse=True)
NotaCp1 = NotasCp[0]
NotaCp2 = NotasCp[1]
NotaCp3 = NotasCp[2]
print(f"Suas notas são {NotaCp1}, {NotaCp2} e sua menor nota é {NotaCp3} e vai ser desconsiderada.")
print()
NotasSp = []
NotasSp.append(float(input("Digite sua nota do Sprint 1:")))
NotasSp.append(float(input("Digite sua nota do Sprint 2:")))
NotasSp.sort(reverse=True)
NotaSp1 = NotasSp[0]
NotaSp2 = NotasSp[1]
print(f"Suas notas são {NotaSp1} e {NotaSp2}")
print()
NotaGS = float(input("Digite a nota da sua Global Solution: "))
print()

print("---------------MÉDIAS---------------")
med1sempeso = (NotaCp1 + NotaCp2 + NotaCp3 - NotaCp3 + NotaSp1 + NotaSp2) / 4
print(f'A média 1 sem peso é de: {med1sempeso:.2f}')
med1compeso = (med1sempeso * 0.4)
print(f'A média 1 com peso é de: {med1compeso:.2f} ')
med1final = med1compeso + (NotaGS * 0.6)
print(f'Sua média final é de: {med1final:.1f}')
