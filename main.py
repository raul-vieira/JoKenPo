import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random
# colors for the project
white = "#FFFFFF"
black = "#333333"
orange = "#fcc058"
yellow = "#fff873"
green = "#34eb3d" 
red = "#e85151" 
background = '#3b3b3b'

# creating window
window = Tk()
window.title('Jo-Ken-Po Game')
window.geometry('260x280')
window.configure(bg=background)

# separating window frames
superior_frame = Frame(window, height=100, width=260, bg=black, padx=0, pady=0, relief='raised') 
superior_frame.grid(row=0, column=0, sticky=NW)

inferior_frame = Frame(window, height=300, width=260, bg=white, padx=0, pady=0, relief='flat') 
inferior_frame.grid(row=1, column=0, sticky=NW)

style = ttk.Style(window)
style.theme_use('clam')

# superior frame config
player_1 = Label(superior_frame, text='You', height=1, anchor='center',font=('Roboto 10 bold'), bg=black, fg=white)
player_1.place(x=25, y=70)
player_1_line = Label(superior_frame, text='', height=10, anchor='center',font=('Roboto 10 bold'), bg=white, fg=white)
player_1_line.place(x=0, y=0)
player_1_points = Label(superior_frame, text='0', height=1, anchor='center',font=('Roboto 30 bold'), bg=black, fg=white)
player_1_points.place(x=50, y=20)

player_div = Label(superior_frame, text=':', height=1, anchor='center',font=('Roboto 30 bold'), bg=black, fg=white)
player_div.place(x=115, y=20)

player_2 = Label(superior_frame, text='COM', height=1, anchor='center',font=('Roboto 10 bold'), bg=black, fg=white)
player_2.place(x=205, y=70)
player_2_line = Label(superior_frame, text='', height=10, anchor='center',font=('Roboto 10 bold'), bg=white, fg=white)
player_2_line.place(x=255, y=0)
player_2_points = Label(superior_frame, text='0', height=1, anchor='center',font=('Roboto 30 bold'), bg=black, fg=white)
player_2_points.place(x=170, y=20)

draw_line = Label(superior_frame, text='', width=255, anchor='center',font=('Roboto 1 bold'), bg=white, fg=white)
draw_line.place(x=0, y=95)

# display pc choice
player_2_choice = Label(inferior_frame, text='', height=1, anchor='center',font=('Roboto 12 bold'), bg=white, fg=white)
player_2_choice.place(x=190, y=10)

global player
global pc 
global rounds
global player_points 
global pc_points 

player_points = 0
pc_points = 0
rounds = 5



# game logic function
def play(i):
    global rounds
    global player_points 
    global pc_points

    if rounds>0:
        print(rounds)
        options = ['rock', 'paper', 'scissors']
        pc = random.choice(options)
        player = i
        player_2_choice['text']=pc
        player_2_choice['fg']=black
        # if draw
        if player == 'rock' and pc == 'rock':
            print('Draw')
            draw_line['bg'] = yellow
            player_1_line['bg'] = white
            player_2_line['bg'] = white

        elif player == 'paper' and pc == 'paper':
            print('Draw')
            draw_line['bg'] = yellow
            player_1_line['bg'] = white
            player_2_line['bg'] = white  

        elif player == 'scissors' and pc == 'scissors':
            print('Draw')
            draw_line['bg'] = yellow
            player_1_line['bg'] = white
            player_2_line['bg'] = white
        # conditions if not draw
        elif player == 'rock' and pc == 'paper':
            print('COM wins')
            draw_line['bg'] = white
            player_1_line['bg'] = red
            player_2_line['bg'] = green
            pc_points +=1
        elif player == 'rock' and pc == 'scissors':
            print('Player wins')
            draw_line['bg'] = white
            player_1_line['bg'] = green
            player_2_line['bg'] = red
            player_points +=1
        elif player == 'paper' and pc == 'scissors':
            print('COM wins')
            draw_line['bg'] = white
            player_1_line['bg'] = red
            player_2_line['bg'] = green
            pc_points +=1
        elif player == 'scissors' and pc == 'paper':
            print('Player wins')
            draw_line['bg'] = white
            player_1_line['bg'] = green
            player_2_line['bg'] = red
            player_points +=1
        elif player == 'scissors' and pc == 'rock':
            print('COM wins')
            draw_line['bg'] = white
            player_1_line['bg'] = red
            player_2_line['bg'] = green
            pc_points +=1
        elif player == 'paper' and pc == 'rock':
            print('Player wins')
            draw_line['bg'] = white
            player_1_line['bg'] = green
            player_2_line['bg'] = red
            player_points +=1
        # points and rounds update
        player_1_points['text']=player_points
        player_2_points['text']=pc_points
        rounds -=1
    else:
        end_game()    


# function to begin the game
# inferior frame config
def begin_game():
    global rock_icon
    global paper_icon
    global scissors_icon
    global button_rock
    global button_paper
    global button_scissors

    button_play.destroy()

    rock_icon = Image.open('images/rock.png')
    rock_icon = rock_icon.resize((50,50), Image.ANTIALIAS)
    rock_icon = ImageTk.PhotoImage(rock_icon)
    button_rock = Button(inferior_frame, command=lambda: play('rock'), width=50, image=rock_icon, compound=CENTER, bg=white, fg=black, font='Roboto 10 bold', anchor=CENTER, relief='flat')
    button_rock.place(x=25, y=60)

    paper_icon = Image.open('images/paper.png')
    paper_icon = paper_icon.resize((50,50), Image.ANTIALIAS)
    paper_icon = ImageTk.PhotoImage(paper_icon)
    button_paper = Button(inferior_frame, command=lambda: play('paper'), width=50, image=paper_icon, compound=CENTER, bg=white, fg=black, font='Roboto 10 bold', anchor=CENTER, relief='flat')
    button_paper.place(x=100, y=60)

    scissors_icon = Image.open('images/scissors.png')
    scissors_icon = scissors_icon.resize((50,50), Image.ANTIALIAS)
    scissors_icon = ImageTk.PhotoImage(scissors_icon)
    button_scissors = Button(inferior_frame, command=lambda: play('scissors'), width=50, image=scissors_icon, compound=CENTER, bg=white, fg=black, font='Roboto 10 bold', anchor=CENTER, relief='flat')
    button_scissors.place(x=180, y=60)


# function to end the game

def end_game():
    global rounds
    global player_points 
    global pc_points 
    # prepare for rematch
    player_points = 0
    pc_points = 0
    rounds = 5
    button_paper.destroy()
    button_rock.destroy()
    button_scissors.destroy()
    # define the winner
    winner_player = int(player_1_points['text'])
    winner_pc = int(player_2_points['text'])
    if winner_player > winner_pc:
        prize = Label(inferior_frame, text='Congratulations, you won!!', height=1, anchor=CENTER, font='Roboto 10 bold', bg=white, fg=green)
        prize.place(x=5,y=60)
    elif winner_player < winner_pc:
        prize = Label(inferior_frame, text='Oh no, you lost!!', height=1, anchor=CENTER, font='Roboto 10 bold', bg=white, fg=red)
        prize.place(x=5,y=60)
    else:
        prize = Label(inferior_frame, text='Its a draw!!', height=1, anchor=CENTER, font='Roboto 10 bold', bg=white, fg=orange)
        prize.place(x=5,y=60)

    # function to rematch
    def play_again():
        player_1_points['text']='0'  
        player_2_points['text']='0'
        prize.destroy()
        button_rematch.destroy()
        begin_game()

    button_rematch = Button(inferior_frame, command=play_again, width=30, text='Play again', bg=background, fg=white, font='Roboto 10 bold', anchor=CENTER, relief='raised', overrelief=RIDGE)
    button_rematch.place(x=5, y=150)

button_play = Button(inferior_frame, command=begin_game, width=30, text='Play', bg=background, fg=white, font='Roboto 10 bold', anchor=CENTER, relief='raised', overrelief=RIDGE)
button_play.place(x=5, y=150)


window.mainloop()
