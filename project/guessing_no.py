#Create a number guessing loop where the user keeps guessing until the correct number is entered
correct=9
guess=int(input("Guess the number : "))

while guess!= correct:
    print("Wrong guess!")
    guess=int(input("Guess again : "))

print("Hurry! Correct guess 🎉")
