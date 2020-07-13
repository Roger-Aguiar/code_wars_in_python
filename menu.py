# Name:         Roger Silva Santos Aguiar
# Function:     This application has several codes implemented for the code wars.
# Initial date: July 13, 2020
# Last update:  July 13, 2020

# Required modules
import spin_words

class Menu:
    def menu(self):
        print("\n******************************************************************************Menu******************************************************************************\n")
        print("1 - Spin Words")
        print("2 - Exit")
        print("\n****************************************************************************************************************************************************************")

    def runSpinWords(self):
        print("\n***************************************************************************Spin Words***************************************************************************")
        print("Hello! In this application, you enter some words, without punctuation, \nthen, the words that have 5 or more letters,"
              "will be spun and displayed in reverse order. Enter the following data:")
        sentence = input("\nPlease, enter a sentence without punctuation: ")
        print("Sentence typed: " + sentence)
        spin = spin_words.SpinWords(sentence)
        spunWords = spin.spinWords()
        print("Spun words: " + spunWords)
        print("\n****************************************************************************************************************************************************************")

if __name__ == '__main__':
    runMenu = Menu()
    runMenu.menu()

    option = int(input("Please, choose an option: "))

    while option == 1:
        runMenu.runSpinWords()
        runMenu.menu()
        option = int(input("Please, choose an option: "))

    if option == 2:
        print("End program.")