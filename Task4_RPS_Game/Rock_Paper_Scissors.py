import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock, Paper, Scissors Game")

        self.user_score = 0
        self.computer_score = 0

        self.user_choice_label = tk.Label(self.master, text="Your choice:")
        self.user_choice_label.pack()

        self.user_choice_var = tk.StringVar()
        self.user_choice_var.set("rock")

        self.user_choices = ["rock", "paper", "scissors"]
        self.user_choice_menu = tk.OptionMenu(self.master, self.user_choice_var, *self.user_choices)
        self.user_choice_menu.pack()

        self.play_button = tk.Button(self.master, text="Play", command=self.play_game)
        self.play_button.pack()

        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack()

        self.score_label = tk.Label(self.master, text="")
        self.score_label.pack()

    def get_computer_choice(self):
        return random.choice(["rock", "paper", "scissors"])

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "scissors" and computer_choice == "paper") or
            (user_choice == "paper" and computer_choice == "rock")
        ):
            self.user_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "You lose!"

    def update_score_label(self):
        self.score_label.config(text=f"Score - You: {self.user_score}, Computer: {self.computer_score}")

    def play_game(self):
        user_choice = self.user_choice_var.get()
        computer_choice = self.get_computer_choice()

        result = self.determine_winner(user_choice, computer_choice)
        self.result_label.config(text=result)
        self.update_score_label()

        play_again = messagebox.askyesno("Play Again", "Do you want to play again?")
        if not play_again:
            self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
