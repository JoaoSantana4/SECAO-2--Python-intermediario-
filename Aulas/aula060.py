# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
caminho_arquivo = 'C:\\Users\\joaov\\OneDrive\\Imagens\\Nova pasta Atenção\\'
caminho_arquivo += 'aula060.txt'


#arquivo = open(caminho_arquivo, 'w')
# 
#arquivo.close()

nomes = ['Joao', 'Maria']

with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(('Linha 3\n', 'Linha 4\n'))
    arquivo.seek(0, 0)
    print(arquivo.read())
    print('Lendo')
    arquivo.seek(0, 0)
    print(arquivo.readline().strip()) #funciona como um next
    print(arquivo.readline(), end= '') #readline está retornando uma str, então eu consigo usar funções para str
    print(arquivo.readline().strip()) #.strip e end= '' são funções que removem os espaços, quebras de linhas são espaços
    print(arquivo.readline().strip())

    print('READLINES')
    arquivo.seek(0, 0)
    for linha in arquivo.readlines():
        print(linha.strip())



print('#' * 40)


with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())