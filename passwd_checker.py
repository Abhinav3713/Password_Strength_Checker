# checker_gui.py
import re
import tkinter as tk
from tkinter import messagebox

# Function to check password strength
def check_password_strength(password):
    strength_points = 0

    # Criteria checks
    if len(password) >= 8:
        strength_points += 1
    if re.search(r"[A-Z]", password):
        strength_points += 1
    if re.search(r"[a-z]", password):
        strength_points += 1
    if re.search(r"[0-9]", password):
        strength_points += 1
    if re.search(r"[\W_]", password):  # special characters
        strength_points += 1

    # Determine strength
    if strength_points <= 2:
        return "Weak"
    elif strength_points == 3 or strength_points == 4:
        return "Moderate"
    else:
        return "Strong"

# GUI function
def evaluate_password():
    pwd = entry.get()
    if not pwd:
        messagebox.showwarning("Input Error", "Please enter a password.")
        return

    result = check_password_strength(pwd)
    result_label.config(text=f"Strength: {result}", fg=color[result])

# Tkinter GUI setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")
root.resizable(False, False)

# UI Elements
tk.Label(root, text="Enter your Password:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, font=("Arial", 12), width=30)
entry.pack()

tk.Button(root, text="Check Strength", command=evaluate_password, font=("Arial", 12)).pack(pady=10)

color = {"Weak": "red", "Moderate": "orange", "Strong": "green"}
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack()

root.mainloop()
