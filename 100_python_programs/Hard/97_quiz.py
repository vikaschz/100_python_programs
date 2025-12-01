"""
Program: Simple Quiz Game
Description: This program asks multiple-choice questions and shows the final score.

"""


quiz = [
    {
        "question": "What is the national animal of India?",
        "options": ["A. Lion", "B. Elephant", "C. Tiger", "D. Peacock"],
        "answer": "C",
    },
    {
        "question": "Who is known as the Father of Computers?",
        "options": [
            "A. Charles Babbage",
            "B. Alan Turing",
            "C. Tim Berners-Lee",
            "D. Bill Gates",
        ],
        "answer": "A",
    },
    {
        "question": "How many continents are there on Earth?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C",
    },
    {
        "question": "What is the hardest natural substance?",
        "options": ["A. Gold", "B. Iron", "C. Diamond", "D. Quartz"],
        "answer": "C",
    },
    {
        "question": "Which blood group is known as the universal donor?",
        "options": ["A. AB+", "B. O+", "C. O-", "D. AB-"],
        "answer": "C",
    },
    {
        "question": "Which language has the most native speakers?",
        "options": ["A. English", "B. Spanish", "C. Mandarin", "D. Hindi"],
        "answer": "C",
    },
    {
        "question": "What is the process of cell division in humans called?",
        "options": ["A. Mitosis", "B. Meiosis", "C. Binary Fission", "D. Budding"],
        "answer": "A",
    },
    {
        "question": "Which country gifted the Statue of Liberty to the USA?",
        "options": ["A. England", "B. France", "C. Germany", "D. Spain"],
        "answer": "B",
    },
    {
        "question": "Which is the tallest mountain in the world?",
        "options": ["A. K2", "B. Mount Everest", "C. Kangchenjunga", "D. Lhotse"],
        "answer": "B",
    },
    {
        "question": "Which festival is known as the Festival of Lights?",
        "options": ["A. Holi", "B. Eid", "C. Christmas", "D. Diwali"],
        "answer": "D",
    },
]

# Initialize score
score = 0

# Ask questions
for i, item in enumerate(quiz, start=1):
    print(f"\nQuestion {i}: {item['question']}")
    for option in item["options"]:
        print(option)
    user_answer = input("Your answer (A/B/C/D) (Enter Q to exit): ").strip().upper()
    if user_answer == item["answer"]:
        print("Correct!")
        score += 1
    elif user_answer == "Q":
        break
    else:
        print(f"Wrong! Correct answer is {item['answer']}")

# Final score
print(f"\nYour final score is: {score} out of {len(quiz)}")
