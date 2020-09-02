# Daniel's Hangman Game
import getpass, os, sys, re

def welcomeMessage():
    print("""
  _   _                   __  __             
 | | | | __ _ _ __   __ _|  \/  | __ _ _ __  
 | |_| |/ _` | '_ \ / _` | |\/| |/ _` | '_ \ 
 |  _  | (_| | | | | (_| | |  | | (_| | | | |
 |_| |_|\__,_|_| |_|\__, |_|  |_|\__,_|_| |_|
                    |___/                    
    """)


# Draws the board
def drawBoard():
    print("""
    |------|
    |      |
    |      O
    |     /|\ 
    |      |
    |     / \ 
    |      
   / \    
   """)



def main():
    if userInput.lower() == "q":
        sys.exit()

    elif userInput.lower() == "s":
        word = getpass.getpass("-\nEnter your word = ")
        os.system("clear")

        wordList = list(word.lower())
        lenWord = len(word.lower())
        guessedCount = 0
        lives = 7

        while True:
            userGuess = input("\nGuess a letter in the word, or the whole word = ")
            if userGuess.lower() == word:
                os.system("clear")
                print("""
                __   __           __        ___       _ 
                \ \ / /__  _   _  \ \      / (_)_ __ | |
                 \ V / _ \| | | |  \ \ /\ / /| | '_ \| |
                  | | (_) | |_| |   \ V  V / | | | | |_|
                  |_|\___/ \__,_|    \_/\_/  |_|_| |_(_)

                """)
                sys.exit()

            elif userGuess.lower() in wordList:
                os.system("clear")
                guessedCount = guessedCount + 1
                print("\nCorrect!")
                print("-\nLetters Guessed: " + str(guessedCount) + "/" + str(lenWord))
                wordList.pop(wordList.index(userGuess))

                if guessedCount == lenWord:
                    os.system("clear")
                    print("""
                    __   __           __        ___       _ 
                    \ \ / /__  _   _  \ \      / (_)_ __ | |
                     \ V / _ \| | | |  \ \ /\ / /| | '_ \| |
                      | | (_) | |_| |   \ V  V / | | | | |_|
                      |_|\___/ \__,_|    \_/\_/  |_|_| |_(_)
                                         
                    """)
                    sys.exit()

            else:
                os.system("clear")
                lives = lives - 1

                if lives == 0:
                    print("""
                    __   __            _              _   _ 
                    \ \ / /__  _   _  | |    ___  ___| |_| |
                     \ V / _ \| | | | | |   / _ \/ __| __| |
                      | | (_) | |_| | | |__| (_) \__ \ |_|_|
                      |_|\___/ \__,_| |_____\___/|___/\__(_)
                                         
                    """)
                    sys.exit()

                print("\nWrong! Try Again")

                # Draws the Hangman

                if lives == 6:
                    print("""
                     |------|
                     |      |
                     |      O
                     |     /|\ 
                     |      |
                     |     /
                     |      
                    / \    
                    """)

                if lives == 5:
                    print("""
                     |------|
                     |      |
                     |      O
                     |     /|\ 
                     |      |
                     |     
                     |      
                    / \    
                    """)

                if lives == 4:
                    print("""
                     |------|
                     |      |
                     |      O
                     |     /|\ 
                     |      
                     |     
                     |      
                    / \    
                    """)

                if lives == 3:
                    print("""
                     |------|
                     |      |
                     |      O
                     |     /|
                     |      
                     |     
                     |      
                    / \    
                    """)

                if lives == 2:
                    print("""
                     |------|
                     |      |
                     |      O
                     |      | 
                     |      
                     |     
                     |      
                    / \    
                    """)

                if lives == 1:
                    print("""
                     |------|
                     |      |
                     |      O
                     |      
                     |      
                     |     
                     |      
                    / \    
                    """)


            print("-\nLives: " + str(lives) + "/7")


# Introduction
welcomeMessage()
drawBoard()
userInput = input("Welcome to Daniels Text-Based Hangman Game!"
                  "\nEnter 'q' to quit or 's' to start = ")

if __name__ == "__main__":
    main()
