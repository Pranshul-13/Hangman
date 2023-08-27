'''

for ... range(n):
	task


for .. list:
	task







names = []

while (True):
	name = input('Enter name : ')
	names.append(name)
	print()
	option = input('Do you want to add more names ? (y/n) : ')

	if(option == 'n'):
		break
	elif(option == 'y'):
		continue

print(names)




'''






import random

def play(word):                       

  display_word = '_' * len(word)              
  count = 0                              
  lives = 5                              

  while count < lives:                   

      guess = input(f'Hangman Word: {display_word} Enter your guess: \n') 

      if guess in word:                                             
          index = word.index(guess)                                    
          display_word = display_word[:index] + guess + display_word[index + 1:]      

      else:
          count += 1
          
          if count == 1:
              print('   _____ \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '__|__\n')
              print(f'Wrong guess.\n Guesses remaining: {lives - count}\n')

          elif count == 2:
              print('   _____ \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '__|__\n')
              print(f'Wrong guess.\n Guesses remaining: {lives - count}\n')

          elif count == 3:
              print('   _____ \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '__|__\n')
              print(f'Wrong guess.\n Guesses remaining: {lives - count}\n')

          elif count == 4:
              print('   _____ \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     O \n'
                    '  |      \n'
                    '  |      \n'
                    '__|__\n')
              print(f'Wrong guess.\n Guesses remaining: {lives - count}\n')

          elif count == 5:
              print('   _____ \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     O \n'
                    '  |    /|\ \n'
                    '  |    / \ \n'
                    '__|__\n')
              print('Wrong guess. You\'ve been hanged!!!\n')
              print(f'The word was: {word}')

      if display_word == word:
          print(f'Congratulations! You have guessed the corect word.')
          break





print('Welcome to the Hangman Game\n')
name = input('Enter your name: ')
print(f'Hello {name}! \nLet\'s get started -')

words_to_guess = [
    "apple",
    "dog",
    "cat",
    "book",
    "tree",
    "mountain",
    "ocean",
    "car",
    "house",
    "sun",
    "moon",
    "flower",
    "river",
    "computer",
    "friend",
    "city",
    "child",
    "song",
    "bird",
    "time"
]


while True:
       word = random.choice(words_to_guess)
       play(word)
       option = input('\nPlay again? (y/n) :')
       if(option=='n'):
       	   break