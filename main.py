import random

def heads_tails():
    user_score = 0
    computer_score = 0
    options = ["Heads","Tails"]
    while user_score != 2 and computer_score != 2:
        choice = random.randint(0,1)
        computer_guess = options[choice]
        user_guess = str(input("Heads or Tails"))
        if user_guess == computer_guess:
            print("It was {}, you guessed {}, you won that round".format(computer_guess,user_guess))
            user_score += 1
        else: 
            print("It was {}, you guessed {}, you lost that round".format(computer_guess,user_guess))
            computer_score += 1
    #The loop has now ended and it will output won the best of 3 rounds
    if user_score == 2:
        print("{}, you won that game".format(first_name))
    else:
        print("{}, you lost that game".format(first_name))

#main program
print("Hi! Welcom to my Heads or Tails game")
first_name = str(input("What is your name"))
age = int(input("What is your age"))
heads_tails() #This calls up the function