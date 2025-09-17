import random
import os
from checagem1 import its_green, its_yellow
from formatacao1 import red, green, yellow, formatar_tentativa, formatar_vazio, frase_estilizada


def cria_ids():
    lista = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    return random.choice(lista) + random.choice(lista) + random.choice(lista) + random.choice(lista) + random.choice(lista)

def escolha_palavras():
    palavras = ["sagaz", "termo", "mexer", "nobre", "senso", "afeto", "algoz", "plena", "fazer", "assim", "sobre", "vigor", "poder", "sutil", "fosse", "cerne", "ideia", "sanar", "audaz", "moral", "inato", "desde", "muito", "justo"]
    return random.choice(palavras)

def regras():

    print(f'{frase_estilizada("regras")}')
    # regras do jogo
    print(f"""Termoo é um jogo de adivinhação onde o objetivo é descobrir uma palavra de cinco letras em até seis tentativas. A cada palpite, o jogo fornece dicas através das cores:
            
    {green('Verde')}: A letra está correta e na posição certa.

    {yellow('Amarelo')}: A letra existe na palavra, mas está na posição errada.

    {red('Vermelho')}: A letra não faz parte da palavra.""")

def entrada():

    print("""
    ============================
    |      MENU PRINCIPAL      |
    |--------------------------| 
    |1 - Iniciar novo jogo     |
    |2 - Entrar em novo jogo   | 
    |3 - Encerrar              |
    |4 - Regras                |
    ============================""")
        
    resp = input('Escolha uma opção: ')
    print('============================')
    return resp


def valida_tentativa():
        while True: 
            tentativa = input('Digite uma palavra com 5 letras: ').lower()

            if len(tentativa) != 5:
                print(f'ERRO! A palavra deve ter 5 letras.')
            elif not tentativa.isalpha():
                print('ERRO! Digite apenas letras.')
            else:
                return tentativa

def testa_letras(palavra_secreta, tentativa):
    cores_tentativa = ['', '', '', '', '']
    contador = 0
    for i in range(len(palavra_secreta)): 
        if its_green(i, palavra_secreta, tentativa):
            cores_tentativa[i] = green(tentativa[i])
            contador += 1
        elif its_yellow(i, palavra_secreta, tentativa):
            cores_tentativa[i] = yellow(tentativa[i])
        else:
            cores_tentativa[i] = red(tentativa[i])
    return cores_tentativa, contador

def faz_fifow(codigo, jogador):
    fifow = '/tmp/j' + jogador + '_fifo' + codigo
    os.mkfifo(fifow)

    print('O ID da sua partida é ', codigo)
    return fifow


def leitor_fifor(jogador, codigo):
    if jogador == '1':
        inverso = '2'
    else:
        inverso = '1'
    fifor = '/tmp/j' + inverso + '_fifo' + codigo
    return fifor



def inicia_jogo(codigo, jogador):
    print(f'{frase_estilizada("jogo iniciado")}')
    print('=' * 21)
    print(formatar_vazio())
    print('=' * 21)
    
    return faz_fifow(codigo, jogador)


def main():
    # título e autores
    print(f"""{frase_estilizada('PYTERMOO')}
    -> Criado por Paulo Porto e Artur Lucena""")
    entrada1 = entrada()
    while entrada1 == '4':
        regras()
        entrada1 = entrada()

    while True:
   
        if entrada1 == '1':
            id_partida = cria_ids()
            fifow = inicia_jogo(id_partida, entrada1)
            fifor = leitor_fifor(entrada1, id_partida)

        elif entrada1 == '2':
            id_partida = input('Digite o ID da partida. ')
            fifow = inicia_jogo(id_partida, entrada1)
            fifor = leitor_fifor(entrada1, id_partida)

        elif entrada1 == '3':
            print(f'{frase_estilizada("fim de jogo")}')
            print('Encerrando sessão...')
            break
        else:
            print('Por favor, digite uma opção válida.')
        if entrada1 == '1':
            palavra_secreta = escolha_palavras()
            with open(fifow, 'w') as fifo:
                fifo.write(palavra_secreta)
        else:
            with open(fifor, 'r') as fifo:
                palavra_secreta = fifo.read()

        chances = 0
        max_tentativas = 6
        win = False
        while chances < max_tentativas and not win:
            tentativa = valida_tentativa()

            print('=' * 21)
            print(formatar_tentativa(testa_letras(palavra_secreta, tentativa)[0]))
            print('=' * 21)
            quantidade_letras = testa_letras(palavra_secreta, tentativa)[1]   
            if entrada1 == '1':
                with open(fifow, 'w') as fifo:
                    fifo.write(f'Seu adversário acertou {formatar_tentativa(quantidade_letras)} !')
                
                with open(fifor, 'r') as fifo:
                    print(fifo.read())

            else:
                with open(fifow, 'r') as fifo:
                    print(fifo.read())
                
                with open(fifow, 'r') as fifo:
                    fifo.write(f'Seu adversário acertou {formatar_tentativa(quantidade_letras)} !')

            if tentativa == palavra_secreta :
                win = True    

            chances += 1

        if win:
            print(f'{frase_estilizada("voce venceu")}')    
            print(f'Você acertou a palavra: "{palavra_secreta}"')
            with open(fifow, 'w'):
                fifo.write('perdeu')
            break
        elif not win or fifor.read() == 'perdeu':
            print(f'{frase_estilizada("voce perdeu")}')
            print(f'A palavra era: "{palavra_secreta}"')
            break
        
    os.remove(fifow)
    

main()
