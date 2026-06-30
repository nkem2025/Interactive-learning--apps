# ============================================================
# PRIMARY 5 MULTIPLICATION QUIZ CHALLENGE
# PART 1
#
# Imports
# Audio System
# Utility Functions
# Introduction Window
# Registration Window
# ============================================================

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageGrab
import pygame
import random
import os
import datetime
import uuid

# ------------------------------------------------------------
# AUDIO INITIALIZATION
# ------------------------------------------------------------

pygame.init()

try:
    pygame.mixer.init()
    AUDIO_AVAILABLE = True
except:
    AUDIO_AVAILABLE = False

# ------------------------------------------------------------
# FILES
# ------------------------------------------------------------

LOGO_FILE = "logo.png"
MUSIC_FILE = "music.mp3"
CORRECT_SOUND = "cheer.wav"
WRONG_SOUND = "boo.wav"

# ------------------------------------------------------------
# APPLICATION COLORS
# ------------------------------------------------------------

NAVY = "#0A2342"
GOLD = "#D4AF37"
WHITE = "#FFFFFF"
LIGHT_BG = "#F4F6F8"
GREEN = "#1E8E3E"
RED = "#C62828"

# ------------------------------------------------------------
# AUDIO FUNCTIONS
# ------------------------------------------------------------

def play_music():
    """Play background music"""

    if not AUDIO_AVAILABLE:
        return

    try:
        if os.path.exists(MUSIC_FILE):
            pygame.mixer.music.load(MUSIC_FILE)
            pygame.mixer.music.play(-1)
    except:
        pass


def stop_music():
    """Stop music"""

    if not AUDIO_AVAILABLE:
        return

    try:
        pygame.mixer.music.stop()
    except:
        pass


def play_correct():
    """Play correct answer sound"""

    if not AUDIO_AVAILABLE:
        return

    try:
        if os.path.exists(CORRECT_SOUND):
            sound = pygame.mixer.Sound(CORRECT_SOUND)
            sound.play()
    except:
        pass


def play_wrong():
    """Play wrong answer sound"""

    if not AUDIO_AVAILABLE:
        return

    try:
        if os.path.exists(WRONG_SOUND):
            sound = pygame.mixer.Sound(WRONG_SOUND)
            sound.play()
    except:
        pass


# ------------------------------------------------------------
# GLOBAL VARIABLES
# ------------------------------------------------------------

student_name = ""
student_class = ""

questions = []
current_question = 0
score = 0

timer_seconds = 60
timer_job = None

# ------------------------------------------------------------
# CERTIFICATE NUMBER
# ------------------------------------------------------------

def generate_certificate_number():

    return "CERT-" + str(uuid.uuid4())[:8].upper()


# ------------------------------------------------------------
# LOGO LOADER
# ------------------------------------------------------------

def load_logo(width=120, height=120):

    try:
        if os.path.exists(LOGO_FILE):

            img = Image.open(LOGO_FILE)
            img = img.resize((width, height))

            return ImageTk.PhotoImage(img)

    except:
        pass

    return None


# ------------------------------------------------------------
# MAIN WINDOW
# ------------------------------------------------------------

root = tk.Tk()

root.title("Primary 6 Multiplication Quiz Challenge")

root.geometry("1000x700")
root.configure(bg=NAVY)
root.resizable(False, False)

# ------------------------------------------------------------
# INTRODUCTION SCREEN
# ------------------------------------------------------------

intro_frame = tk.Frame(
    root,
    bg=NAVY
)

intro_frame.pack(
    fill="both",
    expand=True
)

# ------------------------------------------------------------
# SCHOOL LOGO
# ------------------------------------------------------------

logo_image = load_logo(130, 130)

if logo_image:

    logo_label = tk.Label(
        intro_frame,
        image=logo_image,
        bg=NAVY
    )

    logo_label.pack(
        pady=15
    )

# ------------------------------------------------------------
# SCHOOL NAME
# ------------------------------------------------------------

school_label = tk.Label(
    intro_frame,
    text="BLESSED TANSI CATHOLIC SCHOOL - TEAM BOYS", 
    font=("Arial", 24, "bold"),
    fg=GOLD,
    bg=NAVY
)

school_label.pack()

# ------------------------------------------------------------
# PROJECT TITLE
# ------------------------------------------------------------

