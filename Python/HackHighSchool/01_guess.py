import random

moar_wordos = ("apple", "honey", "dough", "phone", "badge", "flame", "zebra", "focus", "space", "night", "cetus", "eagle", "ghost", "itchy", "jelly", "koala", "lemur", "monks", "nines", "oasdi", "queen", "racer", "stops", "taino", "uglis", "vigor", "water", "xiara", "yacht")
tisword = random.choice(moar_wordos)
ta_corrrect_word = tisword
real_correct = ta_corrrect_word

wguess = ''
lguess = ''
store = ''
ta_count = 0
limit = 10
random_letter = real_correct[0]

such_name = input("What's ur name? ")
print("Welcome to Python's guessing game!!!")
print("You have 10 attempts at guessing a word (Remember to split 10 different guesses into different lines!)")
print("Break your leg, " + such_name + "!")
print("And lets get ready to rrrrrrruuuuuuuuummmmmmmmmmmbbbbbbbbblllllllllleeeeeeeeee!!!!!!!!!")

for count_ta_guess in range(limit):
    while ta_count < limit:
        print("The secret word starts with " + random_letter + ": ")
        guess_the_word = input("GUESS: ")
        if len(guess_the_word) > 5:
            print("0, 1, 2, 3, 4, that's how we count to five!")
            limit -= 1
        elif guess_the_word == "":
            print("You wasted a guess :P")
        elif guess_the_word[0] not in str(random_letter):
            print("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            limit -= 1
        elif guess_the_word not in ta_corrrect_word:
            limit -= 1
            print("You have " + str(limit) + " guesses left!")

        if guess_the_word == ta_corrrect_word:
            break
    break

    if limit == 0:
        break

if guess_the_word == ta_corrrect_word:
    print("Good Job! You are one with the Source.")
else:
    print("Game over! You didn't guess it correctly!")