import tkinter as tk
import random

user_score = 0
computer_score = 0

choices = ["Rock", "Paper", "Scissors"]

def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    result_text.set(f"You chose: {user_choice}\nComputer chose: {computer_choice}")

    if user_choice == computer_choice:
        outcome = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        outcome = "You Win!"
        user_score += 1
    else:
        outcome = "Computer Wins!"
        computer_score += 1

    result_text.set(result_text.get() + f"\n{outcome}")
    score_text.set(f"Score - You: {user_score} | Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_text.set("")
    score_text.set(f"Score - You: {user_score} | Computer: {computer_score}")

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x350")
root.config(bg="lightblue")

result_text = tk.StringVar()
score_text = tk.StringVar()
score_text.set("Score - You: 0 | Computer: 0")

tk.Label(root, text="Choose one:", font=("Arial", 14), bg="lightblue").pack(pady=10)

tk.Button(root, text="Rock", width=15, command=lambda: play("Rock")).pack(pady=5)
tk.Button(root, text="Paper", width=15, command=lambda: play("Paper")).pack(pady=5)
tk.Button(root, text="Scissors", width=15, command=lambda: play("Scissors")).pack(pady=5)

tk.Label(root, textvariable=result_text, font=("Arial", 12), bg="lightblue", pady=10).pack()
tk.Label(root, textvariable=score_text, font=("Arial", 12), bg="lightblue").pack()

tk.Button(root, text="Play Again (Reset Score)", command=reset_game).pack(pady=10)

root.mainloop()
