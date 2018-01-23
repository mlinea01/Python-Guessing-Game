import random

#Initializes variables for the players guess and number of guess to 0 to start the game.
#Sets the variable randomNumber to pick a random number at the start of the program that the user will have to guess.
randomNumber = random.randrange(1, 101)
playerGuess = 0
numberOfGuesses = 0

#This while loop will continue running until playerGuess is equal to the random number selected by the computer.
while playerGuess != randomNumber:
    playerGuess = int(input("Guess a number between 1 and 100"))

    #This variable will increase by 1 for every guess the user makes.
    #Every time the loop runs it will add one to the count.
    numberOfGuesses = numberOfGuesses + 1

    #This if statement will check if the number the user chose is less than the random number.
    #If the players guess is too low, it will print out Too low! Guess Again, allowing the user to guess another number.
    if playerGuess < randomNumber:
        print("Too low! Guess again.")

    #This if statement will check if the number the user chose is greater than the random number.
    #If the players guess is too high, it will print out Too high! Guess again, allowing the user to guess another number.
    elif playerGuess > randomNumber:
        print("Too high! Guess again.")

    #This else statement will check if the players guess is equal to the random number.
    #If the players guess is equal to the random number the loop will end.
    else:
        print("Correct!")

#After the user gets the correct number and loop ends, This line will print how many guess it took the user
#to get the correct answer.
print("It took  you ",numberOfGuesses," guesses.")
