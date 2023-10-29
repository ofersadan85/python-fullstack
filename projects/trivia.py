import json
import random


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


def ask_question(question_object, current_score):
    print(question_object["text"])
    if "wrong" in question_object.keys():
        letters = "ABCDEFG"
        options = question_object["wrong"] + [question_object["answer"][0].capitalize()]
        random.shuffle(options)
        for option in zip(options, letters):
            if option[0].lower() in question_object["answer"]:
                question_object["answer"].append(option[1].lower())
            option = "{}. {}".format(option[1], option[0])
            print(option)
    score = check_answer(question_object["answer"], current_score)
    display_score(score)
    return score


questions_file = open("questions.json", "r")
questions = json.load(questions_file)
questions_file.close()

score = 0
random.shuffle(questions)
for question in questions:
    score = ask_question(question, score)

print("Game over, thanks for playing!")
