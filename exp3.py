import tkinter as tk
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        self.root.geometry("500x600")
        self.root.config(bg="#2e2e2e")
        self.root.resizable(False, False)

        # Title Label
        self.title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Arial", 24, "bold"), fg="white", bg="#2e2e2e")
        self.title_label.pack(pady=20)

        # Instructions
        self.instructions = tk.Label(root, text="Choose your option", font=("Arial", 16), fg="lightgray", bg="#2e2e2e")
        self.instructions.pack()

        # Choices Frame
        self.choice_frame = tk.Frame(root, bg="#2e2e2e")
        self.choice_frame.pack(pady=20)

        self.choices = ("rock", "paper", "scissors")
        self.player_choice = None

        # Rock button
        self.rock_button = tk.Button(self.choice_frame, text="Rock", font=("Arial", 16), width=10, bg="#6c757d", fg="white",
                                     command=lambda: self.make_choice("rock"))
        self.rock_button.grid(row=0, column=0, padx=10)

        # Paper button
        self.paper_button = tk.Button(self.choice_frame, text="Paper", font=("Arial", 16), width=10, bg="#17a2b8", fg="white",
                                      command=lambda: self.make_choice("paper"))
        self.paper_button.grid(row=0, column=1, padx=10)

        # Scissors button
        self.scissors_button = tk.Button(self.choice_frame, text="Scissors", font=("Arial", 16), width=10, bg="#28a745", fg="white",
                                         command=lambda: self.make_choice("scissors"))
        self.scissors_button.grid(row=0, column=2, padx=10)

        # Result Frame
        self.result_frame = tk.Frame(root, bg="#2e2e2e")
        self.result_frame.pack(pady=20)

        # Player and Computer Labels
        self.player_label = tk.Label(self.result_frame, text="Player: ", font=("Arial", 14), fg="lightgray", bg="#2e2e2e")
        self.player_label.grid(row=0, column=0, padx=20)

        self.computer_label = tk.Label(self.result_frame, text="Computer: ", font=("Arial", 14), fg="lightgray", bg="#2e2e2e")
        self.computer_label.grid(row=0, column=1, padx=20)

        # Result message
        self.result_label = tk.Label(root, text="", font=("Arial", 16, "bold"), fg="white", bg="#2e2e2e")
        self.result_label.pack(pady=20)

        # Play Again Button
        self.play_again_button = tk.Button(root, text="Play Again", font=("Arial", 16), width=15, bg="#ffc107", fg="black",
                                           command=self.reset_game)
        self.play_again_button.pack(pady=20)

    def make_choice(self, player_choice):
        self.player_choice = player_choice
        computer_choice = random.choice(self.choices)

        self.player_label.config(text=f"Player: {player_choice.capitalize()}")
        self.computer_label.config(text=f"Computer: {computer_choice.capitalize()}")

        self.determine_winner(player_choice, computer_choice)

    def determine_winner(self, player, computer):
        if player == computer:
            self.result_label.config(text="It's a tie!", fg="lightgray")
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            self.result_label.config(text="You win!", fg="#28a745")
        else:
            self.result_label.config(text="You lose!", fg="#dc3545")

    def reset_game(self):
        self.player_label.config(text="Player: ")
        self.computer_label.config(text="Computer: ")
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()
