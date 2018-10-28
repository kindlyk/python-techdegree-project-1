import random

guesses = []

def menu():
    print("*~*~*Welcome to Number Guessing game*~*~*")
    print("""
    Enter 'Quit' to end game at any time.
    Enter 'Help' for game instructions.
    """)
    
menu()

def help():
    print("""
    Choose a number between 1 and 10.
    Make sure to enter a whole number. For example, enter 5, not 5.0 or five.
    """)


def start_game():
    number = random.randint(1,10)
    count = 0
    while True:
        guess = input("Pick a number between 1 and 10:   ")
        if guess.upper() == 'QUIT':
            print("Sorry to see you go!")
            break
        elif guess.upper() == 'HELP':
            help()
        else:
            try:
                guess = int(guess)
            except Exception:
                print("Oops, try again. Make sure to enter a whole number.")
            else:
                if guess == number:
                    count += 1
                    guesses.append(count)
                    print("You got it! It took you {} tries.".format(count))
                    replay = input("Do you want to play again?(Y/N)   ")
                    if replay.upper() == 'Y':
                        print("Highest score is {}.".format(min(guesses)))
                        number = random.randint(1,10)
                        count = 0
                        continue
                    else:                        
                        print("Game over! See you next time.")
                        break
                elif guess <1 or guess > 10: 
                    print("Not a valid option - make sure to enter a number between 1 and 10.")
                    continue 
                elif guess > number:
                    count += 1
                    print("Try again - number is lower.")
                    continue
                elif guess < number:
                    count += 1
                    print("Try again - number is higher.")
                    continue 


if __name__ == '__main__':
    start_game()