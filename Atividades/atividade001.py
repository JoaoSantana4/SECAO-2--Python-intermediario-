#riar uma função que multiplica os args não nomeados recebidos
#retorne o total para uma variável e mostre o valor dela


def multiplicacao(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicar = multiplicacao(1, 2, 3, 4, 5)
print(multiplicar)