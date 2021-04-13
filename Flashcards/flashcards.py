import json

with open('comptia.json', 'r') as f:
    data = json.load(f)

total = len(data["cards"])
score = 0

for i in data["cards"]:
    guess = input(i["Q"] + " > ")

    if guess == i["A"]:
        score += 1
        print(f"Correct!. Current score: {score}/{total}")
    else:
        print("Sorry, the answer was",i["A"])
        print(f"current score: {score}/{total}")
