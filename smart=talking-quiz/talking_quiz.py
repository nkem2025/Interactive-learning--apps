import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
import pygame
import threading
import os
import time

# -----------------------------
# INIT AUDIO ENGINE
# -----------------------------
pygame.mixer.init()

# -----------------------------
# SAFE SPEAK FUNCTION
# -----------------------------
def speak(text):

    def run():

        try:
            # UNIQUE FILE NAME EVERY TIME (VERY IMPORTANT FIX)
            filename = f"voice_{int(time.time()*1000)}.mp3"

            tts = gTTS(text=text, lang='en')
            tts.save(filename)

            # STOP ANY PREVIOUS SOUND
            pygame.mixer.music.stop()

            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()

            # WAIT UNTIL FINISHED
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)

            # REMOVE FILE AFTER PLAY
            if os.path.exists(filename):
                os.remove(filename)

        except Exception as e:
            print("Voice Error:", e)

    threading.Thread(target=run).start()


# -----------------------------
# QUIZ DATA
# -----------------------------
quiz_data = [
    {
        "question": "What is the capital of Nigeria?",
        "options": ["Lagos", "Abuja", "Kano", "Port Harcourt"],
        "answer": "Abuja"
    },
    {
        "question": "Which language is used for AI?",
        "options": ["Python", "HTML", "CSS", "Java"],
        "answer": "Python"
    },
    {
        "question": "How many days are in a week?",
        "options": ["5", "7", "10", "12"],
        "answer": "7"
    }
]

# -----------------------------
# WINDOW
# -----------------------------
root = tk.Tk()
root.title("Talking Quiz App")
root.geometry("700x600")
root.configure(bg="lightblue")

# -----------------------------
# INTRO (FIXED TIMING)
# -----------------------------
def intro():
    speak("Welcome to the Smart Talking Quiz Application")

root.after(1200, intro)

# -----------------------------
# SCROLL AREA
# -----------------------------
frame = tk.Frame(root)
frame.pack(fill="both", expand=1)

canvas = tk.Canvas(frame, bg="lightblue")
canvas.pack(side="left", fill="both", expand=1)

scrollbar = tk.Scrollbar(frame, command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

quiz_frame = tk.Frame(canvas, bg="lightblue")
canvas.create_window((0,0), window=quiz_frame, anchor="nw")

quiz_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# -----------------------------
# TITLE
# -----------------------------
tk.Label(
    quiz_frame,
    text="SMART TALKING QUIZ",
    font=("Arial", 22, "bold"),
    bg="lightblue"
).pack(pady=15)

# -----------------------------
# ANSWERS STORAGE
# -----------------------------
answers = []

# -----------------------------
# QUESTIONS
# -----------------------------
for i, q in enumerate(quiz_data):

    tk.Button(
        quiz_frame,
        text=f"{i+1}. {q['question']}",
        font=("Arial", 14, "bold"),
        bg="white",
        wraplength=600,
        justify="left",
        command=lambda x=q["question"]: speak(x)
    ).pack(fill="x", padx=20, pady=10)

    var = tk.StringVar()
    answers.append(var)

    for opt in q["options"]:
        tk.Radiobutton(
            quiz_frame,
            text=opt,
            variable=var,
            value=opt,
            bg="lightblue",
            command=lambda x=opt: speak(x)
        ).pack(anchor="w", padx=40)

# -----------------------------
# SCORE FUNCTION
# -----------------------------
def check():

    score = 0

    for i in range(len(quiz_data)):
        if answers[i].get() == quiz_data[i]["answer"]:
            score += 1

    result = f"You scored {score} out of {len(quiz_data)}"

    messagebox.showinfo("Result", result)

    speak(result)

# -----------------------------
# SUBMIT
# -----------------------------
tk.Button(
    quiz_frame,
    text="SUBMIT QUIZ",
    bg="green",
    fg="white",
    font=("Arial", 16, "bold"),
    command=check
).pack(pady=25)

# -----------------------------
# RUN
# -----------------------------
root.mainloop()
