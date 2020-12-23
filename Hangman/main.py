import random
import hangman_words
import hangman_art 

print(hangman_art.logo)
print("\n")

word_list = hangman_words.word_list
stages = hangman_art.stages

chosen_word = random.choice(word_list)

end_of_game = False
lives = 6

display = []
for blank in range(len(chosen_word)):
  display += "_"
print(display)

while not end_of_game:
  print("\n")
  guess = input("Guesss a Word.\t").lower()
 


  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
  
  if guess not in chosen_word:
    lives -= 1

  
  print(' '.join(display))

  print(stages[lives])
  print(display)
  if "_" not in display:
    end_of_game = True
    print("You win.")
  elif lives == 0:
    end_of_game = True
    print("Game Over,You lose.")


