student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
#print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# user_input = input("Write a word: ").upper()


def generate_alpha():
    user_word = input("Write a word: ").upper()
    try:
        user_input_list = [nato_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_alpha()
    else:
        print(user_input_list)

generate_alpha()

