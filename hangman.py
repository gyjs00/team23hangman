import string

condition = False

print("Welcome to Hangman");
word = input("Hello Player 1! Please enter your word:\n")
word = word.upper()
word_length = len(word)


while not condition:
    guesses = input("Enter in the number of guesses for Player 2:\n")
    guesses = int(guesses)
    if guesses >= word_length:
        condition = True
    else:
        print("Not enough guesses for word length!")
        continue 
    

def hangman(word,guesses) :
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    guessed_letters = set()

    while (len(word_letters) > 0 and guesses >0):

        word_list = [letter if letter in guessed_letters else '_' for letter in word]
        print('Current word: ', ' '.join(word_list))

        player2_letter = input("Guess a letter:\n").upper()

        if player2_letter in alphabet - guessed_letters:
            guessed_letters.add(player2_letter)
            if player2_letter in word_letters:
                word_letters.remove(player2_letter)
                guesses = guesses - 1
                print("Correct.")
                print("NUMBER OF GUESSES LEFT: ", guesses,"\n")
            
            
            else:
                guesses = guesses - 1
                print("Incorrect. Letter is not in the word\n")
                print("NUMBER OF GUESSES LEFT: ", guesses,"\n")
               
        else:
            print("Invalid input.")
    

    if guesses == 0:
        print("NO MORE GUESSES")
    else:
        ("WON! The word was ", word)
  

hangman(word,guesses)


