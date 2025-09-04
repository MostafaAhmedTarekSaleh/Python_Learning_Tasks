import random as R
"""
Thought Process:
one list for secretwords and one list for guesses -> this one is the progress display
one counter for guessesleft
"""
secret_words = ["Most","Mohtady","Yasser","MMU"]

chosen_s_word= list(R.choice(secret_words) .lower())

guess_list = []
guesses_left = 6

print("Welcome to Hangman Game")
for letter in chosen_s_word:
    guess_list.append("_")

print(guess_list)

while(guesses_left > 0 and guess_list !=chosen_s_word):
    letter_guess = input("\nPlease enter your letter guess:\n").lower()
    if letter_guess in chosen_s_word:-
        position = -1
        for letter in chosen_s_word:
            position+=1
            if letter == letter_guess:
                guess_list[position] = letter_guess

        print(guess_list)

    else:
        guesses_left -=1
        print(guess_list)

if guess_list == chosen_s_word:
    print("You won!")
else:
    print("Out of guesses , you lost!")





def comp_play():
    in_row = R.randint(1,3)
    in_col = R.randint(1,3)
    if grid[in_row - 1][in_col - 1] == " ":
        grid[in_row - 1][in_col - 1] = "O"
    else:
        comp_play()

checkinput()
display()
comp_play()
display()