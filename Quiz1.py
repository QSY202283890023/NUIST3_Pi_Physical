# NUIST Quiz Game in Python
def quiz():
    print("Welcome to the Animal Quiz!")
    print("Answer the following questions:")

    # Questions and Answers
    questions = [
        "1. What is the largest animal on Earth?\n   a. Blue Whale\n   b. Mouse\n   c. Cat\n   Your answer: ",
        "2. Which bird can fly backwards?\n   a. Cuckoo\n   b. Eagle\n   c. Hummingbird\n   Your answer: ",
        "3. What is the only mammal capable of flight?\n   a. Bat\n   b. Squirrel\n   c. Dolphin\n   Your answer: "
    ]
    
    answers = ["a", "c", "a"]  # Correct answers
    score = 0

    # Ask questions
    for i in range(len(questions)):
        user_answer = input(questions[i]).strip().lower()
        if user_answer == answers[i]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

    # Provide final score
    print("\nQuiz completed!")
    print(f"You got {score}/{len(questions)} questions correct.")

# Run the quiz function
quiz()
