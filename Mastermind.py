import utils as u
import numpy as np
import itertools
import copy

def create_S(colors, rowLength):
    '''
    Creates the set S of all possible 1296 codes. A "code" is a list of integers, where each integer denotes a different color.
    This will be used for STEP 1 (see main function).

    @param colors: the number of different colors for a ball (can be 6, is 8 in some variations).
    @param rowLength: the size of a row on the board (most often 4).
    @return: the set S
    '''
    S = [list(x) for x in itertools.product(range(1,colors+1), repeat=rowLength)]
    return S

def knuth(guess, answer):
    '''
    Runs Knuth's five guess algorithm. Source: https://en.wikipedia.org/wiki/Mastermind_(board_game)#Five-guess_algorithm

    @param guess: the current guess to be played.
    @param answer: the secret code.
    '''

    global S #Initializes S
    print guess

    #STEP 3: Plays the guess to get a response
    (guess_correct, guess_transposed) = u.evaluate_guess(guess, answer)

    #STEP 4: If the response is 4 colored pegs, we have acheieved the secret code.
    if guess_correct  == len(guess):
        return

    #STEP 5: Remove from S any code that would not give the same response if it were the code.
    #In other words, only keep the codes which will return the same pin configuration if they were the answer.
    S = [S[i] for i in range(len(S)) if u.evaluate_guess(guess,S[i]) == (guess_correct, guess_transposed)]


    #STEP 6: Minimax Technique for next guess:

    S_guessSet.remove(guess) #Keeps only unused codes.

    score_array = []
    for code_1 in S_guessSet:
        hitcounts = [] #Will count "hitcounts," or the number of elements deleted for a peg configuration.
        pegComb = [0,0] #Initial peg configuration
        while pegComb[0] != len(guess):
            hitcount = 0
            for code_2 in S:
                (code_correct, code_transposed) = u.evaluate_guess(code_1, code_2)
                if (code_correct,code_transposed) != tuple(pegComb): #For the current peg configuration, this code will be deleted from S. We increase hitcount.
                    hitcount += 1
            hitcounts.append(hitcount)

            #Finds next peg configuration
            if pegComb[0] + pegComb[1] == len(guess): #The sum of the number of the two pegs cannot be greater than 4.
                pegComb[0] += 1
                pegComb[1] = 0
                continue
            if pegComb[1] + 1 > len(guess): #The peg configuration numbers cannot be greater than 4.
                pegComb[0] += 1
                pegComb[1] = 0
                continue
            pegComb[1] += 1

        score_array.append(min(hitcounts)) #The minimum of the hitcounts of each peg configuration for a guess becomes the "score" of the guess. We append the score to score_array.

    guess_index = np.argmax(score_array) #Find the index of the maxiumum score.
    next_guess = S_guessSet[guess_index] #S_guessSet is indexed similarly; we choose the code associated with the maxium score.

    #STEP 7: Repeat from STEP 3.
    knuth(next_guess,answer)

if __name__ == "__main__":
    colors = 6 #Number of colors is 6
    rowLength = 4 #A row on the board has 4 slots.

    #STEP 1: Create the set of all possible codes. Create a copy from which only used guesses will be removed.
    S = create_S(colors,rowLength)
    S_guessSet = copy.deepcopy(S)

     #STEP 2: Initial guess must always be [1,1,2,2]
    initial_guess = [1,1,2,2]
    secret_code = [6,5,6,5] #The secret code

    #STEPS 3-7
    knuth(initial_guess,secret_code)
