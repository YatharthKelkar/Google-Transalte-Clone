from googletrans import Translator, LANGUAGES

# Input prompts with corrected spelling
sourcelanguage = input("Please enter the language from which you are translating the text. ")
destlanguage = input("Please enter the language to which you are translating the text. ")
text = input("Please enter the text you want to translate. ")

# Create a Translator object
translator = Translator()

#language translation codes by this the user can easily acesses the languages
if sourcelanguage == "afrikaans":
    sourcelanguage = "af"

elif sourcelanguage == "hindi":
    sourcelanguage = "hi"

elif sourcelanguage == "marathi":
    sourcelanguage = "mr"   

elif sourcelanguage == "greek":
    sourcelanguage = "el"

elif sourcelanguage == "gujararti":
    sourcelanguage = "gu"    


if destlanguage == "afrikaans":
    destlanguage = "af"

elif destlanguage == "hindi":
    destlanguage = "hi"

elif destlanguage == "marathi":
    destlanguage = "mr"   

elif destlanguage == "greek":
    destlanguage = "el"

elif destlanguage == "gujararti":
    destlanguage = "gu"    

    # Translate the text
out = translator.translate(text, src=sourcelanguage, dest=destlanguage)
    
    # Output the translated text
print(out.text)

    # Print an error message if translation fails
print(f"An error occurred: {e}")
