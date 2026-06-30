import tkinter as tk
from tkinter import messagebox
import pygame

# =====================================
# INITIALIZE SOUND
# =====================================

pygame.mixer.init()

CORRECT_SOUND = "sounds/correct.wav"
WRONG_SOUND = "sounds/wrong.wav"
WARNING_SOUND = "sounds/warning.wav"
BACKGROUND_SOUND = "sounds/background.mp3"

# Play background music forever
pygame.mixer.music.load(BACKGROUND_SOUND)
pygame.mixer.music.play(-1)

# =====================================
# QUESTIONS
# =====================================

questions = [

    {
        "question":"Who built the ark?",
        "options":["Moses","Noah","David","Paul"],
        "answer":"Noah"
    },

    {
        "question":"Who killed Goliath?",
        "options":["David","Peter","John","Abraham"],
        "answer":"David"
    },

    {
        "question":"Who was swallowed by a great fish?",
        "options":["Jonah","Paul","Samuel","Isaiah"],
        "answer":"Jonah"
    },

    {
        "question":"How many disciples did Jesus have?",
        "options":["10","11","12","13"],
        "answer":"12"
    },

    {
        "question":"Where was Jesus born?",
        "options":["Jerusalem","Bethlehem","Nazareth","Egypt"],
        "answer":"Bethlehem"
    },

    {
        "question":"Who led the Israelites out of Egypt?",
        "options":["Moses","David","Peter","Paul"],
        "answer":"Moses"
    },

    {
        "question":"What was the first book of the Bible?",
        "options":["Genesis","Exodus","Psalms","Matthew"],
        "answer":"Genesis"
    },

    {
        "question":"Who was thrown into the lions' den?",
        "options":["Daniel","Joseph","Noah","Elijah"],
        "answer":"Daniel"
    }

]

# =====================================
# MAIN WINDOW
# =====================================

root = tk.Tk()
root.title("Bible Quiz Challenge")
root.geometry("1000x650")
root.config(bg="#e6f2ff")

# =====================================
# VARIABLES
# =====================================

score = 0
current_question = 0

quiz_time = 180
question_time = 20

selected_option = tk.StringVar()

quiz_timer_id = None
question_timer_id = None

# =====================================
# FRAMES
# =====================================

intro_frame = tk.Frame(root,bg="#e6f2ff")
quiz_frame = tk.Frame(root,bg="white")
answer_frame = tk.Frame(root,bg="#fff7cc")
result_frame = tk.Frame(root,bg="#d9ffd9")

for frame in (
    intro_frame,
    quiz_frame,
    answer_frame,
    result_frame
):
    frame.place(relwidth=1,relheight=1)

# =====================================
# SHOW FRAME
# =====================================

def show_frame(frame):
    frame.tkraise()

# =====================================
# INTRODUCTION PAGE
# =====================================

title_label = tk.Label(
    intro_frame,
    text="📖 BIBLE QUIZ CHALLENGE 📖",
    font=("Arial",30,"bold"),
    bg="#e6f2ff",
    fg="darkblue"
)
title_label.pack(pady=40)

intro_text = tk.Label(
    intro_frame,
    text=
    "Welcome to the Bible Quiz Challenge!\n\n"
    "Answer Bible Questions.\n"
    "Earn Points.\n"
    "Beat the Timer.\n"
    "Become a Bible Champion!",
    font=("Arial",18),
    bg="#e6f2ff"
)
intro_text.pack(pady=20)

start_button = tk.Button(
    intro_frame,
    text="START QUIZ",
    font=("Arial",18,"bold"),
    bg="green",
    fg="white",
    width=15,
    command=lambda:start_quiz()
)
start_button.pack(pady=40)

# =====================================
# QUIZ PAGE
# =====================================

score_label = tk.Label(
    quiz_frame,
    text="Score: 0",
    font=("Arial",16,"bold"),
    bg="white"
)
score_label.pack(pady=10)

quiz_timer_label = tk.Label(
    quiz_frame,
    text="Quiz Time: 180",
    font=("Arial",16,"bold"),
    bg="white",
    fg="red"
)
quiz_timer_label.pack()

question_timer_label = tk.Label(
    quiz_frame,
    text="Question Time: 20",
    font=("Arial",16,"bold"),
    bg="white",
    fg="blue"
)
question_timer_label.pack()

