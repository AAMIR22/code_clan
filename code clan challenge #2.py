#Quick Note:
#We used the 'random' library to generate a random guess.
#function guess_number is used to perform the task.
#'while not' loop gives the user multiple chances until they succeed.
#'if-else' statements make this program a bit more interactive.
#This program adds a playful twist by having the program suggest its own random guess, making the game more interactive.
#If the user guesses the program's number but it's not correct, a humorous message is displayed to keep the user engaged.
#The playful comments and teasing add an element of fun to the guessing game, making it more entertaining.


import random


def guess_number():
    number_to_guess = random.randint(1, 10)
    program_guess = random.randint(1, 10)
    attempts = 0
    correct_guess = False

    print("I'm thinking of a number between 1 and 10. Can you guess it?")
    print(f"\nPssst... I think the number might be {program_guess}. But can you trust me? 😉")

    while not correct_guess:
        guess = int(input("What's your guess?: "))
        attempts += 1

        if guess == program_guess and guess != number_to_guess:
            print("Haha, you guessed my number, but it's not the correct one!")

        if guess < number_to_guess:
            print("Oops! Too low. Try again.")
        elif guess > number_to_guess:
            print("Yikes! Too high. Give it another go.")
        else:
            if attempts > 2:
                print(f"\nHmm... Not bad! Try to get within 2 attempts. The number was {number_to_guess} and it took you {attempts} tries.")
            else:
                print(f"\nBravo! You nailed it. The number was {number_to_guess} and it took you {attempts} tries.")
            if guess == program_guess:
                print("This time you got it... but remember, never trust anyone...even me! 😜")
            else:
                print("Remember, never trust anyone...even me! 😜")
            correct_guess = True


guess_number()
