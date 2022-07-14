print("Rock, Paper, Scissors, Shoot!")

import random

#User inputs

user_choice = input("Please make a choice('rock','paper','scissors'): ")
user_choice=user_choice.lower()
print("You chose: " + user_choice)


#Validate user inputs 

valid_options = ["rock" , "paper" , "scissors"]
if user_choice not in valid_options:
    print("Uh oh! That's not an option. Please try again.")
    exit()

#Computer choice

computer_choice = random.choice(['rock' , 'paper' , 'scissors'])
print("The computer chose: " + computer_choice)

#Determine the winner



#Display results 

#
# 