title_label = tk.Label(
    intro_frame,
    text="PRIMARY 6 MULTIPLICATION QUIZ CHALLENGE",
    font=("Arial", 22, "bold"),
    fg=WHITE,
    bg=NAVY
)

title_label.pack(
    pady=15
)

# ------------------------------------------------------------
# DESCRIPTION
# ------------------------------------------------------------

description = """
Welcome to the Primary 6 Multiplication Quiz Challenge.

Answer as many multiplication questions as possible
before the timer runs out.
"""

description_label = tk.Label(
    intro_frame,
    text=description,
    font=("Arial", 13),
    fg=WHITE,
    bg=NAVY,
    justify="center"
)

description_label.pack(
    pady=10
)

# ------------------------------------------------------------
# INSTRUCTIONS
# ------------------------------------------------------------

# ------------------------------------------------------------
# REGISTRATION WINDOW
# ------------------------------------------------------------

def open_registration():

    intro_frame.pack_forget()

    registration_frame.pack(
        fill="both",
        expand=True
    )


# ------------------------------------------------------------
# START BUTTON
# ------------------------------------------------------------

start_btn = tk.Button(
    intro_frame,
    text="START QUIZ",
    font=("Arial", 18, "bold"),
    bg=GOLD,
    fg=NAVY,
    width=18,
    height=2,
    command=open_registration
)

start_btn.pack(
    pady=25
)

# ------------------------------------------------------------
# REGISTRATION FRAME
# ------------------------------------------------------------

registration_frame = tk.Frame(
    root,
    bg=LIGHT_BG
)

# ------------------------------------------------------------
# REGISTRATION TITLE
# ------------------------------------------------------------

welcome_label = tk.Label(
    registration_frame,
    text="Student Registration",
    font=("Arial", 24, "bold"),
    fg=NAVY,
    bg=LIGHT_BG
)

welcome_label.pack(
    pady=30
)

# ------------------------------------------------------------
# NAME FIELD
# ------------------------------------------------------------

name_label = tk.Label(
    registration_frame,
    text="Student Name",
    font=("Arial", 14, "bold"),
    bg=LIGHT_BG
)

name_label.pack()

name_entry = tk.Entry(
    registration_frame,
    font=("Arial", 15),
    width=30
)

name_entry.pack(
    pady=10
)

# ------------------------------------------------------------
# CLASS FIELD
# ------------------------------------------------------------

class_label = tk.Label(
    registration_frame,
    text="Class",
    font=("Arial", 14, "bold"),
    bg=LIGHT_BG
)

class_label.pack()

class_entry = tk.Entry(
    registration_frame,
    font=("Arial", 15),
    width=30
)

class_entry.pack(
    pady=10
)

# ------------------------------------------------------------
# VALIDATION LABEL
# ------------------------------------------------------------

validation_label = tk.Label(
    registration_frame,
    text="",
    font=("Arial", 12, "bold"),
    bg=LIGHT_BG
)

validation_label.pack(
    pady=10
)

# ------------------------------------------------------------
# BEGIN QUIZ FUNCTION
# ------------------------------------------------------------

def begin_quiz():

    global student_name
    global student_class

    student_name = name_entry.get().strip()
    student_class = class_entry.get().strip()

    if student_name == "":
        validation_label.config(
            text="Please enter your name.",
            fg=RED
        )
        return

    if student_class == "":
        validation_label.config(
            text="Please enter your class.",
            fg=RED
        )
        return

    validation_label.config(
        text="",
        fg=GREEN
    )

    registration_frame.pack_forget()

    # PART 2 WILL START QUIZ HERE
    start_quiz()

# ------------------------------------------------------------
# BEGIN QUIZ BUTTON
# ------------------------------------------------------------

begin_btn = tk.Button(
    registration_frame,
    text="BEGIN QUIZ",
    font=("Arial", 16, "bold"),
    bg=GOLD,
    fg=NAVY,
    width=18,
    command=begin_quiz
)

begin_btn.pack(
    pady=20
)


# ============================================================
# PART 2
#
# Quiz Window
# Question Generation
# Timer Management
# Score System
# Sound Feedback
# Safe after() Handling
# ============================================================

# ------------------------------------------------------------
# QUIZ FRAME
# ------------------------------------------------------------

