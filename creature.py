import json
import os

creature = {
	"name": "Tama",
	"hunger": 7,
	"happiness": 3,
	"energy": 5
}

def status():
	print(creature["name"] + " is alive!")
	print("Hunger: " + str(creature["hunger"]))
	print("Happiness: " + str(creature["happiness"]))
	print("Energy: " + str(creature["energy"]))

def feed():
	if creature["hunger"] > 0:
		creature["hunger"] -= 1
		print("You've fed Tama!")
	else:
		print("Tama is full!")

def play():
	if creature["happiness"] <10:
		creature["happiness"] += 1
		print("You've played with Tama!")
	else:
		print("Tama is happy!")

def sleep():
	if creature["energy"] < 10:
		creature["energy"] += 1
		print("Tama is sleeping...")
	else:
		print("Tama isn't tired!")

def save():
	with open("tama.json", "w") as f:
		json.dump(creature, f)

def load():
	with open("tama.json", "r") as f:
		return json.load(f)

if os.path.exists("tama.json"):
	creature = load()

feed()
play()
sleep()
save()
status()
