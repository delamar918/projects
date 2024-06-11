from replit import clear
import random
from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

display = []
for _ in range(word_length):
    display += "_"
    
guess_list = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    guess_list.append(f"{guess}")
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess_list.count(f"{guess}") > 1:
        print(f"You've already guessed {guess}")
      
    if guess not in chosen_word:

        lives -= 1
        if lives > 0:
            print(f"You've guessed {guess}. That's not in the word. You lose a life.")
        elif lives == 0:
            end_of_game = True
            print("You lose.")


    print(f"{' '.join(display)}")


    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
    
