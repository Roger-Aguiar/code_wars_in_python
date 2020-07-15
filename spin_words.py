# Name:         Roger Silva Santos Aguiar
# Function:     This application takes in a string of one or more words,
#               and returns the same string, but with all five or more letter
#               words reversed
# Initial date: July 13, 2020
# Last update:  July 15, 2020

class SpinWords:
    def spin_words(self, sentence):
        words = sentence.split()
        newSentence = ''

        for word in words:
            if len(word) >= 5:
                spin_word = self.reverse_word(word)
                newSentence = newSentence + ' ' + spin_word
            else:
                newSentence = newSentence + ' ' + word

        newSentence = newSentence.strip()
        return newSentence

    def reverse_word(self, word):
        spin_word = ''

        for caracter in word:
            spin_word = caracter + spin_word

        return spin_word

if __name__ == '__main__':
    sentence = input("Please, enter one or more words: ")
    print("Typed words: " + sentence)

    spin = SpinWords()
    new_sentence = spin.spin_words(sentence)

    print("{} is equal to {} ." .format(sentence, new_sentence))