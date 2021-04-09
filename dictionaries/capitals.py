import random


capitals_dict = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
}
list_of_state_capitals = list(capitals_dict.items())
state_capital = random.choice(list_of_state_capitals)


print("Welcome to guessing game! \n type exit to stop the game.")

go_on = True

while go_on:
    user_guess = input(f"Enter a capital of {state_capital[0]}:  ").lower().strip()
    if user_guess == state_capital[1].lower():
        print("Correct!")
        go_on = False
    elif user_guess == "exit":
        print(f"Correct answer was {state_capital[1].lower()}")
        go_on = False
    else:
        print("Incorrect guess! Try again")
        go_on = True






