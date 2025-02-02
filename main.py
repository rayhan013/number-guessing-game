import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

level = input("Choose a difficulty. Type 'easy' or 'hard': ")

num = random.randint(1, 100)

print(num)

attempt = 10

if level == "easy":
    attempt = attempt - 0
elif level == "hard":
    attempt = attempt - 5
else:
    print("wrong input, The game started at Easy Level")


is_game_over = False

while not is_game_over:
    
    guess = int(input("Make a guess\n"))
    
    if guess != num:
        attempt -= 1
        if guess > num:
            print("Too High")
            print("Guess again")
        elif guess < num:
            print("Too low")
            print("Guess again")
        print(f"You have {attempt} attempts remaining to guess the number\n")
        
    if attempt == 0:
        is_game_over = True
        print(f"You've run out of guesses and the number was {num}")
    elif guess == num:
        is_game_over = True
        print("You won")
