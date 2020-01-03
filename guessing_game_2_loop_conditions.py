from random import randint
from turtle import *
import time


guesses = 1 #set guesses var to record a count of guess made by user
num = randint(1,100) #sets num var to a random integer using thr randit imported function
print("Let's play a number guessing game, but first, let me get some details!") #opening statement to user
time.sleep(3) #delays previous statement for 5 seconds
name = str(input("What is your name?")) #set name var to user input
print("Hi",name)
print(num)  
guess = int(input("guess a number between 1 and 100")) #set guess var to user input
if guess == num:
        print("good guess ",name,"!")
        print("you guessed in ",guesses, " attempts!")
        exit()
while guess != num:
    if guess > num:
        print("your guess is too high!")
        guess = int(input("guess again"))
        guesses = guesses + 1
    if guess < num:
        print("your guess is too low!")
        guess = int(input("guess again"))
        guesses = guesses + 1
    if guess == num:
        print("good guess ",name,"!")
        print("you guessed in ",guesses, " attempts!")
print("press F5 to play again, "+name+ "!")
