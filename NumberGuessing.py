import tkinter as tk
from tkinter import messagebox
import random
import winsound

# Sound functions

def play_success():
    winsound.MessageBeep(winsound.MB_ICONASTERISK)

def play_error():
    winsound.MessageBeep(winsound.MB_ICONHAND)

def play_guess():
    winsound.MessageBeep(winsound.MB_OK)

# Game logic

def check_guess():
    global attempts, secret_number
    try:
        guess = int(entry.get())
        attempts += 1
        play_guess()
        if guess < secret_number:
            result_label.config(text="Too low!", fg="#0077b6")
        elif guess > secret_number:
            result_label.config(text="Too high!", fg="#d90429")
        else:
            play_success()
            messagebox.showinfo("Congratulations!", f"You guessed the number in {attempts} attempts.")
            reset_game()
    except ValueError:
        play_error()
        result_label.config(text="Please enter a valid integer.", fg="#ff8800")

def reset_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    entry.delete(0, tk.END)
    result_label.config(text="", fg="#22223b")

# UI setup
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("430x400")
root.configure(bg="#22223b")

header = tk.Label(root, text="Number Guessing Game", font=("Segoe UI", 22, "bold"), fg="#f72585", bg="#22223b")
header.pack(pady=(25, 10))

instructions = tk.Label(root, text="I'm thinking of a number between 1 and 100.", font=("Segoe UI", 13), bg="#22223b", fg="#b5e48c")
instructions.pack(pady=5)

frame = tk.Frame(root, bg="#22223b")
frame.pack(pady=15)

entry_label = tk.Label(frame, text="Your Guess:", font=("Segoe UI", 13), bg="#22223b", fg="#fcbf49")
entry_label.grid(row=0, column=0, padx=5)

entry = tk.Entry(frame, font=("Segoe UI", 13), width=10, bg="#f1faee", fg="#22223b", justify="center")
entry.grid(row=0, column=1, padx=5)

submit_btn = tk.Button(root, text="Guess", command=check_guess, font=("Segoe UI", 13, "bold"), bg="#00b4d8", fg="white", activebackground="#0077b6", activeforeground="white", width=12, bd=0, relief="ridge")
submit_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Segoe UI", 13, "italic"), bg="#22223b", fg="#22223b")
result_label.pack(pady=10)

reset_btn = tk.Button(root, text="Reset Game", command=reset_game, font=("Segoe UI", 12), bg="#f3722c", fg="white", activebackground="#d90429", activeforeground="white", width=14, bd=0, relief="ridge")
reset_btn.pack(pady=5)

footer = tk.Label(root, text="Good luck!", font=("Segoe UI", 11, "italic"), bg="#22223b", fg="#b5e48c")
footer.pack(side="bottom", pady=15)

# Initialize game state
secret_number = random.randint(1, 100)
attempts = 0

root.mainloop()
