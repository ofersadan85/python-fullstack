# A trivia game


def display_score(score):
    print("Your score is now:", score)
    if score == 0:
        print("This is not great!")


def check_answer(possible_answers, score):
    user_answer = input("Your answer: ")
    exit_words = ["exit", "quit", "q", "x"]
    if user_answer.lower() in exit_words:
           exit()
    if user_answer.lower() in possible_answers:
        score = score + 1
        print("Correct!")
    else:
        print("Incorrect!")
    return score

def ask_question(question_text, answer, current_score):
    print(question_text)
    score = check_answer(answer, current_score)
    display_score(score)
    return score

question1 = "Question 1: What is the capital of France?"
answer1 = ["paris"]
question2 = """Question 2: What is the capital of Germany?
A. Berlin
B. Munich
C. Hamburg
D. Frankfurt"""
answer2 = ["a", "berlin"]

number_of_tries = 0
while number_of_tries < 3:
    print("STARTING A NEW GAME")
    score = ask_question(question1, answer1, 0)
    score = ask_question(question2, answer2, score)
    display_score(score)
    number_of_tries = number_of_tries + 1

print("Game over, thanks for playing!")
