questions = [
    {
        "question": "what is the capital of Nigeria",
        "options": ["A. Lagos", "B. Abuja", "C. Kano", "D. Enugu"],
         "answer": "B"
    },
    {
        "question": "Which language are we learning?",
        "options": ["A. Java", "B. C++", "C. Python", "D. Ruby"],
        "answer": "C"
    },
    {
         "question": "Which of these is used to write Python code?",
        "options": ["A. VS Code", "B. Microsoft Word", "C. Calculator", "D. Paint"],
        "answer": "A"
    }
]

def play_quiz():
    print("Welcome to the Quiz Game!")
    print("Answer the following questions.\n")
    score = 0

    for item in questions:
        print("\n" + item["question"])

        for option in item["options"]:
            print(option)

        answer = input("Choose A, B, C or D: ").upper()

        if answer == item["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong answer!")

    print(f"\nYour final score is {score}/{len(questions)}")


play_quiz()