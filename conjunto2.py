
def gerar_subconjuntos(lista):
    n = len(lista)
    for mascara in range(1 << n): 
        subconjunto = []
        for i in range(n):
            if mascara & (1 << i): 
                subconjunto.append(lista[i])
        print(subconjunto)

gerar_subconjuntos([1, 2, 3])
