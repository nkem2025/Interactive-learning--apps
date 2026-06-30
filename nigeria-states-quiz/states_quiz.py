import tkinter as tk
import random

# ALL STATES AND CAPITALS
capitals = {"Abia": "Umuahia", "Adamawa": "Yola", "Akwa Ibom": "Uyo", "Anambra": "Awka", "Bauchi": "Bauchi",
    "Bayelsa": "Yenagoa", "Benue": "Makurdi", "Borno": "Maiduguri", "Cross River": "Calabar",
    "Delta": "Asaba", "Ebonyi": "Abakaliki", "Edo": "Benin City", "Ekiti": "Ado Ekiti", "Enugu": "Enugu",
    "Gombe": "Gombe", "Imo": "Owerri", "Jigawa": "Dutse", "Kaduna": "Kaduna", "Kano": "Kano",
    "Katsina": "Katsina", "Kebbi": "Birnin Kebbi", "Kogi": "Lokoja", "Kwara": "Ilorin", "Lagos": "Ikeja",
    "Nasarawa": "Lafia", "Niger": "Minna", "Ogun": "Abeokuta", "Ondo": "Akure", "Osun": "Osogbo",
    "Oyo": "Ibadan", "Plateau": "Jos", "Rivers": "Port Harcourt", "Sokoto": "Sokoto", "Taraba": "Jalingo",
    "Yobe": "Damaturu", "Zamfara": "Gusau", "Federal Capital Territory": "Abuja"
}

# =========================
# GENERATE QUESTIONS
# =========================

quiz_data = []

states = list(capitals.keys())

for state in states:

    correct_answer = capitals[state]

    wrong_answers = list(capitals.values())
    wrong_answers.remove(correct_answer)

    options = random.sample(wrong_answers, 3)
    options.append(correct_answer)

    random.shuffle(options)

    question = {
        "question": f"What is the capital of {state} State?",
        "options": options,
        "answer": correct_answer
    }

    quiz_data.append(question)

# RANDOMIZE QUESTIONS
random.shuffle(quiz_data)

# LIMIT QUESTIONS
quiz_data = quiz_data[:20]

# =========================
# TKINTER WINDOW
# =========================

root = tk.Tk()
root.title("Nigeria CBT Quiz")

# FULL SCREEN
root.attributes("-fullscreen", True)

# ESC TO EXIT
root.bind("<Escape>", lambda event: root.destroy())

question_index = 0
score = 0

# =========================
# QUESTION LABEL
# =========================

question_label = tk.Label(
    root,
    text="",
    font=("Arial", 28, "bold"),
    wraplength=1000,
    pady=40
)

question_label.pack()

# =========================
# ANSWER CHECKER
# =========================

def check_answer(selected):

    global question_index
    global score

    correct = quiz_data[question_index]["answer"]

    if selected == correct:
        score += 1

    question_index += 1

    if question_index < len(quiz_data):
        load_question()
    else:
        show_result()

# =========================
# LOAD QUESTIONS
# =========================

def load_question():

    question = quiz_data[question_index]

    question_label.config(
        text=f"Question {question_index + 1}\n\n{question['question']}"
    )

    for i in range(4):

        buttons[i].config(
            text=question["options"][i],
            command=lambda option=question["options"][i]: check_answer(option)
        )

# =========================
# SHOW RESULT
# =========================

def show_result():

    question_label.config(
        text=f"QUIZ COMPLETED\n\nSCORE: {score} / {len(quiz_data)}",
        font=("Arial", 40, "bold")
    )

    for btn in buttons:
        btn.destroy()

# =========================
# OPTION BUTTONS
# =========================

buttons = []

for i in range(4):

    btn = tk.Button(
        root,
        text="",
        font=("Arial", 24),
        width=25,
        height=2,
        bg="lightblue"
    )

    btn.pack(pady=15)

    buttons.append(btn)

# START QUIZ
load_question()

# RUN WINDOW
root.mainloop()