question_label = tk.Label(
    quiz_frame,
    text="",
    wraplength=700,
    font=("Arial",22,"bold"),
    bg="white"
)
question_label.pack(pady=40)

option_buttons = []

for i in range(4):

    rb = tk.Radiobutton(
        quiz_frame,
        text="",
        variable=selected_option,
        value="",
        font=("Arial",16),
        bg="white"
    )

    rb.pack(anchor="w",padx=250,pady=5)

    option_buttons.append(rb)

submit_button = tk.Button(
    quiz_frame,
    text="Submit Answer",
    font=("Arial",16,"bold"),
    bg="orange",
    command=lambda:check_answer()
)

submit_button.pack(pady=30)

# =====================================
# ANSWER PAGE
# =====================================

answer_label = tk.Label(
    answer_frame,
    text="",
    font=("Arial",24,"bold"),
    bg="#fff7cc"
)
answer_label.pack(pady=80)

next_button = tk.Button(
    answer_frame,
    text="NEXT QUESTION",
    font=("Arial",16,"bold"),
    command=lambda:next_question()
)
next_button.pack()

# =====================================
# RESULT PAGE
# =====================================

result_label = tk.Label(
    result_frame,
    text="",
    font=("Arial",24,"bold"),
    bg="#d9ffd9"
)
result_label.pack(pady=100)

# =====================================
# LOAD QUESTION
# =====================================

def load_question():

    global question_time

    question_time = 20

    q = questions[current_question]

    question_label.config(
        text=q["question"]
    )

    selected_option.set("")

    for i, option in enumerate(q["options"]):

        option_buttons[i].config(
            text=option,
            value=option
        )

    update_question_timer()

# =====================================
# QUIZ TIMER
# =====================================

def update_quiz_timer():

    global quiz_time
    global quiz_timer_id

    quiz_timer_label.config(
        text=f"Quiz Time: {quiz_time}"
    )

    if quiz_time <= 0:
        show_result()
        return

    quiz_time -= 1

    quiz_timer_id = root.after(
        1000,
        update_quiz_timer
    )

# =====================================
# QUESTION TIMER
# =====================================

def update_question_timer():

    global question_time
    global question_timer_id

    question_timer_label.config(
        text=f"Question Time: {question_time}"
    )

    if question_time <= 5 and question_time > 0:
        pygame.mixer.Sound(
            WARNING_SOUND
        ).play()

    if question_time <= 0:
        check_answer()
        return

    question_time -= 1

    question_timer_id = root.after(
        1000,
        update_question_timer
    )

# =====================================
# START QUIZ
# =====================================

def start_quiz():

    show_frame(quiz_frame)

    update_quiz_timer()

    load_question()

# =====================================
# CHECK ANSWER
# =====================================

def check_answer():

    global score

    if question_timer_id:
        root.after_cancel(question_timer_id)

    user_answer = selected_option.get()

    correct_answer = questions[current_question]["answer"]

    if user_answer == correct_answer:

        score += 1

        pygame.mixer.Sound(
            CORRECT_SOUND
        ).play()

        answer_label.config(
            text=
            f"✅ CORRECT!\n\n"
            f"Answer: {correct_answer}"
        )

    else:

        pygame.mixer.Sound(
            WRONG_SOUND
        ).play()

        answer_label.config(
            text=
            f"❌ WRONG\n\n"
            f"Correct Answer:\n{correct_answer}"
        )

    score_label.config(
        text=f"Score: {score}"
    )

    show_frame(answer_frame)

# =====================================
# NEXT QUESTION
# =====================================

def next_question():

    global current_question

    current_question += 1

    if current_question < len(questions):

        show_frame(quiz_frame)

        load_question()

    else:

        show_result()

# =====================================
# SHOW RESULT
# =====================================

def show_result():

    pygame.mixer.music.stop()

    total = len(questions)

    percentage = (score / total) * 100

    if percentage >= 80:
        grade = "EXCELLENT 🏆"

    elif percentage >= 60:
        grade = "VERY GOOD ⭐"

    elif percentage >= 40:
        grade = "GOOD 👍"

    else:
        grade = "TRY AGAIN 😊"

    result_label.config(

        text=
        f"QUIZ COMPLETED\n\n"
        f"Score: {score}/{total}\n\n"
        f"Percentage: {percentage:.0f}%\n\n"
        f"{grade}"

    )

    show_frame(result_frame)

# =====================================
# START APP
# =====================================

show_frame(intro_frame)

root.mainloop()
 
