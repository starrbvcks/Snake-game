from tkinter import *

#----------------------

def restart_program():
    pass



# ----------------------
GAME_WIDTH = 600
GAME_HEIGHT = 600
SPACE_SIZE = 25
SLOWNESS = 200
SNAKE_COLOR = "PINK"
FOOD_COLOR = "BLUE"
BACKGROUND_COLOR = "black"

score = 0
direction = "down"
# --------------------

window = Tk()
window.title("SNAKE GAME")
window.resizable(False,False)

label = Label(window, text=f"Score:{score}", font= ("Atial Black" , 30))
label.pack()

canvas = Canvas(window, bg= BACKGROUND_COLOR, height= GAME_HEIGHT, width = GAME_WIDTH)
canvas.pack()

restart = Button(window , text="Restart", fg="red", command= restart_program)
restart.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
print(window_width,window_height)
screen_width = window.winfo_screenmmwidth
screen_height = window.winfo_screenmmheight


window.mainloop()