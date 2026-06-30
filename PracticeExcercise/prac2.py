import random

def guessing_game():
    secret= random.randint(1,100)
    attempts=0

    print('I am thinking of a number 1 to 100 ')

    while True:
        try:
            guess=int(input('your guess:'))
            attempts+=1

            if guess<secret:print('too low, try higher')
            elif guess>secret:print('too higher,try low')
            else:
                print(f'corret!you got it in {attempts} Attempts')
                break
        except ValueError:
            print('enter thw whole number')

guessing_game()
