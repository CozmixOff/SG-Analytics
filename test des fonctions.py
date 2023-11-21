import random

def typeur (L):
    typevalue_L = []
    for i in range(len(L)):
        if L[i] not in typevalue_L:
            typevalue_L.append(L[i])
    return sorted(typevalue_L)

def transformateur (L):
    typevalue_L = typeur(L)
    transfo_L = []
    for i in L: 
        x = typevalue_L.index(i)
        transfo_L.append(x)
    
    return transfo_L

liste = list([random.randint(0,100) for i in range(500)])
print(typeur(liste).sort())