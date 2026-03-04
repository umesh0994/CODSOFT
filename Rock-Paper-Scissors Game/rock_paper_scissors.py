import random

choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
wins = {'r': 's', 's': 'p', 'p': 'r'}
user_score, comp_score = 0, 0

print("=== Rock Paper Scissors Game ===")
print("Enter 'r' for Rock, 'p' for Paper, 's' for Scissors, 'q' to quit")

while True:
    user = input("\nYour choice (r/p/s): ").lower()
    if user == 'q':
        break
    if user not in choices:
        print("Invalid! Try again.")
        continue
    
    comp = random.choice(['r', 'p', 's'])
    print(f"You: {choices[user]} | Computer: {choices[comp]}")
    
    if user == comp:
        print("Result: It's a Tie!")
    elif wins[user] == comp:
        print("Result: You Win!")
        user_score += 1
    else:
        print("Result: You Lose!")
        comp_score += 1
    
    print(f"Score - You: {user_score} | Computer: {comp_score}")
    print("-" * 30)

print(f"\nFinal Score - You: {user_score} | Computer: {comp_score}")
print("Thanks for playing!")

