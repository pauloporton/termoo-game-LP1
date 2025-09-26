import random
from checagem import its_green, its_yellow
from formatacao import red, green, yellow, formatar_tentativa, formatar_vazio, frase_estilizada
from base_palavras import palavras
from collections import Counter

def regras():
    # regras do jogo
    print(f"""Termoo é um jogo de adivinhação onde o objetivo é descobrir uma palavra de cinco letras em até seis tentativas. A cada palpite, o jogo fornece dicas através das cores:
        
{green('Verde')}: A letra está correta e na posição certa.

{yellow('Amarelo')}: A letra existe na palavra, mas está na posição errada.

{red('Vermelho')}: A letra não faz parte da palavra.""")
    

def valida_entrada():
    while True:
        tentativa = input('Digite uma palavra com 5 letras: ').lower()

        if len(tentativa) != 5 or not tentativa.isalpha():
            print(f'ERRO! A palavra deve ter 5 caracteres e ser composta apenas por letras sem acento.')
        else:
            return tentativa
   

def escolhe_palavra():
    palavra = random.choice(palavras)
    return palavra


# indica se a letra é verde, amarela ou vermelha
def testa_cores_letras(palavra_secreta, tentativa):
    cores_tentativa = ["", "", "", "", ""]
    contador_letras_secretas = Counter(palavra_secreta)

    for i in range(5):
        if its_green(i, palavra_secreta, tentativa):
            cores_tentativa[i] = green(tentativa[i])
            contador_letras_secretas[tentativa[i]] -= 1

    for i in range(5):
        if cores_tentativa[i] != "":
            continue

        if its_yellow(i, contador_letras_secretas, tentativa):
            cores_tentativa[i] = yellow(tentativa[i])
            contador_letras_secretas[tentativa[i]] -= 1
        else:
            cores_tentativa[i] = red(tentativa[i])

    return cores_tentativa


def entrada():
    print("""
============================
|      MENU PRINCIPAL      |
|--------------------------| 
|1 - Regras                |
|2 - Iniciar novo jogo     | 
|3 - Encerrar              |
============================""")
        
    resp = input('Escolha uma opção: ')
    print('============================')
    return resp


def main():
    print(f"""{frase_estilizada('PYTERMOO')}
    -> Criado por Paulo Porto e Artur Lucena""")
    while True:
        entrada1 = entrada()

        if entrada1 == '1':
            print(f'{frase_estilizada('regras')}')
            regras()

        elif entrada1 == '2':
            print(f'{frase_estilizada('jogo iniciado')}')
            print('=' * 21)
            print(formatar_vazio())
            print('=' * 21)

            # escolha da palavra a ser adivinhada
            palavra_secreta = escolhe_palavra()

            chances = 0
            max_tentativas = 6
            win = False

            while chances < max_tentativas and not win:
                # Bloco de validação de entrada
                tentativa = valida_entrada()
                
                # Apresenta o resultado formatado
                print('=' * 21)
                print(formatar_tentativa(testa_cores_letras(palavra_secreta, tentativa)))
                print('=' * 21)

                # Verifica a condição de vitória
                if tentativa == palavra_secreta:
                    win = True    

                chances += 1

            # Apresenta vitória
            if win:
                print(f'{frase_estilizada('voce venceu')}')    
                print(f'Você acertou a palavra: "{palavra_secreta}"')
            # Apresenta derrota
            else:
                print(f'{frase_estilizada('voce perdeu')}')
                print(f'A palavra era: "{palavra_secreta}"') 

        elif entrada1 == '3':
            print(f'{frase_estilizada('fim de jogo')}')
            print('Encerrando sessão...')
            break

        else:
            print('Por favor, digite uma opção válida.')


main()