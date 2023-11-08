import random


def display_score(score):
    print(f"Your score is now: {score}") # print("Your score is now:", score)
    if score == 0:
        print("This is not great!")


class Question:
    def __init__(self, text, answer, wrong):
        self.text = text
        self.answer = answer
        self.wrong = wrong

    def ask(self, current_score):
        print(self.text)
        letters = "ABCDEFG"  # This is a string, so we can iterate over it to get A, B, C, etc.
        options = self.wrong + [self.answer[0]]  # Add the correct answer to the list of wrong answers
        random.shuffle(options)  # Shuffle the options so the correct answer isn't always the last one
        for item in zip(letters, options):  # zip() lets us iterate over two lists at the same time, an `item` will be a tuple of (letter, answer)
            letter = item[0]  # This is the letter, like "A"
            option = item[1]  # This is one of the possible options, like "Paris"
            if (option.lower() in self.answer):  # If this is the correct answer...
                self.answer.append(letter.lower())  # ...add the letter to the list of possible answers
            option = "{}. {}".format(letter, option.capitalize())  # This will format the option to be "A. Option"
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


question1 = Question(
    text="What is the capital city of Germany?",
    answer=["berlin"],
    wrong=["Munich", "Hamburg"]
)

score = 0
score = question1.ask(score)
print("Game over, thanks for playing!")
