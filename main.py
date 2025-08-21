'''
    author: Thisun
    date: 22/08/2025
    version: 1.0.0
    description: A heads or tails guessing game.
'''
#-----------------libraries-------------------------------
import random
#-----------------functions-------------------------------
#This functions chooses heads or tails and asks the user to make a guess.
def heads_tails():
    user_score = 0
    computer_score = 0
    options = ["Heads","Tails"]
    while (user_score != 2 and computer_score != 2):
        choice = random.randint(0,1)
        computer_guess = options[choice]
        user_guess = str(input("Heads or Tails: "))
        if user_guess == computer_guess:
            print("It was {}, you guessed {}, you won that round".format(computer_guess,user_guess))
            user_score += 1
        else: 
            print("It was {}, you guessed {}, you lost that round".format(computer_guess,user_guess))
            computer_score += 1
    #The loop has now ended and it will output won the best of 3 rounds
    if (user_score == 2):
        print("{}, you won that game".format(first_name))
    else:
        print("{}, you lost that game".format(first_name))

#Forces the user to enter a valid name
def force_name():
    name = input("What is your name? ").strip() #takes initial input
    MIN_NAME_LENGTH = 2
    MAX_NAME_LENGTH = 10
    while len(name) < MIN_NAME_LENGTH or len(name) > MAX_NAME_LENGTH: #repeats until name has valid length
        name = input("Invalid name length. Please enter a valid name: ") #asks for input repetedly
    return name #returns the valid name

#-----------------main program-----------------------
print("Hi! Welcome to my Heads or Tails game")
first_name = force_name() #gets name using force_name
age = int(input("What is your age? "))
heads_tails() #This calls up the function