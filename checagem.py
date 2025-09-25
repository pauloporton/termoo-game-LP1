contador_correct = {}
contador_guess = {}

def start(correct, guess):
    for ch in correct:
        if ch not in contador_correct:
            contador_correct[ch] = 1
        else:
            contador_correct[ch] += 1

    for ch in guess:
        if ch not in contador_guess:
            contador_guess[ch] = 1
        else:
            contador_guess[ch] += 1


def its_green(pos, correct, guess):
    if correct[pos] == guess[pos]:
        contador_correct[guess[pos]] -= 1
        contador_guess[guess[pos]] -= 1
        return True
    

def its_yellow(pos, correct, guess):
    contador_guess[guess[pos]] -= 1

    if (guess[pos] not in contador_correct) or (contador_correct[guess[pos]] == 0):
        return False
    else:
        contador_correct[guess[pos]] -= 1
        return True

