import random
import tkinter as tk
from tkinter import messagebox

class Game2048:
    def __init__(self, master):
        self.master = master
        self.master.title("2048 Game")
        self.master.geometry("400x400")
        self.board = [[0] * 4 for _ in range(4)]

        self.init_board()
        self.draw_board()

        self.master.bind("<Left>", lambda event: self.move("left"))
        self.master.bind("<Right>", lambda event: self.move("right"))
        self.master.bind("<Up>", lambda event: self.move("up"))
        self.master.bind("<Down>", lambda event: self.move("down"))

    def init_board(self):
        add_new_tile(self.board)
        add_new_tile(self.board)

    def draw_board(self):
        for i in range(4):
            for j in range(4):
                cell_value = self.board[i][j]
                cell_color = get_color(cell_value)

                label = tk.Label(self.master, text=str(cell_value), font=("Helvetica", 16, "bold"),
                                 width=5, height=2, relief="ridge", bg=cell_color)
                label.grid(row=i, column=j, padx=5, pady=5)

    def move(self, direction):
        if direction == "left":
            self.board = [merge(row) for row in self.board]
        elif direction == "right":
            self.board = [merge(row[::-1])[::-1] for row in self.board]
        elif direction == "up":
            self.board = [merge([self.board[i][j] for i in range(4)]) for j in range(4)]
        elif direction == "down":
            self.board = [merge([self.board[i][j] for i in range(4)][::-1])[::-1] for j in range(4)]

        add_new_tile(self.board)
        self.draw_board()

        if is_game_over(self.board):
            messagebox.showinfo("Game Over", "Game Over!")
            self.master.destroy()

def merge(row):
    new_row = [0] * 4
    index = 0
    for num in row:
        if num != 0:
            if new_row[index] == 0:
                new_row[index] = num
            elif new_row[index] == num:
                new_row[index] *= 2
                index += 1
            else:
                index += 1
                new_row[index] = num
    return new_row

def add_new_tile(board):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = 2 if random.random() < 0.9 else 4

def is_game_over(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return False
            if j > 0 and board[i][j] == board[i][j - 1]:
                return False
            if i > 0 and board[i][j] == board[i - 1][j]:
                return False
    return True

def get_color(value):
    colors = {
        2: "#eee4da",
        4: "#ede0c8",
        8: "#f2b179",
        16: "#f59563",
        32: "#f67c5f",
        64: "#f65e3b",
        128: "#edcf72",
        256: "#edcc61",
        512: "#edc850",
        1024: "#edc53f",
        2048: "#edc22e",
    }
    return colors.get(value, "#cdc1b4")

if __name__ == "__main__":
    root = tk.Tk()
    game = Game2048(root)
    root.mainloop()