quiz_frame = tk.Frame(
    root,
    bg=WHITE
)

# ------------------------------------------------------------
# TOP BAR
# ------------------------------------------------------------

top_bar = tk.Frame(
    quiz_frame,
    bg=NAVY,
    height=70
)

top_bar.pack(
    fill="x"
)

# ------------------------------------------------------------
# TIMER LABEL
# ------------------------------------------------------------

timer_label = tk.Label(
    top_bar,
    text="Time: 60",
    font=("Arial", 16, "bold"),
    fg=GOLD,
    bg=NAVY
)

timer_label.pack(
    side="left",
    padx=20,
    pady=15
)

# ------------------------------------------------------------
# SCORE LABEL
# ------------------------------------------------------------

score_label = tk.Label(
    top_bar,
    text="Score: 0",
    font=("Arial", 16, "bold"),
    fg=WHITE,
    bg=NAVY
)

score_label.pack(
    side="right",
    padx=20,
    pady=15
)

# ------------------------------------------------------------
# QUESTION NUMBER LABEL
# ------------------------------------------------------------

question_number_label = tk.Label(
    quiz_frame,
    text="Question 1 of 20",
    font=("Arial", 18, "bold"),
    fg=NAVY,
    bg=WHITE
)

question_number_label.pack(
    pady=(40, 20)
)

# ------------------------------------------------------------
# QUESTION DISPLAY
# ------------------------------------------------------------

question_label = tk.Label(
    quiz_frame,
    text="",
    font=("Arial", 30, "bold"),
    fg=NAVY,
    bg=WHITE
)

question_label.pack(
    pady=20
)

# ------------------------------------------------------------
# ANSWER ENTRY
# ------------------------------------------------------------

answer_entry = tk.Entry(
    quiz_frame,
    font=("Arial", 24),
    justify="center",
    width=10
)

answer_entry.pack(
    pady=20
)

# ------------------------------------------------------------
# FEEDBACK LABEL
# ------------------------------------------------------------

feedback_label = tk.Label(
    quiz_frame,
    text="",
    font=("Arial", 16, "bold"),
    bg=WHITE
)

feedback_label.pack(
    pady=15
)

# ------------------------------------------------------------
# SUBMIT BUTTON
# ------------------------------------------------------------

submit_btn = tk.Button(
    quiz_frame,
    text="SUBMIT ANSWER",
    font=("Arial", 16, "bold"),
    bg=GOLD,
    fg=NAVY,
    width=18
)

submit_btn.pack(
    pady=20
)

# ------------------------------------------------------------
# QUESTION STORAGE
# ------------------------------------------------------------

correct_answers = []

# ------------------------------------------------------------
# GENERATE QUESTIONS
# ------------------------------------------------------------

def generate_questions():
    """
    Create 20 random multiplication questions
    from 2 x 2 to 12 x 12
    """

    global questions
    global correct_answers

    questions = []
    correct_answers = []

    for _ in range(20):

        num1 = random.randint(2, 12)
        num2 = random.randint(2, 12)

        questions.append((num1, num2))
        correct_answers.append(num1 * num2)

# ------------------------------------------------------------
# DISPLAY QUESTION
# ------------------------------------------------------------

def display_question():

    if current_question >= len(questions):
        end_quiz()
        return

    num1, num2 = questions[current_question]

    question_number_label.config(
        text=f"Question {current_question + 1} of 20"
    )

    question_label.config(
        text=f"{num1} × {num2} = ?"
    )

    answer_entry.delete(0, tk.END)
    answer_entry.focus()

# ------------------------------------------------------------
# SAFE TIMER
# ------------------------------------------------------------

def update_timer():

    global timer_seconds
    global timer_job

    if not quiz_frame.winfo_exists():
        return

    timer_label.config(
        text=f"Time: {timer_seconds}"
    )

    if timer_seconds <= 0:

        timer_label.config(
            text="Time Up!"
        )

        end_quiz()
        return

    timer_seconds -= 1

    timer_job = root.after(
        1000,
        update_timer
    )

# ------------------------------------------------------------
# CANCEL TIMER SAFELY
# ------------------------------------------------------------

def cancel_timer():

    global timer_job

    if timer_job is not None:

        try:
            root.after_cancel(timer_job)
        except:
            pass

        timer_job = None

