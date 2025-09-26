def its_green(pos, correct, guess):
    if correct[pos] == guess[pos]:
        return True
    

def its_yellow(pos, tot_letras_correct, guess):
    if tot_letras_correct.get(guess[pos], 0) > 0:
        return True
    