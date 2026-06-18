from tkinter import *
import random

# ----------------------
# متغیرهای پایه و تنظیمات پیش‌فرض
GAME_WIDTH = 600
GAME_HEIGHT = 600
SPACE_SIZE = 25
BODY_PARTS = 3

# تنظیمات سختی پیش‌فرض (Normal)
BASE_SLOWNESS = 120
SLOWNESS = 120
SPEED_INC = 2
NUM_OBSTACLES = 8

# تنظیمات استایل پیش‌فرض (Candy)
HEAD_COLOR = "Red"
BODY_COLOR = "Pink"
FOOD_COLOR = "Yellow"
OBSTACLE_COLOR = "White"
BACKGROUND_COLOR = "Purple"

score = 0
direction = "down"
game_loop_id = None  # برای مدیریت صحیح ری‌استارت و جلوگیری از تداخل تایمرها

# ----------------------
def restart_program():
    global score, direction, SLOWNESS, game_loop_id
    
    # لغو حلقه قبلی بازی در صورت وجود
    if game_loop_id is not None:
        window.after_cancel(game_loop_id)
        
    score = 0
    direction = "down"
    SLOWNESS = BASE_SLOWNESS # بازنشانی سرعت
    
    label.config(text=f"Score: {score}")
    canvas.config(bg=BACKGROUND_COLOR) # اعمال رنگ پس‌زمینه جدید
    canvas.delete("all")
    
    global snake, food, obstacles
    obstacles = Obstacles()
    snake = Snake()
    food = Food()
    next_turn(snake, food)

def open_settings():
    settings_win = Toplevel(window)
    settings_win.title("Settings")
    settings_win.geometry("300x300")
    settings_win.resizable(False, False)
    
    # متغیرهای فرم
    diff_var = StringVar(value="Normal")
    theme_var = StringVar(value="Candy")
    
    Label(settings_win, text="Difficulty Level", font=("Arial", 14, "bold")).pack(pady=10)
    Radiobutton(settings_win, text="Easy (No obstacles, Slow)", variable=diff_var, value="Easy").pack()
    Radiobutton(settings_win, text="Normal (8 obstacles, Medium)", variable=diff_var, value="Normal").pack()
    Radiobutton(settings_win, text="Hard (15 obstacles, Fast)", variable=diff_var, value="Hard").pack()
    
    Label(settings_win, text="Game Theme", font=("Arial", 14, "bold")).pack(pady=10)
    Radiobutton(settings_win, text="Candy (Pink/Purple)", variable=theme_var, value="Candy").pack()
    Radiobutton(settings_win, text="Classic (Green/Black)", variable=theme_var, value="Classic").pack()
    Radiobutton(settings_win, text="Neon (Cyan/Black)", variable=theme_var, value="Neon").pack()
    
    Button(settings_win, text="Apply & Restart", bg="green", fg="white", font=("Arial", 12),
           command=lambda: apply_settings(diff_var.get(), theme_var.get(), settings_win)).pack(pady=20)

def apply_settings(diff, theme, settings_win):
    global BASE_SLOWNESS, SPEED_INC, NUM_OBSTACLES
    global HEAD_COLOR, BODY_COLOR, FOOD_COLOR, OBSTACLE_COLOR, BACKGROUND_COLOR
    
    # اعمال سختی
    if diff == "Easy":
        BASE_SLOWNESS, SPEED_INC, NUM_OBSTACLES = 150, 0, 0
    elif diff == "Normal":
        BASE_SLOWNESS, SPEED_INC, NUM_OBSTACLES = 120, 2, 8
    elif diff == "Hard":
        BASE_SLOWNESS, SPEED_INC, NUM_OBSTACLES = 90, 5, 15
        
    # اعمال تم
    if theme == "Classic":
        HEAD_COLOR, BODY_COLOR, FOOD_COLOR, OBSTACLE_COLOR, BACKGROUND_COLOR = "DarkGreen", "Green", "Red", "Gray", "black"
    elif theme == "Candy":
        HEAD_COLOR, BODY_COLOR, FOOD_COLOR, OBSTACLE_COLOR, BACKGROUND_COLOR = "Red", "Pink", "Yellow", "White", "Purple"
    elif theme == "Neon":
        HEAD_COLOR, BODY_COLOR, FOOD_COLOR, OBSTACLE_COLOR, BACKGROUND_COLOR = "White", "Cyan", "Magenta", "Yellow", "black"
        
    settings_win.destroy()
    restart_program()