# ------------------------------------------------------------
# NEXT QUESTION
# ------------------------------------------------------------

def next_question():

    global current_question

    current_question += 1

    feedback_label.config(text="")

    display_question()

# ------------------------------------------------------------
# SUBMIT ANSWER
# ------------------------------------------------------------

def submit_answer():

    global score

    if current_question >= len(correct_answers):
        return

    answer = answer_entry.get().strip()

    if answer == "":
        feedback_label.config(
            text="Please enter an answer.",
            fg=RED
        )
        return

    try:
        answer = int(answer)

    except:

        feedback_label.config(
            text="Numbers only.",
            fg=RED
        )
        return

    correct = correct_answers[current_question]

    # --------------------------------------------------------
    # CORRECT ANSWER
    # --------------------------------------------------------

    if answer == correct:

        score += 1

        score_label.config(
            text=f"Score: {score}"
        )

        play_correct()

        feedback_label.config(
            text="✓ Correct! Great Job!",
            fg=GREEN
        )

    # --------------------------------------------------------
    # WRONG ANSWER
    # --------------------------------------------------------

    else:

        play_wrong()

        feedback_label.config(
            text=f"✗ Incorrect! Correct Answer = {correct}",
            fg=RED
        )

    # --------------------------------------------------------
    # AUTO NEXT
    # --------------------------------------------------------

    root.after(
        1500,
        next_question
    )

# ------------------------------------------------------------
# ENTER KEY SUPPORT
# ------------------------------------------------------------

answer_entry.bind(
    "<Return>",
    lambda event: submit_answer()
)

submit_btn.config(
    command=submit_answer
)

# ------------------------------------------------------------
# START QUIZ
# ------------------------------------------------------------

def start_quiz():

    global score
    global current_question
    global timer_seconds

    score = 0
    current_question = 0
    timer_seconds = 60

    score_label.config(
        text="Score: 0"
    )

    feedback_label.config(
        text=""
    )

    generate_questions()

    quiz_frame.pack(
        fill="both",
        expand=True
    )

    play_music()

    display_question()

    update_timer()

# ------------------------------------------------------------
# END QUIZ
# ------------------------------------------------------------

def end_quiz():

    cancel_timer()

    stop_music()

    if quiz_frame.winfo_exists():
        quiz_frame.pack_forget()

    # PART 3 WILL OPEN RESULTS WINDOW
    show_results()

# ============================================================
# PART 3
#
# Results Window
# Grade System
# Certificate Window
# Save PNG
# Save PDF
# Print Certificate
# Exit Program
# ============================================================

# ------------------------------------------------------------
# REPORTLAB PDF SUPPORT
# ------------------------------------------------------------

try:
    from reportlab.pdfgen import canvas
    PDF_AVAILABLE = True
except:
    PDF_AVAILABLE = False

# ------------------------------------------------------------
# RESULTS VARIABLES
# ------------------------------------------------------------

percentage = 0
grade = ""
remark = ""

# ------------------------------------------------------------
# GRADE CALCULATOR
# ------------------------------------------------------------

def calculate_grade(percent):

    if percent >= 90:
        return "A+", "Outstanding"

    elif percent >= 80:
        return "A", "Excellent"

    elif percent >= 70:
        return "B", "Very Good"

    elif percent >= 60:
        return "C", "Good"

    elif percent >= 50:
        return "D", "Fair"

    else:
        return "F", "Needs Improvement"


# ------------------------------------------------------------
# RESULTS FRAME
# ------------------------------------------------------------

results_frame = tk.Frame(
    root,
    bg=LIGHT_BG
)

# ------------------------------------------------------------
# RESULTS TITLE
# ------------------------------------------------------------

results_title = tk.Label(
    results_frame,
    text="QUIZ RESULTS",
    font=("Arial", 28, "bold"),
    fg=NAVY,
    bg=LIGHT_BG
)

results_title.pack(
    pady=20
)

# ------------------------------------------------------------
# RESULTS DISPLAY LABEL
# ------------------------------------------------------------

results_label = tk.Label(
    results_frame,
    text="",
    font=("Arial", 15),
    justify="left",
    bg=LIGHT_BG,
    fg=NAVY
)

results_label.pack(
    pady=20
)

# ------------------------------------------------------------
# GRADE LABEL
# ------------------------------------------------------------

