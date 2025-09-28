# Flashcards

A simple command-line flashcards app built with Python. It lets you practice questions stored in a JSON file, track your score, and retry the ones you got wrong.

---

## Features
- Loads flashcards from a `cards.json` file  
- Randomly shuffles cards each session  
- Lets you self-mark whether you knew the answer (`y/n`)  
- Tracks your score and shows percentage correct  
- Gives you a second round to review the ones you missed  
- Automatically restarts when finished for continuous practice  

---

## Usage
1. Make sure you have a `cards.json` file in the same directory.  
2. Run the program:  
   ```bash
   python3 flashcards.py
Follow the prompts:

Press Enter to reveal the answer

Type y if you knew it, n if you didn’t

Wrong answers will be saved for a review round

Example cards.json
json
Copy code
[
    {
        "front": "What is the capital of France?",
        "back": "Paris"
    },
    {
        "front": "What does CPU stand for?",
        "back": "Central Processing Unit"
    },
    {
        "front": "Who created Python?",
        "back": "Guido van Rossum"
    }
]
