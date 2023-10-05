from translate import Translator

print("Welcome to Translator.py.")

while True:

    Lang_ISO = input("Please enter the ISO code you wish to use (Ex: zh, sk, etc): ")
    translator = Translator(to_lang=Lang_ISO)
    sentence = input("Please enter the sentence you'd like to translate: ")
    translation = translator.translate(sentence)

    print(translation)
    answer = input("Would you like to translate another sentence? (Y/N) ")
    if answer == "N":
        break
    elif answer == "Y":
        continue
    else:
        print("Invalid command. Only accept Y or N.")

