def recomendar_plano(consumo_mensal):

    if consumo_mensal <= 10:
        return "Plano Essencial Fibra - 50Mbps: Recomendado para um consumo médio de até 10 GB."
    elif 10 < consumo_mensal <= 20:
        return "Plano Prata Fibra - 100Mbps: Recomendado para um consumo médio acima de 10 GB até 20 GB."
    else:
        return "Plano Premium Fibra - 300Mbps: Recomendado para um consumo médio acima de 20 GB."
    
consumo = float(input("Por favor, insira o seu consumo médio mensal de dados em GB: "))
plano_recomendado = recomendar_plano(consumo)
print(plano_recomendado)