import random
from checagem import its_green, its_yellow, start
from formatacao import red, green, yellow, formatar_tentativa, formatar_vazio, frase_estilizada
from base_palavras import palavras
def regras():
        # regras do jogo
    print(f"""Termoo é um jogo de adivinhação onde o objetivo é descobrir uma palavra de cinco letras em até seis tentativas. A cada palpite, o jogo fornece dicas através das cores:
        
{green('Verde')}: A letra está correta e na posição certa.

{yellow('Amarelo')}: A letra existe na palavra, mas está na posição errada.

{red('Vermelho')}: A letra não faz parte da palavra.""")
    

def valida_entrada(palavras):
    tentativa = input('Digite uma palavra com 5 letras: ').lower()
    while True:
        if len(tentativa) != 5 or not tentativa.isalpha() or tentativa not in palavras:
            print(f'ERRO! A palavra deve ter 5 caracteres e ser composta apenas por letras sem acento.')
            tentativa = input('Digite uma palavra com 5 letras: ').lower()
        else:
            return tentativa
    

def escolhe_palavra():
    palavra = random.choice(palavras)
    return palavra

def testa_cores_letras(palavra_secreta, tentativa):
    cores_tentativa = ["", "", "", "", ""]
    start(palavra_secreta,tentativa)

    for i in range(5): # indica se a letra é verde, amarela ou vermelha
        if its_green(i, palavra_secreta, tentativa):
            cores_tentativa[i] = green(tentativa[i])

    for i in range(5):
        if its_yellow(i, palavra_secreta,tentativa) and cores_tentativa[i] == "":
            cores_tentativa[i] = yellow(tentativa[i])

        elif cores_tentativa[i] == "":
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
    -> Criado por Paulo Porto e Arthur Lucena""")
    entrada1 = entrada()

    if entrada1 == '1':
        while True:
            regras()
            entrada1 = entrada()
            if entrada != '1':
                break


    if entrada1 == '2':
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
            tentativa = valida_entrada(palavras)
    
            
            # Apresenta o resultado formatado
            print('=' * 21)
            print(formatar_tentativa(testa_cores_letras(palavra_secreta, tentativa)))
            print('=' * 21)

            # Verifica a condição de vitória
            if tentativa == palavra_secreta:
                win = True    

            chances += 1

        if win:
            print(f'{frase_estilizada('voce venceu')}')    
            print(f'Você acertou a palavra: "{palavra_secreta}"')
        else:
            print(f'{frase_estilizada('voce perdeu')}')
            print(f'A palavra era: "{palavra_secreta}"') 

    elif entrada1 == '3':
        print(f'{frase_estilizada('fim de jogo')}')
        print('Encerrando sessão...')

    else:
        print('Por favor, digite uma opção válida.')

main()