grade_label = tk.Label(
    results_frame,
    text="",
    font=("Arial", 36, "bold"),
    fg=GOLD,
    bg=LIGHT_BG
)

grade_label.pack(
    pady=10
)

# ------------------------------------------------------------
# SHOW RESULTS
# ------------------------------------------------------------

def show_results():

    global percentage
    global grade
    global remark

    total_questions = len(questions)

    percentage = round(
        (score / total_questions) * 100
    )

    grade, remark = calculate_grade(
        percentage
    )

    results_text = f"""
Student Name : {student_name}

Class : {student_class}

Total Questions : {total_questions}

Correct Answers : {score}

Score : {score}/{total_questions}

Percentage : {percentage}%

Remark : {remark}
"""

    results_label.config(
        text=results_text
    )

    grade_label.config(
        text=f"GRADE: {grade}"
    )

    results_frame.pack(
        fill="both",
        expand=True
    )

# ------------------------------------------------------------
# OPEN CERTIFICATE
# ------------------------------------------------------------

def open_certificate():

    results_frame.pack_forget()

    build_certificate()

# ------------------------------------------------------------
# CERTIFICATE BUTTON
# ------------------------------------------------------------

certificate_btn = tk.Button(
    results_frame,
    text="VIEW CERTIFICATE",
    font=("Arial", 16, "bold"),
    bg=GOLD,
    fg=NAVY,
    width=20,
    command=open_certificate
)

certificate_btn.pack(
    pady=10
)

# ============================================================
# CERTIFICATE WINDOW
# ============================================================

certificate_frame = tk.Frame(
    root,
    bg=WHITE
)

certificate_number = generate_certificate_number()

certificate_canvas = None

# ------------------------------------------------------------
# BUILD CERTIFICATE
# ------------------------------------------------------------

def build_certificate():

    global certificate_canvas

    certificate_frame.pack(
        fill="both",
        expand=True
    )

    certificate_canvas = tk.Canvas(
        certificate_frame,
        width=900,
        height=600,
        bg="white",
        highlightthickness=0
    )

    certificate_canvas.pack(
        pady=0
    )

    # BORDER

    certificate_canvas.create_rectangle(
        15, 15, 885, 585,
        outline=GOLD,
        width=6
    )

    certificate_canvas.create_rectangle(
        30, 30, 870, 570,
        outline=NAVY,
        width=3
    )

    # LOGO

    try:

        if os.path.exists(LOGO_FILE):

            logo = Image.open(LOGO_FILE)
            logo = logo.resize((90, 90))

            cert_logo = ImageTk.PhotoImage(logo)

            certificate_canvas.logo = cert_logo

            certificate_canvas.create_image(
                450,
                90,
                image=cert_logo
            )

    except:
        pass

    # SCHOOL NAME

    certificate_canvas.create_text(
        450,
        170,
        text="BLESSED TANSI CATHOLIC SCHOOL",
        font=("Arial", 24, "bold"),
        fill=NAVY
    )

    # TITLE

    certificate_canvas.create_text(
        450,
        220,
        text="CERTIFICATE OF ACHIEVEMENT",
        font=("Times New Roman", 28, "bold"),
        fill=GOLD
    )

    certificate_canvas.create_text(
        450,
        270,
        text="This certificate is proudly awarded to",
        font=("Arial", 14),
        fill="black"
    )

    certificate_canvas.create_text(
        450,
        320,
        text=student_name.upper(),
        font=("Arial", 24, "bold"),
        fill=NAVY
    )

    certificate_canvas.create_text(
        450,
        360,
        text=f"Class: {student_class}",
        font=("Arial", 15),
        fill="black"
    )

    certificate_canvas.create_text(
        450,
        390,
        text=f"Score: {score}/20",
        font=("Arial", 15),
        fill="black"
    )

    certificate_canvas.create_text(
        450,
        420,
        text=f"Percentage: {percentage}%",
        font=("Arial", 15),
        fill="black"
    )

    certificate_canvas.create_text(
        450,
        450,
        text=f"Grade: {grade}",
        font=("Arial", 18, "bold"),
        fill=GOLD
    )

    certificate_canvas.create_text(
        450,
        480,
        text=f"Remark: {remark}",
        font=("Arial", 14),
        fill="black"
    )

    today = datetime.date.today()

    certificate_canvas.create_text(
        200,
        530,
        text=f"Date: {today}",
        font=("Arial", 12)
    )

    certificate_canvas.create_text(
        680,
        530,
        text=f"Certificate No: {certificate_number}",
        font=("Arial", 12)
    )

    certificate_canvas.create_line(
        340, 550,
        560, 550,
        width=2
    )

    certificate_canvas.create_text(
        450,
        565,
        text="Head Teacher Signature",
        font=("Arial", 11)
    )

    create_certificate_buttons()

