def its_green(pos, correct, guess):
    if correct[pos] == guess[pos]:
        return True
    

def its_yellow(pos, correct, guess):
    for j in range(len(correct)):
        if correct[j] == guess[pos] and correct[j] != guess[j]:
            return True

