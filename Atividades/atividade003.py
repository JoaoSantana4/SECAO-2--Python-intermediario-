# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

#Minha resolução

def calcular(numero1, numero2):
    return numero1 * numero2
    

multi = calcular(2, 2)
triplo = calcular(2, 3)
quadru = calcular(2, 4)

print(multi)
print(triplo)
print(quadru)


#Resolução do professor

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))