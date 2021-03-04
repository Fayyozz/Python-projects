import pandas

data_tb = pandas.read_csv("./nato_phonetic_alphabet.csv")
letter_codes_dict = {row.letter: row.code for (index, row) in data_tb.iterrows()}


def ask_user():
    user_word = input("Enter a word: ").upper()
    try:
        word_list = [letter_codes_dict[letter] for letter in user_word]
    except KeyError:
        print("Please only enter letters.")
        ask_user()
    else:
        print(word_list)


ask_user()


