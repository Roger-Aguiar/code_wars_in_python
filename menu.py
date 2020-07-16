# Name:         Roger Silva Santos Aguiar
# Function:     This application has several codes implemented for the code wars.
# Initial date: July 13, 2020
# Last update:  July 16, 2020

# Required modules
import spin_words
import bit_counting

class Menu:
    def menu(self):
        print("\n******************************************************************************Menu******************************************************************************\n")
        print("1 - Spin Words")
        print("2 - Bit count")
        print("3 - Exit")
        print("\n****************************************************************************************************************************************************************")

    def runSpinWords(self):
        print("\n***************************************************************************Spin Words***************************************************************************")
        print("Hello! In this application, you enter some words, without punctuation, \nthen, the words that have 5 or more letters,"
              "will be spun and displayed in reverse order. Enter the following data:")
        sentence = input("\nPlease, enter a sentence without punctuation: ")
        print("Sentence typed: " + sentence)
        spin = spin_words.SpinWords()
        new_sentence = spin.spin_words(sentence)
        print("{} is equal to {} ." .format(sentence, new_sentence))
        print("\n****************************************************************************************************************************************************************")

    def run_bit_count(self):
        print("\n****************************************************************************Bit Count***************************************************************************")
        print("Hello! In this application, you enter an integer number, then, this number will be converted to binary,"
              "and it will display how many bits equal 1 this number has:")

        number = int(input("\nEnter an integer number: "))
        bit = bit_counting.BitCounting()
        bit.count_bits_equal_one(number)

        print("\n****************************************************************************************************************************************************************")

if __name__ == '__main__':
    runMenu = Menu()
    runMenu.menu()

    option = int(input("Please, choose an option: "))

    while option != 3:
        if option == 1:
            runMenu.runSpinWords()
            runMenu.menu()
        elif option == 2:
            runMenu.run_bit_count()
            runMenu.menu()

        option = int(input("Please, choose an option: "))

    if option == 3:
        print("End program.")