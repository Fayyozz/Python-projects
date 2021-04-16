# this is the binary search algorithm implementation in python


# parameters range for the problem
# commands to enter to the problem: lower, higher and right from the user

min_value = int(input("Enter min value for the range:  "))
max_value = int(input("Enter max value for the range:  "))

print(f"Please think of any number between {min_value} and {max_value} inclusive")

print("You will enter L if my guess is lower than the answer")
print("You will enter H if my guess is higher than the answer")
print("You will enter R if my guess is right than the answer")


def search(min_v, max_v, number_of_guesses):
    lst_numbers = []
    for n in range(min_v, max_v + 1):
        lst_numbers.append(n)
    lst_numbers.sort()

    guess_index = len(lst_numbers) // 2 
    guess_number = lst_numbers[guess_index]

    print(f"my guess is {guess_number}")
    result = input("is it correct ? Enter L/H/R ").strip().upper()

    if result == "R":
        print(f"Yahoo, I got it right in {number_of_guesses} guesses")
    elif result == "H":
        search(lst_numbers[0], lst_numbers[guess_index], number_of_guesses + 1)
    elif result == "L":
        search(lst_numbers[guess_index], lst_numbers[-1], number_of_guesses + 1)


num_guesses = 1
search(min_value, max_value, num_guesses)

