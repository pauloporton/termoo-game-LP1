import random
from checagem import its_green, its_yellow, start
from formatacao import red, green, yellow, formatar_tentativa, formatar_vazio, frase_estilizada
from base_palavras import palavras

# título e autores
print(f"""{frase_estilizada('PYTERMOO')}
-> Criado por Paulo Porto e Arthur Lucena""")

while True:
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

    if resp == '1':
        print(f'{frase_estilizada('regras')}')
        # regras do jogo
        print(f"""Termoo é um jogo de adivinhação onde o objetivo é descobrir uma palavra de cinco letras em até seis tentativas. A cada palpite, o jogo fornece dicas através das cores:
            
    {green('Verde')}: A letra está correta e na posição certa.

    {yellow('Amarelo')}: A letra existe na palavra, mas está na posição errada.

    {red('Vermelho')}: A letra não faz parte da palavra.""")

    elif resp == '2':
        print(f'{frase_estilizada('jogo iniciado')}')
        print('=' * 21)
        print(formatar_vazio())
        print('=' * 21)

        # escolha da palavra a ser adivinhada
        palavra_secreta = random.choice(palavras)

        chances = 0
        max_tentativas = 6
        win = False

        while chances < max_tentativas and not win:
            # Bloco de validação de entrada
            while True: 
                tentativa = input('Digite uma palavra com 5 letras: ').lower()

                if len(tentativa) != 5:
                    print(f'ERRO! A palavra deve ter 5 letras.')
                elif not tentativa.isalpha():
                    print('ERRO! Digite apenas letras.')
                else:
                    break # A entrada é válida, sai do loop de validação

            cores_tentativa = ["", "", "", "", ""]

            start(palavra_secreta,tentativa)

            for i in range(len(palavra_secreta)): # indica se a letra é verde, amarela ou vermelha
                if its_green(i, palavra_secreta, tentativa):
                    cores_tentativa[i] = green(tentativa[i])

            for i in range(len(palavra_secreta)):
                if its_yellow(i, palavra_secreta,tentativa) and cores_tentativa[i] == "":
                    cores_tentativa[i] = yellow(tentativa[i])
                elif cores_tentativa[i] == "":
                    cores_tentativa[i] = red(tentativa[i])
            

            # Apresenta o resultado formatado
            print('=' * 21)
            print(formatar_tentativa(cores_tentativa))
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

    elif resp == '3':
        print(f'{frase_estilizada('fim de jogo')}')
        print('Encerrando sessão...')
        break

    else:
        print('Por favor, digite uma opção válida.')
