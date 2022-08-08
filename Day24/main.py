# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"
namesList = []

with open("./Input/Names/invited_names.txt", 'r') as namesFile:
    for names in namesFile:
        namesList.append(names.strip())
    print(namesList)

with open("./Input/Letters/starting_letter.txt", 'r') as letterFile:
    letterContent = letterFile.read()
    for names in namesList:
        new_letter = letterContent.replace(PLACEHOLDER, names)
        letter_title = "Letter to " + names
        with open(f"./Output/ReadyToSend/{letter_title}", 'w') as file:
            file.write(new_letter)


