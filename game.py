print("Welcome, Player One, to 'Rock, Paper, Scissors, Shoot!'")

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

#Determine the winner & display results

if user_choice==computer_choice:
    print("It's a tie! Please play again.")
    exit()

if user_choice=="rock" and computer_choice=="scissors":
    print("Rock crushes scissors. You win! Thanks for playing. Feel free to play again!")
    
if user_choice=="paper" and computer_choice=="rock":
    print("Paper covers rock. You win! Thanks for playing. Feel free to play again!")

if user_choice=="scissors" and computer_choice=="paper":
    print("Scissors cut paper. You win! Thanks for playing. Feel free to play again!")

if user_choice=="scissors" and computer_choice=="rock":
    print("Rock crushes scissors. You lose. Thanks for playing, try again!")
        
if user_choice=="rock" and computer_choice=="paper":
    print("Paper covers rock. You lose. Thanks for playing, try again!")

if user_choice=="paper" and computer_choice=="scissors":
    print("Scissors cut paper. You lose. Thanks for playing, try again!")
