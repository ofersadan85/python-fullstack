import json
import random


def display_score(score):
    print(f"Your score is now: {score}. {'This is not great!' if score == 0 else ''}")


class Question:
    def __init__(self, text, answer, wrong=False):
        self.text = text
        self.answer = answer
        self.wrong = wrong

    def __str__(self):
        return self.text

    def ask(self, current_score):
        print(self)
        letters = "ABCDEFG"
        if self.wrong:
            options = self.wrong + [self.answer[0]]
            random.shuffle(options)
            for item in zip(letters, options):
                # zip() - iterate over two lists at the same time
                # an `item` will be a tuple of (letter, answer)
                letter = item[0]  # This is the letter, like "A"
                option = item[1]  # This is one of the possible options, like "Paris"
                if option.lower() in self.answer:
                    # If this is the correct answer add the letter to the list answers
                    self.answer.append(letter.lower())
                option = f"{letter}. {option.capitalize()}"
                print(option)
        score = self.check_answer(current_score)
        display_score(score)
        return score

    def check_answer(self, score):
        user_answer = input("Your answer: ")
        exit_words = ["exit", "quit", "q", "x"]
        if user_answer.lower() in exit_words:
            exit()
        if user_answer.lower() in self.answer:
            score = score + 1
            print("Correct!")
        else:
            print("Incorrect!")
        return score


question_file = open("questions.json", "r")
questions = json.load(question_file)
question_file.close()


# questions_objects = [Question(q["text"], q["answer"], q.get("wrong")) for q in questions]
# questions_objects = [Question(**q) for q in questions]
questions_objects = []
for q in questions:
    # q = Question(text=q["text"], answer=q["answer"], wrong=q["wrong"])
    q = Question(**q)
    questions_objects.append(q)

random.shuffle(questions_objects)

score = 0
for q in questions_objects:
    score = q.ask(score)

print("Game over, thanks for playing!")
