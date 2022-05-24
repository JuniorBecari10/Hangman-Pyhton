import random
from os import name, system

def get_random_word():
    file = open("words.txt")
    f = file.readlines()[0]
    w = f.split(" ")
    i = random.randrange(0, len(w) - 1)
    
    return w[i][:-1]

def clear():
    # for windows
    if name == 'nt':
        system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        system('clear')

def hang(guess):
    if len(guess) != 1:
        return False
    
    if guess in word:
        return True
    
    return False

def print_letters(word, guesses):
    for i in range(len(word)):
        if i in guesses:
            print(word[i], end=" ")
        else:
            print("_", end=" ")
    print("\n")

################################################

word = get_random_word()
guessed_indexes = []
chances = 8

def main():
    global chances
    
    while True:
        clear()
        print("Hangman Game\n")
        
        print_letters(word, guessed_indexes)
        
        print("Chances:", chances)
        
        if chances == 0:
            print("You lost. The word was " + word + ".")
            
            break
        
        inp = input("Enter your guess (Just press Enter to try the entire word): ")
        
        if inp == "":
            inp = input("Enter the word (if you miss, you lose): ")
            
            if inp != word:
                print("You lost. The word was " + word + ".")
                
                break
        
        if len(inp) != 1:
            continue
        
        if hang(inp):
            guessed_indexes.append(word.index(inp))
        else:
            chances = chances - 1

main()
