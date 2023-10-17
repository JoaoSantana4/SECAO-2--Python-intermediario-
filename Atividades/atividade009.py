"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
"""

lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]


def somar_lista(l1, l2):
    intervalo = min(len(l1), len(l2))
    return [(l1[i] + l2[i]) for i in range(intervalo)]

somar = somar_lista(lista_a, lista_b)
print(somar)


# lista_soma = []
# for i in range(len(lista_b)):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)

# lista_soma = []
# for i, _ in enumerate(lista_b):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)

#lista_a = [10, 2, 3, 40, 5, 6, 7]
#lista_b = [1, 2, 3, 4]
#lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
#print(lista_soma)