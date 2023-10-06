# Exemplo de uso dos sets
#letras = set()
#while True:
#    letra = input('Digite: ')
#    letras.add(letra.lower())
#   if 'l' in letras:
#        print('PARABÉNS')
#       break
#
#    print(letras)



#Jogo da advinhação da palavra

palavras = set()

while True:
    print('JOGO DA ADVINHAÇÃO!')
    print('ADVINHE A PALAVRA SEGUINDO A SEGUINTE DICA: É UM ANIMAL')
    palavra = input('Digite uma palavra: ')
    palavras.add(palavra.lower())

    if 'macaco' in palavra:
        print('PARABÉNS')
        break

    print(palavras)