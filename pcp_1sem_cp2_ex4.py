def exibir_menu_cargos():
    """Exibe o menu de cargos."""
    print("\n" + "=" * 50)
    print("SELECIONE O CARGO:")
    print("1 - Gerente")
    print("2 - Analista")
    print("3 - Assistente") 
    print("4 - Estagiário")
    print("=" * 50)

def obter_cargo():
    """Valida e retorna o cargo selecionado."""
    while True:
        try:
            exibir_menu_cargos()
            opcao = int(input("Digite o numero do cargo: "))
            if opcao in [1, 2, 3, 4]:
                return opcao
            else:
                print("Opcao invalida! Escolha 1, 2, 3 ou 4.")
        except ValueError:
            print("Digite apenas numeros!")

def calcular_horas_extras(salario_base, horas_extras):
    """
    Calcula o valor das horas extras.
    Valor hora extra = 1.5% do salario base por hora
    """
    if horas_extras <= 0:
        return 0.0
    valor_hora_extra = salario_base * 0.015  # 1.5%
    return valor_hora_extra * horas_extras

def calcular_descontos_faltas(salario_base, faltas):
    """
    Calcula desconto por faltas.
    2% do salario base por falta
    """
    if faltas <= 0:
        return 0.0
    return salario_base * 0.02 * faltas

def calcular_bonus(cargo, recebeu_bonus):
    """
    Calcula bonus por desempenho baseado no cargo.
    """
    if recebeu_bonus.lower() != 's':
        return 0.0
    
    bonus_por_cargo = {
        1: 1000.0,  # Gerente
        2: 500.0,   # Analista
        3: 300.0,   # Assistente
        4: 100.0    # Estagiario
    }
    return bonus_por_cargo.get(cargo, 0.0)

def coletar_dados_funcionario():
    """Coleta todos os dados do funcionario com validacao."""
    print("CADASTRO DE FUNCIONARIO")
    print("-" * 30)
    
    # Nome
    nome = input("Nome completo: ").strip().title()
    
    # Cargo
    cargo = obter_cargo()
    cargos = {1: "Gerente", 2: "Analista", 3: "Assistente", 4: "Estagiario"}
    
    # Salario base
    while True:
        try:
            salario_base = float(input("Salario base (R$): "))
            if salario_base > 0:
                break
            print("Salario deve ser maior que zero!")
        except ValueError:
            print("Digite um valor numerico valido!")
    
    # Horas extras
    while True:
        try:
            horas_extras = float(input("Horas extras trabalhadas: "))
            if horas_extras >= 0:
                break
            print("Horas extras nao podem ser negativas!")
        except ValueError:
            print("Digite um numero valido!")
    
    # Faltas
    while True:
        try:
            faltas = int(input("Total de faltas no mes: "))
            if faltas >= 0:
                break
            print("Faltas nao podem ser negativas!")
        except ValueError:
            print("Digite um numero inteiro valido!")
    
    # Bonus
    while True:
        bonus = input("Recebeu bonus por desempenho? (s/n): ").lower().strip()
        if bonus in ['s', 'n']:
            break
        print("Digite apenas 's' ou 'n'!")
    
    return {
        'nome': nome,
        'cargo': cargo,
        'cargo_nome': cargos[cargo],
        'salario_base': salario_base,
        'horas_extras': horas_extras,
        'faltas': faltas,
        'bonus': bonus
    }

def calcular_folha_pamento(dados):
    """Calcula todos os valores da folha de pagamento."""
    salario_base = dados['salario_base']
    
    horas_extras_valor = calcular_horas_extras(salario_base, dados['horas_extras'])
    descontos_faltas = calcular_descontos_faltas(salario_base, dados['faltas'])
    bonus_valor = calcular_bonus(dados['cargo'], dados['bonus'])
    
    salario_bruto = salario_base + horas_extras_valor + bonus_valor
    total_acrescimos = horas_extras_valor + bonus_valor
    total_descontos = descontos_faltas
    salario_final = salario_bruto - total_descontos
    
    return {
        'salario_bruto': salario_bruto,
        'total_acrescimos': total_acrescimos,
        'total_descontos': total_descontos,
        'salario_final': salario_final,
        'horas_extras_valor': horas_extras_valor,
        'bonus_valor': bonus_valor,
        'descontos_faltas': descontos_faltas
    }

def exibir_holerite(dados_funcionario, folha):
    """Exibe o resultado da folha de pagamento."""
    print("\n" + "=" * 50)
    print("HOLERITE - FOLHA DE PAGAMENTO")
    print("=" * 50)
    print(f"Funcionario: {dados_funcionario['nome']}")
    print(f"Cargo: {dados_funcionario['cargo_nome']}")
    print("-" * 40)
    
    print(f"Salario Base:         R$ {dados_funcionario['salario_base']:>8.2f}")
    print(f"Horas Extras:         R$ {folha['horas_extras_valor']:>8.2f}")
    print(f"Bonus:                R$ {folha['bonus_valor']:>8.2f}")
    print(f"Desconto por Faltas:  R$ {folha['descontos_faltas']:>8.2f}")
    print("-" * 40)
    print(f"Salario Bruto:        R$ {folha['salario_bruto']:>8.2f}")
    print(f"SALARIO FINAL:        R$ {folha['salario_final']:>8.2f}")
    print("=" * 50)

# EXECUCAO PRINCIPAL
def main():
    """
    Funcao principal do sistema.
    Permite calcular folha de pagamento para multiplos funcionarios.
    """
    while True:
        dados = coletar_dados_funcionario()
        folha = calcular_folha_pamento(dados)
        exibir_holerite(dados, folha)
        
        print("\n" + "=" * 50)
        continuar = input("Calcular outro funcionario? (s/n): ").lower().strip()
        if continuar != 's':
            print("Fim do processamento.")
            break
        print()

if __name__ == "__main__":
    main()
