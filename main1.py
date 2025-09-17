import random
import os
from checagem import its_green, its_yellow
from formatacao import red, green, yellow, formatar_tentativa, formatar_vazio, frase_estilizada


def escolha_palavras():
    palavras = ["sagaz", "termo", "mexer", "nobre", "senso", "afeto", "algoz", "plena", "fazer", "assim", "sobre", "vigor", "poder", "sutil", "fosse", "cerne", "ideia", "sanar", "audaz", "moral", "inato", "desde", "muito", "justo"]
    return random.choice(palavras)

def regras():

    print(f'{frase_estilizada('regras')}')
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
    |1 - Regras                |
    |2 - Iniciar novo jogo     | 
    |3 - Encerrar              |
    |4 - Entrar em novo jogo   |
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
    for i in range(len(palavra_secreta)): 
        if its_green(i, palavra_secreta, tentativa):
            cores_tentativa[i] = green(tentativa[i])
        elif its_yellow(i, palavra_secreta, tentativa):
            cores_tentativa[i] = yellow(tentativa[i])
        else:
            cores_tentativa[i] = red(tentativa[i])
    return cores_tentativa


def inicia_jogo():
    print(f'{frase_estilizada('jogo iniciado')}')
    print('=' * 21)
    print(formatar_vazio())
    print('=' * 21)


def main():
    # título e autores
    print(f"""{frase_estilizada('PYTERMOO')}
    -> Criado por Paulo Porto e Artur Lucena""")
    entrada1 = entrada()
    while entrada1 == '1':
        regras()
        entrada1 = entrada()
    
    if entrada1 == '4':
        id_jogo = input('Digite o ID do jogo criado. ')
        fifow2 = '/tmp/j2_fifo' + id_jogo
        os.mkfifo(fifow2)
        
        fifor2 = '/tmp/j1_fifo' + id_jogo

    while True:
        if entrada1 == '2':
            inicia_jogo()

            palavra_secreta = escolha_palavras()
            
            chances = 0
            max_tentativas = 6
            win = False
            while chances < max_tentativas and not win:
                tentativa = valida_tentativa()

                print('=' * 21)
                print(formatar_tentativa(testa_letras(palavra_secreta, tentativa)))
                print('=' * 21)

                if tentativa == palavra_secreta:
                    win = True    

                chances += 1

            if win:
                print(f'{frase_estilizada('voce venceu')}')    
                print(f'Você acertou a palavra: "{palavra_secreta}"')
                break
            else:
                print(f'{frase_estilizada('voce perdeu')}')
                print(f'A palavra era: "{palavra_secreta}"')
                break

        elif entrada1 == '3':
            print(f'{frase_estilizada('fim de jogo')}')
            print('Encerrando sessão...')
            break

        else:
            print('Por favor, digite uma opção válida.')

main()
