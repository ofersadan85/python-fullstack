# A trivia game
# Users will be asked one question and will have to input an answer
# We will check if the answer is correct and print a message and a score
# The second question will be a multiple choice question.
# Once again we will check the answer and print a message and a score
# This very simple game has some problems, your task is to improve it

print("Welcome to the trivia game!")
print("Your score: 0")
print()
print("Question 1: What is the capital of France?")
answer_one = input("Your answer: ")
if answer_one == "Paris":
    print("Correct!")
    print("Your score: 1")
else:
    print("Incorrect!")
    print("Your score: 0")
    
print()
print("Question 2: What is the capital of Germany?")
print("A. Berlin")
print("B. Munich")
print("C. Hamburg")
print("D. Frankfurt")
answer_two = input("Your answer: ")
if answer_two == "A":
    print("Correct!")
    print("Your score: 2")
else:
    print("Incorrect!")
    print("Your score: 1")
