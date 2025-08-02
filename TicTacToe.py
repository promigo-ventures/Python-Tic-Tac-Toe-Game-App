from tkinter import *
from tkmacosx import Button as BT  # ✅ Replaces standard Button
import random

def next_turn(row, col):
    global player
    if buttons[row][col]['text'] == "" and not check_winner():
        buttons[row][col].config(text=player)

        result = check_winner()

        if result is False:

            player = "O" if player == "X" else "X"
            label.config(text=player + " turn")
        elif result is True:
            label.config(text=player + " wins!")
        elif result == "Tie":
            label.config(text="It's a Tie!")

def check_winner():
    # Horizontal
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            for i in range(3):
                buttons[row][i].config(bg="green", activebackground="green")
            return True

    # Vertical
    for col in range(3):
        if buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] != "":
            for i in range(3):
                buttons[i][col].config(bg="green", activebackground="green")
            return True

    # Diagonal TL-BR
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green", activebackground="green")
        buttons[1][1].config(bg="green", activebackground="green")
        buttons[2][2].config(bg="green", activebackground="green")
        return True

    # Diagonal TR-BL
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green", activebackground="green")
        buttons[1][1].config(bg="green", activebackground="green")
        buttons[2][0].config(bg="green", activebackground="green")
        return True

    # Tie
    if all(buttons[r][c]['text'] != "" for r in range(3) for c in range(3)):
        for r in range(3):
            for c in range(3):
                buttons[r][c].config(bg="yellow", activebackground="yellow")
        return "Tie"

    return False

def new_game():
    global player
    player = random.choice(players)
    label.config(text=player + " turn")
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", bg="white", activebackground="lightgrey")

# --- UI Setup ---
window = Tk()
window.title("Tic-Tac-Toe")

players = ["X", "O"]
player = random.choice(players)

label = Label(text=player + " turn", font=("consolas", 30))
label.pack(pady=10)

frame = Frame(window)
frame.pack()

buttons = [[None for _ in range(3)] for _ in range(3)]

for row in range(3):
    for col in range(3):
        b = BT(frame,
               text="",
               font=("consolas", 30),
               width=100, height=100,
               bg="white",
               activebackground="lightgrey",
               command=lambda r=row, c=col: next_turn(r, c))
        b.grid(row=row, column=col, padx=5, pady=5)
        buttons[row][col] = b

BT(text="Restart", font=("consolas", 20), bg="blue", fg="white", command=new_game).pack(pady=10)

window.mainloop()
