import tkinter as tk
from load_questions import load_questions

# WELCOME FUNCTION
def welcome_screen():
    welcome_label.config(text="*******Welcome to the Pub Quiz!*******")
    instructions_label.config(text="Answer each question by clicking on the correct button.")

# QUESTION DISPLAY FUNCTION
def display_question(question_data):
    question_label.config(text=question_data['question'])
    option_a_button.config(text=question_data["options"][0], state="normal")
    option_b_button.config(text=question_data["options"][1], state="normal")
    option_c_button.config(text=question_data["options"][2], state="normal")
    option_d_button.config(text=question_data["options"][3], state="normal")

# INPUT VALIDATION FUNCTION
def answer_question(answer):
    global current_question, score
    
    if answer == current_question["answer"]:
        score += 1
    
    option_a_button.config(state="disabled")
    option_b_button.config(state="disabled")
    option_c_button.config(state="disabled")
    option_d_button.config(state="disabled")
    
    # AUTOMATIC NEXT QUESTION
    next_question()

# NEXT QUESTION FUNCTION
def next_question():
    global current_question_index, current_question
    current_question_index += 1
    
    if current_question_index < len(questions):
        current_question = questions[current_question_index]
        display_question(current_question)
    else:
        show_results()

# RESULTS DISPLAY FUNCTION
def show_results():
    score_label.config(text=f"Your score: {score}/{len(questions)}")
    if score == len(questions):
        result_label.config(text="NERD!!!!")
    elif score >= len(questions) / 2:
        result_label.config(text="Good effort!")
    else:
        result_label.config(text="Try again, you got this.")
    
    finish_button.config(state="normal")

# TY FUNCTION
def finish_quiz():
    thank_you_label.config(text="Thanks for taking the quiz, NOW GET AAAT MOII PUB!")
    finish_button.config(state="disabled")

# LOAD QUESTIONS FROM EXTERNAL FUNCTION
questions = load_questions()
current_question_index = 0
score = 0
current_question = questions[current_question_index]

# TKINTER
root = tk.Tk()
root.title("Pub Quiz")
root.configure(bg="black")

# FONT
font = ("Impact", 20)

# WIDGETS
welcome_label = tk.Label(root, text="", fg="white", bg="black", font=font)
instructions_label = tk.Label(root, text="", fg="white", bg="black", font=font)
question_label = tk.Label(root, text="", fg="red", bg="black", font=font)
option_a_button = tk.Button(root, text="", fg="black", bg="white", font=font, command=lambda: answer_question("A"))
option_b_button = tk.Button(root, text="", fg="black", bg="white", font=font, command=lambda: answer_question("B"))
option_c_button = tk.Button(root, text="", fg="black", bg="white", font=font, command=lambda: answer_question("C"))
option_d_button = tk.Button(root, text="", fg="black", bg="white", font=font, command=lambda: answer_question("D"))
finish_button = tk.Button(root, text="Finish Quiz", fg="black", bg="white", font=font, state="disabled", command=finish_quiz)
result_label = tk.Label(root, text="", fg="white", bg="black", font=font)
score_label = tk.Label(root, text="", fg="white", bg="black", font=font)
thank_you_label = tk.Label(root, text="", fg="white", bg="black", font=font)

# WIDGET PLACEMENT
welcome_label.pack(pady=20)
instructions_label.pack(pady=10)
question_label.pack(pady=10)
option_a_button.pack(pady=5)
option_b_button.pack(pady=5)
option_c_button.pack(pady=5)
option_d_button.pack(pady=5)
result_label.pack(pady=10)
score_label.pack(pady=10)
finish_button.pack(pady=10)
thank_you_label.pack(pady=20)


welcome_screen()

display_question(current_question)

root.mainloop()
