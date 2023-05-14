"""Guessing Game """

def guess_the_number(number: int) ->int:
    """This function is where the guessing happens
    
    Keyword arguments:
    argument -- the number the user guessed
    Return: returns if the user guessed the right number
    """

    ACTUAL_NUMBER = 48
    
    if number > ACTUAL_NUMBER:
        print(f"The guessed number {number} is greater than the Actual Number")
        return False
    elif number < ACTUAL_NUMBER:
        print(f"The guessed number {number} is less than the Actual Number")
        return False
    else:
        return True

def play_game() ->any:

    while True:
        number_guessed = int(input("Guess the number! "))
        if guess_the_number(number_guessed):
            break
    return f" {number_guessed} is the correct Guess"


print(play_game())