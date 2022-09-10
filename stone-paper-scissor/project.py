from os import P_WAIT, abort
from tkinter import *
from PIL import Image, ImageTk
from random import randint
from tkinter import messagebox
from tkinter import simpledialog
import time
from sys import exit

root = Tk()

root.title("Rock Scissor Paper")
root.configure(background="#9b59b6")
# max_score=10


# picture
rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissors-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))

# insert picture
user_label = Label(root, image=scissor_img, bg="#9b59b6")
comp_label = Label(root, image=scissor_img_comp, bg="#9b59b6")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)


# scores
playerScore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerScore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

# indicators
user_indicator = Label(root, font=50, text="USER", bg="#9b59b6", fg="white")
comp_indicator = Label(root, font=50, text="COMPUTER",
                       bg="#9b59b6", fg="white")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)


# messages
msg = Label(root, font=50, bg="#9b59b6", fg="white")
msg.grid(row=3, column=2)


max_score = 10

# messagebox.showinfo("Limit","Scorelimit is 10")
# time.sleep(5)

# update message


def updateMessage(x):
    msg['text'] = x

# update user score


def updateUserScore():

    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)
    MsgBox = ""

    if (score == max_score):
        MsgBox = messagebox.askquestion(
            'You Won', 'Want to play again')
    if MsgBox == 'yes':
        playerScore["text"] = 0
        computerScore["text"] = 0
    elif MsgBox == 'no':
        MsgBox = messagebox.askquestion('EXIT', "You want to exit")
        if MsgBox == "yes":
            exit()
        else:
            pass
    else:
        pass

# update computer score


def updateCompScore():

    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)
    MsgBox = ""

    if (score == max_score):
        MsgBox = messagebox.askquestion(
            'You Loose', "You want to play again")
    if MsgBox == 'yes':
        playerScore["text"] = 0
        computerScore["text"] = 0
    elif MsgBox == 'no':
        MsgBox = messagebox.askquestion('EXIT', "You want to exit")
        if MsgBox == "yes":
            exit()
        else:
            pass
    else:
        pass
# check winner


def checkWin(player, computer):

    if player == computer:
        updateMessage("Its a tie!!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif playerScore["text"] == "3" or computerScore["text"] == "3":
        pass


# update choices
choices = ["rock", "paper", "scissor"]

# max_score =simpledialog.askinteger("Score Limit!", \
# "Set the Limit of the Score",minvalue=1,)


def updateChoice(x):
    compChoice = ""

    if (int(playerScore["text"]) < max_score and int(computerScore["text"]) < max_score):
        # for computer
        compChoice = choices[randint(0, 2)]
        if compChoice == "rock":
            comp_label.configure(image=rock_img_comp)
        elif compChoice == "paper":
            comp_label.configure(image=paper_img_comp)
        else:
            comp_label.configure(image=scissor_img_comp)


# for user
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWin(x, compChoice)


def restart():
    MsgBox = messagebox.askquestion(
        'RESET SCORE', 'Are you sure you want to Reset the Score')
    if MsgBox == 'yes':
        playerScore["text"] = 0
        computerScore["text"] = 0
    else:
        pass


# buttons
rock = Button(root, width=20, height=2, text="ROCK",
              bg="#FF3E4D", fg="white", command=lambda: updateChoice("rock")).grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="PAPER",
               bg="#FAD02E", fg="white", command=lambda: updateChoice("paper")).grid(row=2, column=2)
scissor = Button(root, width=20, height=2, text="SCISSOR",
                 bg="#0ABDE3", fg="white", command=lambda: updateChoice("scissor")).grid(row=2, column=3)
reset = Button(root, width=20, height=2, text="RESET",
               bg="#B33C5A", fg="white", command=restart).grid(row=4, column=2)

# max_score =simpledialog.askinteger("Score Limit!", \
# "Set the Limit of the Score",minvalue=1,)

root.mainloop()