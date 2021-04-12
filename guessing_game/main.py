
from random import randint


def wants_play_again():
    user_input = input("Do you want to play again type yes/no: ").strip().lower()
    if user_input == "yes":
        return True
    else:
        return False


def guess_number_game():
    random_number = randint(1, 100)
    user_chances = 5

    print("-----------------------------")
    print("Welcome to the guessing game!")
    print("-----------------------------")

    while user_chances > 0:

        try:
            user_guess = int(input("Guess an integer: "))
        except ValueError:
            print("Invalid input. Please enter only numbers")
            continue

        if user_guess == random_number:
            print("You nailed it!")
            if wants_play_again():
                guess_number_game()
            else:
                break
        elif user_guess > random_number:
            print("Your guess is bigger than the answer")
            user_chances -= 1
            print(f"You have {user_chances} chances left \n")
        elif user_guess < random_number:
            print("Your guess is lower than the answer")
            user_chances -= 1
            print(f"You have {user_chances} chances left \n")

    if user_chances == 0:
        print("You lose :(")
        if wants_play_again():
            guess_number_game()


guess_number_game()