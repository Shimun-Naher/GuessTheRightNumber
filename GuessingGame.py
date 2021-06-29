import tkinter as tk
from random import randrange

root = tk.Tk()
root.title("Guess the Right Number to Win")

initial = tk.Label(root, text = "Guess A Number From 0 to 9")
beginner = tk.Label(root, text = "# of Guesses: 0")
maxguess = tk.Label(root, text = "Maximum # of Guesses: 3")
options = tk.Label(root, text="What's Your Guess?")

buttons = []
for number in range(0, 10):
    button = tk.Button(root, text=number, command=lambda number=number : process(number), state=tk.DISABLED)
    buttons.append(button)


beginning = []
for number in range(0, 1):
    initiation = tk.Button(root, text="Let's Begin", command=lambda : starting(number))
    beginning.append(initiation)

initial.grid(row=0, column=0, columnspan=5)
beginner.grid(row=2, column=0, columnspan=2)
maxguess.grid(row=2, column=3, columnspan=2)
options.grid(row=4, column=0, columnspan=5)


for row in range(0, 2):
    for col in range(0, 5):
        i = row * 5 + col
        buttons[i].grid(row=row+10, column=col)

beginning[0].grid(row=13, column=0, columnspan=5)

guess = 0
totalNumberOfGuesses = 0
correctNumber = randrange(10)
print(correctNumber)
options = []
guess_row = 4

def init():
    global buttons, guess, totalNumberOfGuesses, correctNumber, beginner, options, guess_row
    guess = 0
    totalNumberOfGuesses = 0
    correctNumber = randrange(10)
    print(correctNumber)
    beginner["text"] = "# of Guesses: 0"
    guess_row = 4

    for option in options:
        option.grid_forget()
    options = []


def process(i):
    global totalNumberOfGuesses, buttons, guess_row
    guess = i

    totalNumberOfGuesses += 1
    beginner["text"] = "# of Guesses: " + str(totalNumberOfGuesses)

    if guess == correctNumber:
        lbm = tk.Label(root, text="Your guess is correct. You won!", fg="green")
        lbm.grid(row=guess_row, column=0, columnspan=5)
        options.append(lbm)
        guess_row += 1

        for b in buttons:
            b["state"] = tk.DISABLED
    else:
        if guess > correctNumber:
            lbm = tk.Label(root, text="The correct number is smaller", fg="red")
            lbm.grid(row=guess_row, column=0, columnspan=5)
            options.append(lbm)
            guess_row += 1
        else:
            lbm = tk.Label(root, text="The correct number is larger", fg="red")
            lbm.grid(row=guess_row, column=0, columnspan=5)
            options.append(lbm)
            guess_row += 1

    if totalNumberOfGuesses == 3:
        if guess != correctNumber:
            lbm = tk.Label(root, text="Maximum number of guesses reached. You lost!", fg="red")
            lbm.grid(row=guess_row, column=0, columnspan=5)
            options.append(lbm)
            guess_row += 1

        for b in buttons:
            b["state"] = tk.DISABLED

    buttons[i]["state"] = tk.DISABLED


status = "none"


def starting(i):
    global status
    for b in buttons:
        b["state"] = tk.NORMAL

    if status == "none":
        status = "started"
        beginning[i]["text"] = "Start Over"
    else:
        status = "restarted"
        init()
    print("The Game Has Started")


root.mainloop()
