import random

words = ['apple', 'tiger', 'dance', 'smart', 'brave']
word = random.choice(words)
guesses = ''
turns = 6

print("Welcome to Hangman!")
while turns > 0:
    failed = 0
    display = ''
    for char in word:
        if char in guesses:
            display += char + ' '
        else:
            display += '_ '
            failed += 1
    print("\nWord: ", display.strip())

    if failed == 0:
        print("🎉 Congratulations! You guessed it right.")
        break

    guess = input("Guess a letter: ").lower()
    if guess in guesses:
        print("You already guessed that letter.")
    elif guess in word:
        print("✅ Good guess!")
        guesses += guess
    else:
        print("❌ Wrong guess!")
        turns -= 1
        guesses += guess
        print("Tries left:", turns)

    if turns == 0:
        print("💀 You lost! The word was:", word)
      
