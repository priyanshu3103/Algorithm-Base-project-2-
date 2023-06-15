from tkinter import *
import random

# To give the next chance to the players 
def next_turn(row,col):
    
    global player
    if buttons[row][col]['text'] == "" and check_winner() is False:

        if player == players[0]:
            buttons[row][col]['text'] =player

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+" Turn"))

            elif check_winner() is True:
                label.config(text=(players[0]+" Wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie")

        else:
            buttons[row][col]['text'] =player

            if check_winner() is False:
                player = players[0]
                label.config(text=(player[0]+" Turn"))

            elif check_winner() is True:
                label.config(text=(players[1]+" Wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie")

# To check the winner who is win

def check_winner():
    
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] !="":
            buttons[row][0].config(bg="blue")
            buttons[row][1].config(bg="blue")
            buttons[row][2].config(bg="blue")
            return True
        
    for col in range(3):
        if buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] !="":
            buttons[0][col].config(bg="blue")
            buttons[1][col].config(bg="blue")
            buttons[2][col].config(bg="blue")
            return True
    
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] !="":
            buttons[0][0].config(bg="blue")
            buttons[1][1].config(bg="blue")
            buttons[2][2].config(bg="blue")
            return True
    
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] !="":
            buttons[0][2].config(bg="blue")
            buttons[1][1].config(bg="blue")
            buttons[2][0].config(bg="blue")
            return True
    
    elif empty_space() is False:

        for row in range(3):
            for col in range(3):
                buttons[row][col].config(bg="green")
        return "Tie"
    
    else:
        return False

# To check the empty space 

def empty_space():
    spaces = 9
    for row in range(3):
        for col in range(3):
            if buttons[row][col]['text'] != "":
                spaces-=1
    
    if spaces == 0:
        return False
    
    else:
        return True

# To restart the game

def new_game():
    
    global player
    player = random.choice(players)

    label.config(text=player + " Turn")

    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="",bg="#F0F0F0")


# Main game windows

windows =Tk()
windows.title("Tic-Tac-Toe")
windows.config(bg='#838B8B')
windows.geometry("400x350")
players = ["X", "O"]
player= random.choice(players)
buttons=[[0,0,0],
         [0,0,0],
         [0,0,0]]
label = Label(text= player + " Turn", font=("consolas",20), bg='#838B8B')
label.pack(side='top')

reset_button = Button(text="restart", font=('consolas',10), command=new_game)
reset_button.pack(side="top")

frame =Frame(windows)
frame.pack()


for row in range(3):
    for col in range(3):
        buttons[row][col] = Button(frame, text = "", font=("consolas",20),width=5, height=2, bg= '#C1CDCD', command=lambda row=row, col=col: next_turn(row,col))
        buttons[row][col].grid(row=row,column=col)

windows.mainloop()