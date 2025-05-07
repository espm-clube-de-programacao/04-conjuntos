itens = [('corda', 3, 8), 
         ('cantil', 1, 3), 
         ('barraca', 5, 12), 
         ('kit médico', 2, 6), 
         ('lanche', 4, 7)
         ]

n = len(itens)
peso_max = 10
melhor_combinacao = []
melhor_peso = 0
melhor_valor = 0

for mascara in range(1 << n): # 1 * 2^n
    peso_total = 0
    valor_total = 0
    combinacao = []
    for i in range(n):
        if mascara & (1 << i):
            nome, peso, valor = itens[i]
            peso_total += peso
            valor_total += valor
            combinacao.append(nome)
    
    if peso_total <= peso_max and valor_total > melhor_valor:
        melhor_valor = valor_total
        melhor_peso = peso_total
        melhor_combinacao = combinacao[:]
        
print(f'itens escolhidos: {melhor_combinacao}')
print(f'peso total: {melhor_peso} kg')
print(f'valor total: {melhor_valor}')