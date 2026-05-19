questions = {
    "math": [
        {"q": "What is 15 + 27?", "a": "42", "options": ["35", "42", "48", "52"]},
        {"q": "What is 8 × 6?", "a": "48", "options": ["42", "48", "54", "64"]},
        {"q": "What is 64 ÷ 8?", "a": "8", "options": ["6", "7", "8", "9"]},
    ],
    "ai": [
        {"q": "What does AI stand for?", "a": "Artificial Intelligence", "options": ["Automatic Input", "Artificial Intelligence", "Advanced Internet", "Auto Instruction"]},
        {"q": "Which one is an example of AI?", "a": "Voice Assistant", "options": ["Calculator", "Voice Assistant", "Traffic Light", "Bicycle"]},
    ],
    "grammar": [
        {"q": "Which is spelled correctly?", "a": "Beautiful", "options": ["Beautifull", "Beautiful", "Beautifal", "Butiful"]},
        {"q": "Choose the noun:", "a": "Happiness", "options": ["Run", "Happiness", "Quickly", "Blue"]},
    ],
    "software": [
        {"q": "What is Python?", "a": "A Programming Language", "options": ["A Snake", "A Programming Language", "A Game", "A Robot"]},
        {"q": "What is a 'bug' in coding?", "a": "An error in the code", "options": ["An insect", "An error in the code", "A new feature", "A button"]},
    ]
}

def get_topics():
    return list(questions.keys())

def get_questions(topic):
    return questions.get(topic, [])