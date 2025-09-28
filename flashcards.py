import json
import random as r

def fetchCards():
    with open("cards.json", "r") as f:
        return json.load(f)

while True:
    data = fetchCards()
    practice = []
    score = 0
    r.shuffle(data)
    for i in range (len(data)):
        print(data[i]["front"])
        print()
        input("Click 'enter' to see answer ")
        print()
        print(data[i]["back"])
        print()
        if input("Did you know this? (y/n): ") == "n":
            practice.append(data[i])
        else:
            score += 1
        print()
    print()
    print(f'You got {score/len(data)*100}%; {score}/{len(data)}')
    print()
    print("Practice What You Got Wrong:")
    print()
    r.shuffle(practice)
    for i in range (len(practice)):
        current = r.randrange(len(practice))
        print()
        print(practice[i]["front"])
        print()
        input("Click 'enter' to see answer ")
        print()
        print(practice[i]["back"])
        print()
        input("Click 'enter' to continue 6")
        print()
    
    print("Restarting")
    print()