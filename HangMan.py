import random
'''
This is my first simple python project.
This is HangMan.

Rules:
Guess the random word or the man hangs!

Game Loop:
I will show you the state of the current word.
Show you the wrong guesses.
Ask you to guess a letter
Check if its valid
Update correct/wrong guess
check win/loss condition
Show win/lose message
reveal the word
ask if you want to play again.
'''

#Create a list of secret words for the user to guess from.
words = ['Apple', 'Banana', 'Chicken', 'Knocked', 'Loose', 'Paleface', 'Swiss', 'Cheese', 'Innocent']

#Make it guess a random word each time
randword = random.choice(words)

#Make vars for guessed letters, wrong letters, max tries, tries left(lives)
guessed_letters = 0
wrong_letters = 0
max_tries = 8
lives = 4

#Show the current state of the word

#Show wrong guesses

#Ask the user to guess again

#check if the guess is valid

#update the correct/wrong guess

#check if win or less

#Show win/lose message

#Reveal the full word

#Ask if they want to play again.
