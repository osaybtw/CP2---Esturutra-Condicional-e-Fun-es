Código_origem = int(input("Digite o código de origem da carga (1 a 5): "))
Código_da_carga = int(input("Digite o código da sua carga: "))
Peso_carga = float(input("Digite o peso da sua carga em Toneladas: "))

print(f'Seu código de origem é: {Código_origem}')
print(f'O código da sua carga é: {Código_da_carga}')
print(f'O peso da sua carga é em toneladas: {Peso_carga}T')
Pcakg = Peso_carga * 10 ** 3
print(f'O peso da sua carga em quilos é de:{Pcakg}kg ')

if 10 <= Código_da_carga <= 20:
    PporKg = 100
    print(f'Seu código da carga é {Código_da_carga} e o preço por kg é R$100,00')
elif 21 <= Código_da_carga <= 30:
    PporKg = 250
    print(f'Seu código da carga é {Código_da_carga} e o preço por kg é R$250,00')
elif 31 <= Código_da_carga <= 40:
    PporKg = 340
    print(f'Seu código da carga é {Código_da_carga} e o preço por kg é R$340,00')

preco_carga = Pcakg * PporKg
print(f'Preço total da carga: R$ {preco_carga:.2f}')

if Código_origem == 1:
    imposto_percentual = 0.35
elif Código_origem == 2:
    imposto_percentual = 0.25
elif Código_origem == 3:
    imposto_percentual = 0.15
elif Código_origem == 4:
    imposto_percentual = 0.05
else:  # Código_origem == 5
    imposto_percentual = 0
valor_imposto = preco_carga * imposto_percentual

print(f'Imposto (estado {Código_origem}): {imposto_percentual * 100}% = R$ {valor_imposto:.2f}')
valor_total = preco_carga + valor_imposto
print(f'VALOR TOTAL TRANSPORTADO: R$ {valor_total:.2f}')