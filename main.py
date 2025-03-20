#TODO: Create a letter using starting_letter.txt
with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()

with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()

# print(names)
updated_names =[]
for name in names:
    new_name = name.strip("\n")
    updated_names.append(new_name)

# print(updated_names)

#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
for name in updated_names:
    new_letter = letter.replace("[name]",name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode  = 'w') as file:
        file.write(new_letter)


#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp