import pandas

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
phonetics_df = pandas.read_csv('nato_phonetic_alphabet.csv')
phonetics_dict = {row.letter:row.code for (index, row) in phonetics_df.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetics():
    try:
        input_word = input("Enter a word: ").upper()
        phonetics_list = [phonetics_dict[letter] for letter in input_word]
    except KeyError:
        print("Alphabetic characters only please")
        generate_phonetics()
    else:
        print(phonetics_list)

generate_phonetics()