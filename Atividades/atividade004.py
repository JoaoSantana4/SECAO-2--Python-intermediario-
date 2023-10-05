# Exercício - sistema de perguntas e respostas

#Minha resolução

import emoji

pergunta_1 = {
    'Pergunta': 'Quanto é 2+2?',
    'Opções': ['1', '3', '4', '5'],
    'Resposta': '4',
}


pergunta_2 = {
    'Pergunta': 'Quanto é 5*5?',
    'Opções': ['25', '55', '10', '51'],
    'Resposta': '25',
}


pergunta_3 = {
    'Pergunta': 'Quanto é 10/2?',
    'Opções': ['4', '5', '2', '1'],
    'Resposta': '5',
}


menu_do_jogo = input('Você quer jogar o jogo da advinhação? [s]im ou [n]ão: ')


def jogo_1():
    global guarda_resposta
    guarda_resposta = 0
    indice = 0
    print('Qual a resposta correta para a seguinte pergunta: ')
    print(pergunta_1['Pergunta'])
    for resposta in (pergunta_1['Opções']):
        print(indice,')', resposta)
        indice += 1
    resposta_pergunta_1 = input('DIGITE O INDICE DA RESPOSTA CORRETA: ')
    while resposta_pergunta_1 is not None:
        if resposta_pergunta_1 == '2':
            print(emoji.emojize('RESPOSTA CORRETA ✅'))
            break
        elif resposta_pergunta_1 == '0':
            print('RESPOSTA ERRADA')
            break
        elif resposta_pergunta_1 == '1':
            print('RESPOSTA ERRADA')
            break
        elif resposta_pergunta_1 == '3':
            print('RESPOSTA ERRADA')
            break
        else:
            print('DIGITE UM VALOR VÁLIDO!')
            break
    if resposta_pergunta_1 == '2':
        guarda_resposta +=1
    else:
        guarda_resposta == guarda_resposta
    return


def jogo_2():
    global guarda_resposta
    indice_2 = 0
    print('Qual a resposta correta para a seguinte pergunta: ')
    print(pergunta_2['Pergunta'])
    for resposta in (pergunta_2['Opções']):
        print(indice_2,')', resposta)
        indice_2 += 1
    resposta_pergunta_2 = input('DIGITE O INDICE DA RESPOSTA CORRETA: ')
    while resposta_pergunta_2 is not None:
        if resposta_pergunta_2 == '0':
            print('RESPOSTA CORRETA ✅')
            break
        elif resposta_pergunta_2 == '2':
            print('RESPOSTA ERRADA ❌')
            break
        elif resposta_pergunta_2 == '1':
            print('RESPOSTA ERRADA ❌')
            break
        elif resposta_pergunta_2 == '3':
            print('RESPOSTA ERRADA ❌')
            break
        else:
            print('DIGITE UM VALOR VÁLIDO!')
            break
    if resposta_pergunta_2 == '0':
        guarda_resposta +=1
    else:
        guarda_resposta == guarda_resposta
    return


def jogo_3():
    global guarda_resposta
    indice_3 = 0
    print('Qual a resposta correta para a seguinte pergunta: ')
    print(pergunta_3['Pergunta'])
    for resposta in (pergunta_3['Opções']):
        print(indice_3,')', resposta)
        indice_3 += 1
    resposta_pergunta_3 = input('DIGITE O INDICE DA RESPOSTA CORRETA: ')
    while resposta_pergunta_3 is not None:
        if resposta_pergunta_3 == '1':
            print('RESPOSTA CORRETA ✅')
            break
        elif resposta_pergunta_3 == '0':
            print('RESPOSTA ERRADA ❌')
            break
        elif resposta_pergunta_3 == '2':
            print('RESPOSTA ERRADA ❌')
            break
        elif resposta_pergunta_3 == '3':
            print('RESPOSTA ERRADA ❌')
            break
        else:
            print('DIGITE UM VALOR VÁLIDO! ❌')
            break
    if resposta_pergunta_3 == '1':
        guarda_resposta +=1
    else:
        guarda_resposta == guarda_resposta
    return

if menu_do_jogo == 's':
   jogo_1()
   jogo_2()
   jogo_3()
   if guarda_resposta > 0:
       print(f'PARABÉNS VOCÊ ACERTOU {guarda_resposta} PERGUNTAS! 🥇')
   else:
       print('VOCÊ ERROU TODAS AS PERGUNTAS! 😵')
       

elif menu_do_jogo == 'n':
    print('Ok')
    exit

else:
    print('Por favor, digite um digito válido!')

