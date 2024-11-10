# PUB QUIZ
from load_questions import load_questions 

def welcome():
    print("*******Welcome to the Pub Quiz!*******")
    print("Answer each question by entering the corresponding letter for the correct choice.")

# ASK QUESTION FUNCTION
def ask_question(question_data):
    print(f"\n{question_data['question']}")
    for option in question_data["options"]:
        print(option)
    
    # USER INPUT & VALIDATION
    user_answer = input("Enter your answer (A, B, C, or D): ").upper()
    while user_answer not in ["A", "B", "C", "D"]:
        print("Invalid choice. Please select A, B, C, or D.")
        user_answer = input("Enter your answer (A, B, C, or D): ").upper()
        
    
    return user_answer == question_data["answer"]
    
# CALCULATE SCORE
def calculate_score(questions):
    score = 0
    for question_data in questions:
        if ask_question(question_data):
            score += 1
    return score

# Display results
def display_results(score, total_questions):
    print("\n*******Results*******")
    print(f"Your score: {score}/{total_questions}")
    if score == total_questions:
        print("NERD!!!!")
    elif score >= total_questions / 2:
        print("Good effort!")
    else:
        print("Try again, you got this.")

# TY FUNCTION
def display_thank_you():
    print("\nThanks for taking the quiz, NOW GET AAAT MOII PUB!.")

# MAIN FUNCTION
def main():
    welcome()
    questions = load_questions()
    score = calculate_score(questions)
    display_results(score, len(questions))
    display_thank_you()

if __name__ == "__main__":
    main()
