'''
Utility functions for Mastermind puzzles.
'''

'''
This function compares a guess and a code and returns (numCorrect, numTransposed)
which correspond to the number of colored and white pegs returned in Mastermind.
'''
def evaluate_guess(guess, code):
	# Get the length n of the guess and the code.
    assert(len(guess) == len(code))
    n = len(guess)

    # Determine the correct and incorrect positions.
    correct_positions = [i for i in list(range(n)) if guess[i] == code[i]]
    incorrect_positions = [i for i in list(range(n)) if guess[i] != code[i]]
    num_correct = len(correct_positions)

    # Reduce the guess and the code by removing the correct positions.
    # Create the set values that are common between the two reduced lists.
    reduced_guess = [guess[i] for i in incorrect_positions] 
    reduced_code = [code[i] for i in incorrect_positions]
    reduced_set = set(reduced_guess) & set(reduced_guess)

    # Determine the number of transposed values.
    num_transposed = 0
    for x in reduced_set:
    	num_transposed += min(reduced_guess.count(x), reduced_code.count(x))

    return num_correct, num_transposed





if __name__ == "__main__":
    guess = [1,1,2,2]
    secret_code = [1,2,3,4]
    num_correct, num_transposed = evaluate_guess(guess, secret_code)
    print("secret code: "+ str(secret_code))
    print("guess: " + str(guess))
    print(str(num_correct) + " black peg(s) and " + str(num_transposed) + " white peg(s)")



