from random import randint
from turtle import *

guesses = 1
num = randint(1,100)
name = str(input("What is your name?"))
guess = int(input("guess a number between 1 and 100"))

while guess != num:
    if guesses >10:
        print("Too many guesses "+ name+", game over!")
        break
    if guess > num:
        print("your guess is too high!")
        guess = int(input("guess again"))
        guesses = guesses + 1
    if guess < num:
        print("your guess is too low!")
        guess = int(input("guess again"))
        guesses = guesses + 1
    if guess == num:
        print("good guess "+name+"!")
        print("you guessed in ",guesses, " attempts!")
        forward(100)
        right(120)
        forward(100)
        right(120)
        forward(100)
print("press F5 to play again!")
