questions = [
    {
        "question": "What is always coming but never arrives? ",
        "answer":"tomorrow"
    },
    {
        "question": "What is it that lives if it is fed, and dies if you give it a drink? ",
        "answer":"fire"
    },
    {
        "question": "Uncle Bill’s farm had a terrible storm and all but seven sheep were killed. How many sheep are still alive? ",
        "answer":"seven"
    },
    {
        "question": "What goes up and down, but always remains in the same place? ",
        "answer":"stairs"
    },
    {
        "question":"Everyone in the world needs it, but they usually give it without taking it. What is it? ",
        "answer":"advice"
    },
]

count = 0
def new_game():
    global count
    for question in questions:
        my_input = input(question.get("question"))
        check_input = check_answer( my_input = my_input, answer = question.get("answer"))
        if(check_input):
            count+=1

def check_answer(my_input, answer):
    correct = False
    if(my_input.lower() == answer):
        correct = True
    return correct

def display_score():
    global count
    print(f"Your Final Score is {count}")


while True:
    new_game()
    display_score()

    play = input("Do you want to play again? yes/no :")
    if(play != "yes"):
        print("Bye")
        break
    count = 0