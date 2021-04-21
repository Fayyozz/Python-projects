import csv
from random import randint
from os import path


def update_leaderboard(attempts, user_name):
    if path.exists("leaderboard.csv"):
        leaderboard_data_list = []
        new_sorted_leaders = []
        with open("leaderboard.csv", "r") as leaderboard:
            leaderboard_data_list = [leader for leader in csv.DictReader(leaderboard)]
            leaderboard_data_list.append({"user_name": user_name, "attempts": attempts})
            users_with_scores = [(leader_data["user_name"], int(leader_data["attempts"])) for leader_data in
                                 leaderboard_data_list]

            users_with_scores.sort(key=lambda x: x[1])

            for item in users_with_scores:
                new_sorted_leaders.append({"user_name": item[0], "attempts": item[1]})

        with open("leaderboard.csv", "w") as csv_data:
            field_names = ["user_name", "attempts"]
            leaderboard_writer = csv.DictWriter(csv_data, fieldnames=field_names)
            leaderboard_writer.writeheader()
            for leader_data in new_sorted_leaders[:10]:
                leaderboard_writer.writerow(leader_data)

    else:
        with open("leaderboard.csv", "w") as csv_file:
            field_names = ["user_name", "attempts"]
            writer = csv.DictWriter(csv_file, fieldnames=field_names)
            writer.writeheader()
            writer.writerow({"user_name": user_name, "attempts": attempts})


def wants_play_again():
    user_input = input("Do you want to play again type yes/no: ").strip().lower()
    if user_input == "yes":
        return True
    else:
        return False


def print_leaders():
    if path.exists("leaderboard.csv"):
        with open("leaderboard.csv", "r") as data_file:
            leaders_data = csv.DictReader(data_file)
            for item in leaders_data:
                print(f"{item['user_name']} - {item['attempts']}")


def guess_number_game():

    print_leaders()

    random_number = randint(1, 100)
    user_attempts = 0

    print("-----------------------------")
    print("Welcome to the guessing game!")
    print("-----------------------------")
    user_name = input("Enter your Name: ")

    while user_attempts < 5:
        print(random_number)
        try:
            user_guess = int(input("Guess an integer: "))
        except ValueError:
            print("Invalid input. Please enter only numbers")
            continue

        if user_guess == random_number:
            update_leaderboard(user_attempts + 1, user_name)
            print("You nailed it!")
            if wants_play_again():
                guess_number_game()
            else:
                break
        elif user_guess > random_number:
            print("Your guess is bigger than the answer")
            user_attempts += 1
            print(f"You have attempted {user_attempts} times \n")
        elif user_guess < random_number:
            print("Your guess is lower than the answer")
            user_attempts += 1
            print(f"You have attempted {user_attempts} times \n")

    if user_attempts == 5:
        update_leaderboard(user_attempts, user_name)
        print("You lose :( \n You run out of your attempts")
        if wants_play_again():
            guess_number_game()


guess_number_game()