def change_direction(new_direction):
    global direction
    if new_direction == 'left' and direction != 'right': direction = new_direction
    elif new_direction == 'right' and direction != 'left': direction = new_direction
    elif new_direction == 'up' and direction != 'down': direction = new_direction
    elif new_direction == 'down' and direction != 'up': direction = new_direction

def check_collisions(snake):
    x, y = snake.coordinates[0]
    # برخورد با بدن
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]: return True
    # برخورد با مانع
    for obs in obstacles.coordinates:
        if x == obs[0] and y == obs[1]: return True
    return False

def game_over():
    canvas.delete("all")
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('Arial Black', 50), text="GAME OVER", fill="red")

def next_turn(snake, food):
    global SLOWNESS, score, game_loop_id
    x, y = snake.coordinates[0]
    
    if direction == "up": y -= SPACE_SIZE
    elif direction == "down": y += SPACE_SIZE
    elif direction == "left": x -= SPACE_SIZE
    elif direction == "right": x += SPACE_SIZE

    # رد شدن از دیوارها
    if x < 0: x = GAME_WIDTH - SPACE_SIZE
    elif x >= GAME_WIDTH: x = 0
    if y < 0: y = GAME_HEIGHT - SPACE_SIZE
    elif y >= GAME_HEIGHT: y = 0

    snake.coordinates.insert(0, (x, y))
    
    if len(snake.squares) > 0:
        canvas.itemconfig(snake.squares[0], fill=BODY_COLOR)
        
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=HEAD_COLOR)
    snake.squares.insert(0, square)

    # خوردن غذا
    if x == food.coordinates[0] and y == food.coordinates[1]:
        score += 1
        label.config(text=f"Score:{score}")
        
        # افزایش سرعت (کاهش SLOWNESS) - حداقل سرعت روی 40 تنظیم شده تا غیرممکن نشود
        SLOWNESS = max(40, SLOWNESS - SPEED_INC)
        
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        game_loop_id = window.after(SLOWNESS, next_turn, snake, food)

# ----------------------
class Snake:
    def __init__(self):
        self.coordinates = []
        self.squares = []
        for i in range(0, BODY_PARTS):
            self.coordinates.append([GAME_WIDTH/2, GAME_HEIGHT/2])

        for index, (x, y) in enumerate(self.coordinates):
            color = HEAD_COLOR if index == 0 else BODY_COLOR
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=color)
            self.squares.append(square)

class Food:
    def __init__(self):
        while True:
            x = random.randint(0, int(GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
            y = random.randint(0, int(GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
            
            # جلوگیری از افتادن غذا روی موانع
            if not any(obs[0] == x and obs[1] == y for obs in obstacles.coordinates):
                break
                
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

class Obstacles:
    def __init__(self):
        self.coordinates = []
        for _ in range(NUM_OBSTACLES):
            x = random.randint(0, int(GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
            y = random.randint(0, int(GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
            # جلوگیری از قرار گرفتن مانع در مرکز بازی (محل شروع مار)
            if not (GAME_WIDTH/2 - 50 < x < GAME_WIDTH/2 + 50 and GAME_HEIGHT/2 - 50 < y < GAME_HEIGHT/2 + 50):
                self.coordinates.append([x, y])
                canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=OBSTACLE_COLOR)

# --------------------
window = Tk()
window.title("SNAKE GAME")
window.resizable(False, False)

# فریم بالای صفحه برای دکمه‌ها
top_frame = Frame(window)
top_frame.pack(fill=X, pady=5)

label = Label(top_frame, text=f"Score: {score}", font=("Arial Black", 20))
label.pack(side=LEFT, padx=20)

Button(top_frame, text="⚙️ Settings", font=("Arial", 12), command=open_settings).pack(side=RIGHT, padx=10)
Button(top_frame, text="🔄 Restart", fg="red", font=("Arial", 12), command=restart_program).pack(side=RIGHT, padx=5)

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

# وسط‌چین کردن پنجره
window.update()
x = int((window.winfo_screenwidth() / 2) - (window.winfo_width() / 2))
y = int((window.winfo_screenheight() / 2) - (window.winfo_height() / 2))
window.geometry(f"{window.winfo_width()}x{window.winfo_height()}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

obstacles = Obstacles()
snake = Snake()
food = Food()
next_turn(snake, food)

window.mainloop()