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
    if "wrong" in question_object.keys():  # We will only display multiple choice if there are wrong answers
        letters = "ABCDEFG"  # This is a string, so we can iterate over it to get A, B, C, etc.
        options = question_object["wrong"] + [question_object["answer"][0]]  # Add the correct answer to the list of wrong answers
        random.shuffle(options)  # Shuffle the options so the correct answer isn't always the last one
        for item in zip(letters, options):  # zip() lets us iterate over two lists at the same time, an `item` will be a tuple of (letter, answer)
            letter = item[0]  # This is the letter, like "A"
            option = item[1]  # This is one of the possible options, like "Paris"
            if (option.lower() in question_object["answer"]):  # If this is the correct answer...
                question_object["answer"].append(letter.lower())  # ...add the letter to the list of possible answers
            option = "{}. {}".format(letter, option.capitalize())  # This will format the option to be "A. Option"
            print(option)
    score = check_answer(question_object["answer"], current_score)
    display_score(score)
    return score


questions_file = open("questions.json", "r")
questions = json.load(questions_file)
questions_file.close()

score = 0
random.shuffle(questions)  # Shuffle the questions so they aren't always in the same order
for question in questions:
    score = ask_question(question, score)

print("Game over, thanks for playing!")
