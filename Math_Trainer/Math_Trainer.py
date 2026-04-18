# Import necessary libraries for randomness, OS operations, and time tracking
import random
import os
import time

# Display a welcome message and instructions for the game
print("========================================================")
print("            Welcome to the Math Trainer!  ")
print("========================================================")

print ("Get ready to challenge your math skills and have fun! 🎉")
print("Instructions: Solve the math problem and earn points! You have 3 lives")
print("Good luck! 🍀")

# Initialize game variables for points, level, lives, and consecutive correct answers
points = 0
level = 1
lives = 3
Consecutive_correct_answers = 0

# Record the start time of the game to implement a time limit for each level
start_game_time = time.time()

# Main game loop that continues until the player runs out of lives
while lives > 0:
    if level == 1: time_limit = 20
    elif level == 2: time_limit = 30
    elif level == 3: time_limit = 60
    elif level == 4: time_limit = 80
    else: time_limit = 80

# Calculate the elapsed time and remaining time for the current level
    elapsed_time = time.time() - start_game_time
    remaining_time = time_limit - elapsed_time 
    
    # Display the remaining time to the player
    if remaining_time <= 0:
        print("\nTime's up! ⏰")
        break # 

   # Generate random numbers based on current level difficulty
    num1 = random.randint(1, 10 * level)
    num2 = random.randint(1, 10 * level)
    opperation = random.choice(['+', '-', '*'])

# Determine the operation based on the current level
    if level == 1: 
         opperation = '+'     
    elif level == 2:
        opperation = '-'
    elif level == 3:
        opperation ='*'
    elif level == 4:
        opperation = '/'
    else:
        opperation = 'x'
        
    if opperation == '+':
        correct_answer = num1 + num2

    elif opperation == '-':
          correct_answer = num1 - num2

    elif opperation == '*':
                    correct_answer = num1 * num2

        # For division, we want to ensure that the division is clean (no remainders) and that we don't divide by zero       
    elif opperation == '/':
                    correct_answer = num1 
                    num1 = num1 * num2 

                  # For the 'x' operation, we will solve for x in the equation x + num1 = num1 + num2, which simplifies to x = num2  
    elif opperation == 'x':
                    correct_answer = num2
                   
# Display the current level, points, and lives to the player
    print(f"Level: {level} / Points: {points} / lives: {lives}")

    if opperation == 'x':
        user_answer = input(f"Solve for x: x + {num1} = {num1 + num2} -> x = ")
    else:
        user_answer = input(f"What is {num1} {opperation} {num2}? ")
      
# Check if the user's answer is correct and update points, lives, and consecutive correct answers accordingly
    if int(user_answer) == int(correct_answer):
        print("Correct! ✨")
        points += 10
        Consecutive_correct_answers += 1    

# If the player gets 3 consecutive correct answers, they level up and the difficulty increases
        if Consecutive_correct_answers == 3:
                level += 1
                Consecutive_correct_answers = 0
                print("🚀 LEVEL UP! Numbers are getting bigger...")

    # If the answer is wrong, the player loses a life and the consecutive correct answers count resets
    else:
        print(f"Wrong! ❌ The correct answer was: {correct_answer}")
        lives -= 1
        Consecutive_correct_answers = 0
        if lives == 0:
            print("Game Over! You've lost all your lives. 😢")
            print(f"Your final score: {points} points")
            break

# If the player reaches level 6, they win the game and the loop breaks
    if level == 7:
          print("Congratulations! You've reached the highest level! 🏆")
          break



# After the game ends, we will check if the player's score is a new high score and save it to a file if it is
file_name = "highscore.txt"

# 1. Leer el record anterior
if os.path.exists(file_name):
    with open(file_name, "r") as f:
        last_record = int(f.read())
else:
    last_record = 0 

#if the player's points are greater than the last record, we will congratulate them and save the new high score to the file. Otherwise, we will display the current record and encourage them to try again.
if points > last_record:
    print(f"🎊 NEW HIGH SCORE! You beat the previous record of {last_record}!")
    with open(file_name, "w") as f:
        f.write(str(points))

#else, we will display the current record and encourage the player to try again.
else:
    print(f"Last score: {last_record}. Good job!😉")