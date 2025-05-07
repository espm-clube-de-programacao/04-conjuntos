
def gerar_subsets(conjunto, k=0, atual=[]):
    if k == len(conjunto):
        print(atual)
        return
 
    gerar_subsets(conjunto, k+1, atual)
    gerar_subsets(conjunto, k+1, atual + [conjunto[k]])
    
# programa principal
gerar_subsets([1, 2, 3])