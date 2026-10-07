questions = [
    {"question": "What is the capital of Japan?", "answer": "tokyo"},
    {"question": "What is 2 + 2 * 2?", "answer": "6"},
    {"question": "What language are we learning?", "answer": "python"},
    {"question": "what is the capital of Karnataka", "answer": "bangalore"}
]

def run_quiz(questions) :
    score = 0
    print("Lets start!")

    for q in questions:
        answer = input(f"{q['question']} ")
        if answer == q['answer'] :
            print("Correct answer")
            score+=1
        else :
            print(f"Wrong!, the answer is {q['answer']}")
    return score


def get_percentage(score) :
    percentage = score / len(questions) * 100
    return percentage

def get_grade(percentage) :
    if percentage >= 90 :
        return "A"
    elif percentage >= 75 :
        return "B"
    elif percentage >= 50 :
        return "C"
    else :
        return "F"


def get_message(grade) :
    if grade == "A" :
        return "Excellent!"
    elif grade == "B" :
        return "Good"
    elif grade == "C" :
        return "Bad"
    elif grade == "F" :
        return "Better luck next time"

print("Welcome to the Quiz")
score = run_quiz(questions)
percentage = get_percentage(score)
grade = get_grade(percentage)
message = get_message(grade)

print("------------------------")
print("Quiz results:")
print(f"You have scored {score} marks out of {len(questions)}.")
print(f"Which brings up a percentage of {percentage} & grade of {grade}")
print(f"{message} \nThank you")
print("------------------------")



