itens = [('corda', 3, 8), 
         ('cantil', 1, 3), 
         ('barraca', 5, 12), 
         ('kit médico', 2, 6), 
         ('lanche', 4, 7)
         ]

peso_max = 10
melhor_valor = 0
combinacao = []

# parâmetros --> 
# k --> índice para acesso a lista
# peso_atual --> valor do peso dos itens até o momento
# valor_atual --> soma dos valores das utilidade
# lista --> lista dos itens escolhidos
def mochila(k, peso_atual, valor_atual, lista):
    global melhor_valor, combinacao

    if peso_atual > peso_max:
        return
    if k == len(itens):
        if valor_atual > melhor_valor:
            melhor_valor = valor_atual
            combinacao = lista[:]
        return

    # Não pega o item k
    mochila(k + 1, peso_atual, valor_atual, lista)

    # Pega o item k
    item = itens[k]
    lista.append(item)
    mochila(k + 1, peso_atual + item[1], valor_atual + item[2], lista)
    lista.pop()

# programa principal
mochila(0, 0, 0, [])

# exibe os resultados
print("Itens escolhidos:", ", ".join(i[0] for i in combinacao))
print("Peso total:", sum(i[1] for i in combinacao), "kg")
print("Valor total:", melhor_valor)