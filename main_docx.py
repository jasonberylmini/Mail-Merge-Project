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