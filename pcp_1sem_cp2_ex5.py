#dados
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
renda = float(input("Digite sua renda mensal R$: "))
valor = float(input("Digite o valor desejado do empréstimo: "))
parcelas = int(input("Quantidade de parcelas (3 até 24): "))

#aprovação
def pode_aprovar(idade, renda, valor, parcelas):
    if idade < 18:
        return False, "Cliente menor de idade."

    if valor > renda * 20:
        return False, f"Valor maior que 20x a renda. Limite: {renda*20}"

    if parcelas < 3 or parcelas > 24:
        return False, "Parcelas devem estar entre 3 e 24."

    return True, "Aprovado"

aprovado, motivo = pode_aprovar(idade, renda, valor, parcelas)

if not aprovado:
    print(f"Empréstimo negado: {motivo}")
    exit()

#taxa de juros
def definir_taxa(parcelas):
    if parcelas <= 6:
        return 0.05
    elif parcelas <=12:
        return 0.08
    else:
        return 0.1

#calculo do financiamento
def calcular_parcela(valor, taxa, parcelas):
    if taxa == 0:
        return valor / parcelas
    return valor * (taxa * (1 + taxa)**parcelas) / ((1 + taxa)**parcelas - 1)

def calcular_total(parcela, parcelas):
    return parcela * parcelas

def calcular_juros(total, valor):
    return total - valor

taxa = definir_taxa(parcelas)
pmt = calcular_parcela(valor, taxa, parcelas)
total = calcular_total(pmt, parcelas)
juros = calcular_juros(total, valor)

#print
resultado = f"""
Empréstimo aprovado.
Cliente: {nome}
Valor financiado: {valor} R$
Taxa de juros aplicada: {taxa*100}%
Valor da parcela: {pmt:.2f} R$
Valor total pago: {total:.2f} R$
Total de juros pagos: {juros:.2f} R$
"""

print(resultado)