# ------------------------------------------------------------
# SAVE PNG
# ------------------------------------------------------------

def save_png():

    try:

        filename = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Image", "*.png")]
        )

        if not filename:
            return

        x = root.winfo_rootx() + certificate_canvas.winfo_x()
        y = root.winfo_rooty() + certificate_canvas.winfo_y()

        x1 = x + certificate_canvas.winfo_width()
        y1 = y + certificate_canvas.winfo_height()

        image = ImageGrab.grab(
            bbox=(x, y, x1, y1)
        )

        image.save(filename)

    except:
        pass

# ------------------------------------------------------------
# SAVE PDF
# ------------------------------------------------------------

def save_pdf():

    if not PDF_AVAILABLE:
        return

    try:

        filename = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF File", "*.pdf")]
        )

        if not filename:
            return

        pdf = canvas.Canvas(filename)

        pdf.setFont("Helvetica-Bold", 20)
        pdf.drawString(
            150,
            800,
            "CERTIFICATE OF ACHIEVEMENT"
        )

        pdf.setFont("Helvetica", 14)

        pdf.drawString(
            100,
            730,
            f"Student Name: {student_name}"
        )

        pdf.drawString(
            100,
            700,
            f"Class: {student_class}"
        )

        pdf.drawString(
            100,
            670,
            f"Score: {score}/20"
        )

        pdf.drawString(
            100,
            640,
            f"Percentage: {percentage}%"
        )

        pdf.drawString(
            100,
            610,
            f"Grade: {grade}"
        )

        pdf.drawString(
            100,
            580,
            f"Remark: {remark}"
        )

        pdf.drawString(
            100,
            550,
            f"Certificate Number: {certificate_number}"
        )

        pdf.save()

    except:
        pass

# ------------------------------------------------------------
# PRINT CERTIFICATE
# ------------------------------------------------------------

def print_certificate():

    try:

        save_png()

    except:
        pass

# ------------------------------------------------------------
# EXIT PROGRAM
# ------------------------------------------------------------

def exit_program():

    stop_music()

    try:
        pygame.quit()
    except:
        pass

    root.destroy()

# ------------------------------------------------------------
# CERTIFICATE BUTTONS
# ------------------------------------------------------------

def create_certificate_buttons():

    button_frame = tk.Frame(
        certificate_frame,
        bg=WHITE
    )

    button_frame.pack(
        pady=10
    )

    tk.Button(
        button_frame,
        text="Save PNG",
        font=("Arial", 12, "bold"),
        bg=GOLD,
        fg=NAVY,
        command=save_png
    ).grid(
        row=0,
        column=0,
        padx=10
    )

    tk.Button(
        button_frame,
        text="Save PDF",
        font=("Arial", 12, "bold"),
        bg=GOLD,
        fg=NAVY,
        command=save_pdf
    ).grid(
        row=0,
        column=1,
        padx=10
    )

    tk.Button(
        button_frame,
        text="Print",
        font=("Arial", 12, "bold"),
        bg=GOLD,
        fg=NAVY,
        command=print_certificate
    ).grid(
        row=0,
        column=2,
        padx=10
    )

    tk.Button(
        button_frame,
        text="Exit Program",
        font=("Arial", 12, "bold"),
        bg="red",
        fg="white",
        command=exit_program
    ).grid(
        row=0,
        column=3,
        padx=10
    )

# ------------------------------------------------------------
# CLEAN EXIT
# ------------------------------------------------------------

def on_close():

    cancel_timer()
    stop_music()

    try:
        pygame.quit()
    except:
        pass

    root.destroy()

root.protocol(
    "WM_DELETE_WINDOW",
    on_close
)

# ------------------------------------------------------------
# START APPLICATION
# ------------------------------------------------------------

root.mainloop()
