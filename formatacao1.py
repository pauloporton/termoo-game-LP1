# cores que serão utilizadas no jogo
r = "\033[31m"
g = "\033[32m"
y = "\033[33m"
reset = "\033[0m"

# funções formatação cores
def red(texto):
    return f'{r}{texto}{reset}'


def green(texto):
    return f'{g}{texto}{reset}'


def yellow(texto):
    return f'{y}{texto}{reset}'


# funções formatação das palabvras exibidas
def formatar_tentativa(palavra):
    return f'| {palavra[0]} | {palavra[1]} | {palavra[2]} | {palavra[3]} | {palavra[4]} |'


def formatar_vazio():
    return '|   |   |   |   |   |'


# função palavras estilizadas
def frase_estilizada(texto):
    if texto == 'PYTERMOO':
        return """ 
██████╗ ██╗   ██╗████████╗███████╗██████╗ ███╗   ███╗ ██████╗  ██████╗ 
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██╔═══██╗██╔═══██╗
██████╔╝ ╚████╔╝    ██║   █████╗  ██████╔╝██╔████╔██║██║   ██║██║   ██║
██╔═══╝   ╚██╔╝     ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║   ██║██║   ██║
██║        ██║      ██║   ███████╗██║  ██║██║ ╚═╝ ██║╚██████╔╝╚██████╔╝
╚═╝        ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝  ╚═════╝
        """
    elif texto == 'regras':
        return """ 
┏━┓┏━╸┏━╸┏━┓┏━┓┏━┓
┣┳┛┣╸ ┃╺┓┣┳┛┣━┫┗━┓
╹┗╸┗━╸┗━┛╹┗╸╹ ╹┗━┛
"""
    elif texto == 'jogo iniciado':
        return """ 
 ┏┓┏━┓┏━╸┏━┓   ╻┏┓╻╻┏━╸╻┏━┓╺┳┓┏━┓
  ┃┃ ┃┃╺┓┃ ┃   ┃┃┗┫┃┃  ┃┣━┫ ┃┃┃ ┃
┗━┛┗━┛┗━┛┗━┛   ╹╹ ╹╹┗━╸╹╹ ╹╺┻┛┗━┛
"""
    elif texto == 'voce venceu':
        return """
╻ ╻┏━┓┏━╸┏━╸   ╻ ╻┏━╸┏┓╻┏━╸┏━╸╻ ╻╻╻
┃┏┛┃ ┃┃  ┣╸    ┃┏┛┣╸ ┃┗┫┃  ┣╸ ┃ ┃╹╹
┗┛ ┗━┛┗━╸┗━╸   ┗┛ ┗━╸╹ ╹┗━╸┗━╸┗━┛╹╹
"""
    elif texto == 'voce perdeu':
        return """
╻ ╻┏━┓┏━╸┏━╸   ┏━┓┏━╸┏━┓╺┳┓┏━╸╻ ╻╻╻
┃┏┛┃ ┃┃  ┣╸    ┣━┛┣╸ ┣┳┛ ┃┃┣╸ ┃ ┃╹╹
┗┛ ┗━┛┗━╸┗━╸   ╹  ┗━╸╹┗╸╺┻┛┗━╸┗━┛╹╹
"""
    elif texto == 'fim de jogo':
        return """
┏━╸╻┏┳┓   ╺┳┓┏━╸    ┏┓┏━┓┏━╸┏━┓
┣╸ ┃┃┃┃    ┃┃┣╸      ┃┃ ┃┃╺┓┃ ┃
╹  ╹╹ ╹   ╺┻┛┗━╸   ┗━┛┗━┛┗━┛┗━┛
"""

    
    
