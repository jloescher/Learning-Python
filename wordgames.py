import random


def getRandomWord():
    words = ["pizza", "cheese", "apples"]
    word = words[random.randint(0, len(words)-1)]
    return word


def showWord(word):
    for character in word:
        print(character, " ", end='')
    print("")


def getGuess():
    print("Enter a letter: ")
    return input()


def processLetter(letter, secret_word, blanked_word):
    result = False

    for i in range(0, len(secret_word)):
        if secret_word[i] == letter:
            result = True
            blanked_word[i] = letter

    return result


def printStrikes(number_of_strikes):
    for i in range (0, number_of_strikes):
        print("X ", end='')
    print("")


def playWordGame():
    strikes = 0
    max_strikes = 3
    playing = True

    word = getRandomWord()
    blanked_word = list("_" * len(word))

    while playing:
        showWord(blanked_word)
        letter = getGuess()
        found = processLetter(letter, word, blanked_word)

        if not found:
            strikes += 1
            printStrikes(strikes)

        if strikes >= max_strikes:
            playing = False

        if not "_" in blanked_word:
            playing = False

    if strikes >= max_strikes:
        print("Loser!")
    else:
        print("Winner!")


print("Game started")
playWordGame()
print("Game over")