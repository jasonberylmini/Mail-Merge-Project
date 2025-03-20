# PLACE_HOLDER = "[name]"
# #Create a letter using starting_letter.txt
# with open("./Input/Names/invited_names.txt") as file:
#     names = file.readlines()
#
#
# #for each name in invited_names.txt
# with open("./Input/Letters/starting_letter.txt") as file:
#     letter_contents = file.read()
#     for name in names:
#         new_name = name.strip()
#         # Replace the [name] placeholder with the actual name.
#         new_letter = letter_contents.replace(PLACE_HOLDER, new_name)
#         # Save the letters in the folder "ReadyToSend".
#         with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", mode='w') as new_file:
#             new_file.write(new_letter)


from docx import Document

PLACE_HOLDER = "[name]"

# Read all names
with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()

# Read the letter template
with open("./Input/Letters/starting_letter.txt") as file:
    letter_contents = file.read()

# Generate proper Word documents
for name in names:
    new_name = name.strip()
    new_letter = letter_contents.replace(PLACE_HOLDER, new_name)

    # Create a new Word document
    doc = Document()
    doc.add_paragraph(new_letter)

    # Save as a proper .docx file
    doc.save(f"./Output/ReadyToSend/letter_for_{new_name}.docx")

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp