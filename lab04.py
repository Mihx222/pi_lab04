from tkinter import *
from tkinter import messagebox
from random import randint


#   Game score
player_score = 0
bot_score = 0


def download_rules():
    """
    Download rules image from the internet
    """
    import urllib.request as url
    url.urlretrieve("https://i.imgur.com/bueoebd.png", "rules.png")


def rules_window():
    """
    Create a window dedicated to game rules
    """
    window = Toplevel(root)
    window.title("Rules")
    window.resizable(False, False)
#   Set initial window position
    window.geometry("+300+300")

#   Use downloaded image
    rules_label = Label(window)
    rules_label.rules_picture_png = PhotoImage(file="rules.png")
    rules_label['text'] = "rules.png"
    rules_label['image'] = rules_label.rules_picture_png
    rules_label.pack()

#   Close window button
    close_dialog_button = Button(window, width=38, font="none 12", text="Close", command=window.destroy)
    close_dialog_button.pack()

#   Focus on window
    window.focus_set()
#   Doesn't allow interacting with root as long as window exists
    window.grab_set()


#   Check for choice
def check_for_choice():
    """
    Checks if player has made a choice
    """
    if choice.get() == "Choose an option":
        messagebox.showerror("Error", "Choose an option first!")
    else:
        simulate_game()


#   Game logic
def simulate_game():
    bot_element_choice = randint(1, 5)

#   Dynamically update bot choice
    if bot_element_choice == 1:
        bot_choice_label.config(fg="black", text="Bot chose: Rock")
        bot_element_choice_text = "Rock"
    elif bot_element_choice == 2:
        bot_choice_label.config(fg="black", text="Bot chose: Paper")
        bot_element_choice_text = "Paper"
    elif bot_element_choice == 3:
        bot_choice_label.config(fg="black", text="Bot chose: Scissors")
        bot_element_choice_text = "Scissors"
    elif bot_element_choice == 4:
        bot_choice_label.config(fg="black", text="Bot chose: Spock")
        bot_element_choice_text = "Spock"
    else:
        bot_choice_label.config(fg="black", text="Bot chose: Lizard")
        bot_element_choice_text = "Lizard"

#   Check and filter input
    if ((choice.get() == "Rock" and bot_element_choice == 2) or
        (choice.get() == "Paper" and bot_element_choice == 1) or
        (choice.get() == "Paper" and bot_element_choice == 4) or
        (choice.get() == "Spock" and bot_element_choice == 2)):
        result = "Paper"
    elif ((choice.get() == "Rock" and bot_element_choice == 3) or
          (choice.get() == "Scissors" and bot_element_choice == 1) or
          (choice.get() == "Rock" and bot_element_choice == 5) or
          (choice.get() == "Lizard" and bot_element_choice == 1)):
        result = "Rock"
    elif ((choice.get() == "Scissors" and bot_element_choice == 2) or
          (choice.get() == "Paper" and bot_element_choice == 3) or
          (choice.get() == "Scissors" and bot_element_choice == 5) or
          (choice.get() == "Lizard" and bot_element_choice == 3)):
        result = "Scissors"
    elif ((choice.get() == "Spock" and bot_element_choice == 1) or
          (choice.get() == "Rock" and bot_element_choice == 4) or
          (choice.get() == "Spock" and bot_element_choice == 3) or
          (choice.get() == "Scissors" and bot_element_choice == 4)):
        result = "Spock"
    else:
        result = "Lizard"

#   Verify win conditions, evaluate winner and modify score labels
    global player_score, bot_score
    if choice.get() == result and bot_element_choice_text != result:
        player_score = player_score + 1
        player_score_label['text'] = "Player score: " + str(player_score)
        messagebox.showinfo("Felicitari", "Felicitari! Ati castigat!")
    elif bot_element_choice_text == result and choice.get() != result:
        bot_score = bot_score + 1
        bot_score_label['text'] = "Bot score: " + str(bot_score)
        messagebox.showinfo("Nenorocire", "A castigat Bot-ul!")
    else:
        messagebox.showinfo("Egalitate", "Egalitate!")


#   Downloads image of rules
download_rules()
#   Setup root
root = Tk()
#   Set initial window position
root.geometry("+300+300")
root.resizable(False, False)
root.title("Rock, Paper, Scissors")

#   Introduction message label
label = Label(root, text="Welcome to the advanced version of Rock, Paper and Scissors.\n"
                         "Check the rules before playing.",
              font=("Helvetica", 16))
label.pack(padx=3, pady=3)

#   Root frames
root_top_frame = Frame(root)
root_top_frame.pack(side=TOP)
root_bottom_frame = Frame(root)
root_bottom_frame.pack(side=BOTTOM)
score_frame = LabelFrame(root, text="Score")
score_frame.pack(padx=3, pady=3, fill="both", expand="yes")

#   Game frame
game_options_frame = LabelFrame(root_top_frame, text="Match")
game_options_frame.pack(padx=3, pady=3, fill="both", expand="yes")

# Choices
choices = {"Rock", "Paper", "Scissors", "Lizard", "Spock"}

#   Game layer top frame
game_layer_top_frame = Frame(game_options_frame)
game_layer_top_frame.pack(side=TOP)

#   Game layer bottom frame
game_layer_bottom_frame = Frame(game_options_frame)
game_layer_bottom_frame.pack(side=BOTTOM)

#   Player choice list
choice_label = Label(game_layer_top_frame, text="Choose your element:", font="none 12")
choice_label.pack(side=LEFT)
choice = StringVar(game_layer_top_frame)
choice.set("Choose an option")
choices_option_menu = OptionMenu(game_layer_top_frame, choice, *choices)
choices_option_menu.pack(padx=3, pady=3, side=LEFT)

#   Bot choice
bot_choice = StringVar(game_layer_top_frame)
bot_choice.set("None")
bot_choice_label = Label(game_layer_top_frame, text="Bot chose: " + bot_choice.get(), font="none 12")
if bot_choice.get() == "None":
    bot_choice_label.config(fg="red", text="Bot chose: Nothing yet")
bot_choice_label.pack(padx=50, pady=3, side=LEFT)

#   Rules button
rules_button = Button(root_bottom_frame, text="Rules", width=22, font="none 12", command=rules_window)
rules_button.pack(padx=3, pady=3, side=LEFT)

#   About
about_label = Label(root_bottom_frame, text="Made by: Curchi Mihail, IA-171")
about_label.pack(padx=3, pady=3, side=LEFT)

#   Quit button
quit_button = Button(root_bottom_frame, text="Quit", width=22, font="none 12", command=root.destroy)
quit_button.pack(padx=3, pady=3, side=RIGHT)

#   Score labels
player_score_label = Label(score_frame, text="Player: " + str(player_score), font="none 12")
player_score_label.pack(padx=60, pady=3, side=LEFT)
bot_score_label = Label(score_frame, text="Bot: " + str(bot_score), font="none 12")
bot_score_label.pack(padx=60, pady=3, side=RIGHT)

#   Play button
play_button = Button(game_layer_bottom_frame, text="Play", width=65, font="none 12", command=check_for_choice)
play_button.pack(padx=3, pady=5)

#   Launches root
root.mainloop()
