import random

def play(word):
    # Setup initial game state
    display_word = ['_'] * len(word)
    lives = 5
    guessed_letters = set()
    hangman_stages = [
        '''
           _____ 
          |     
          |     
          |     
          |     
          |     
          |     
        __|__
        ''',
        '''
           _____ 
          |     | 
          |     | 
          |      
          |      
          |      
          |      
        __|__
        ''',
        '''
           _____ 
          |     | 
          |     | 
          |     | 
          |      
          |      
          |      
        __|__
        ''',
        '''
           _____ 
          |     | 
          |     | 
          |     | 
          |     O 
          |      
          |      
        __|__
        ''',
        '''
           _____ 
          |     | 
          |     | 
          |     | 
          |     O 
          |    /|\\ 
          |    / \\ 
        __|__
        '''
    ]

    print(f"\n{' '.join(display_word)}")
    
    while lives > 0:
        guess = input("\nEnter your guess: ").strip().lower()

        # Validate single letter input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        # Check for repeated guesses
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        # Add to guessed letters set
        guessed_letters.add(guess)

        # Correct guess
        if guess in word:
            for i, char in enumerate(word):
                if char == guess:
                    display_word[i] = guess

            print("\n" + ' '.join(display_word))

            # Check for win
            if ''.join(display_word) == word:
                print(f"\n🎉 Congratulations! You guessed the correct word: {word}")
                break
        # Incorrect guess
        else:
            lives -= 1
            print(hangman_stages[5 - lives])  # Show the current hangman stage
            print(f"Wrong guess. Guesses remaining: {lives}\n")

        # Game over
        if lives == 0:
            print(f"💀 Game over! The word was: {word}")

# Game Introduction
print("Welcome to the Hangman Game\n")
name = input("Enter your name: ")
print(f"Hello {name}! Let's get started.")

# Word bank
words_to_guess = [
    "apple", "dog", "cat", "book", "tree", "mountain", "ocean",
    "car", "house", "sun", "moon", "flower", "river", "computer",
    "friend", "city", "child", "song", "bird", "time"
]

# Main game loop
while True:
    word = random.choice(words_to_guess)
    play(word)
    option = input("\nPlay again? (y/n): ").strip().lower()
    if option == 'n':
        print("\nThanks for playing! Goodbye!")
        break
