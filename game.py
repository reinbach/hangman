#!/usr/bin/env python
# Hang Man
import random
import hangman
import sys

WORD_FILE = "words.txt"

def get_random_word():
    # usigin algorithm R(3.4.2) (Waterman's "Reservoir Algorithm")
    # from Knuth's "The Art of Computer Programming" (simplified version)
    #
    # get random word from word file
    # - ignore words that are less than 3 chars
    with open(WORD_FILE, "r") as fp:
        line = next(fp)
        for num, aline in enumerate(fp):
            if len(aline) <= 2 or random.randrange(num + 2):
                continue
            line = aline
        return line.strip()


def display_word(word, guessed_letters):
    # display word, by getting a list of chars in word
    # replacing unguessed chars with "_"
    # then checke whether the word has been solved
    # if so then success
    solved = False
    d = []
    for c in word:
        if c.lower() in guessed_letters:
            d.append(c)
        else:
            d.append("_")
    if "_" not in d:
        solved = True
        print("Congratulations, you solved it!  {0}".format(word))
    else:
        print("".join(d))
    return solved


def check_guess(word, guessed_letters, guess):
    #TODO ensure guess is a letter
    if len(guess) != 1:
        print("\nInvalid choice, try again")
        return
    guessed_letters.append(guess)
    if guess not in word:
        return draw_hangman(word, guessed_letters)
    return True


def draw_hangman(word, guessed_letters):
    # get count of guessed letters not in word
    # to determine hangman stage
    # if equal or greater than hangman stages
    # failed
    guess = True
    word_chars = set(word)
    failed_guesses = [x for x in guessed_letters if x not in word_chars]
    if len(failed_guesses) >= len(hangman.STAGES) - 1:
        print("Oh no... you failed to guess the letters")
        guess = False
    print(hangman.STAGES[len(failed_guesses)])
    return guess


def main():
    guessed_letters = []
    # get random word
    word = get_random_word()
    # display
    while not display_word(word, guessed_letters):
        # ask for letter
        guess = input("Next guess... ")
        # check letter
        if not check_guess(word, guessed_letters, guess):
            break
    # if solved word -> congrats
    # else draw next part of hangman
    # if completely drawn hangman -> fail
    again = input("Would you like to play again (y/n)...")
    while again.lower() not in ["y", "n"]:
        again = input("Need to select 'y' or 'n'")
    if again.lower() == "y":
        main()
    sys.exit(1)

if __name__ == "__main__":
    main()