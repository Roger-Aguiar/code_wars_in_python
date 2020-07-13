# Name:         Roger Silva Santos Aguiar
# Function:     This application takes in a string of one or more words,
#               and returns the same string, but with all five or more letter
#               words reversed
# Initial date: July 13, 2020
# Last update:  July 13, 2020

class SpinWords:
    def __init__(self, sentence):
        self.sentence = sentence

    def spinWords(self):
        sentence = self.sentence.split(" ")
        spunWords = ""

        for word in sentence:
            if len(word) >= 5:
                currentWord = []
                lengthWord = 0
                while lengthWord < len(word):
                    currentWord.append(word[lengthWord])
                    lengthWord = lengthWord + 1
                currentWord.reverse()

                for newLetter in currentWord:
                    spunWords = spunWords + newLetter
                spunWords = spunWords + " "
            else:
                spunWords = spunWords + word + " "
        return  spunWords

if __name__ == '__main__':
    words = input("Please, enter one or more words: ")
    print("Typed words: " + words)

    spin = SpinWords(words)
    spunWords = spin.spinWords()

    print("Spun words: " + spunWords)