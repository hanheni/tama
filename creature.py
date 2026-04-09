import json
import os
import time

creature = {
        "name": "Tama",
        "hunger": 7,
        "happiness": 3,
        "energy": 5,
        "last_seen": time.time()
}

def load():
        with open("tama.json", "r") as f:
                return json.load(f)        
if os.path.exists("tama.json"):
        creature = load()

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

def decay():
        hours_passed = (time.time() - creature["last_seen"]) / 3600 
        if hours_passed >= 1:
                creature["hunger"] += 1
                creature["happiness"] -= 1
                creature["energy"] -= 1
        creature["last_seen"] = time.time()

def save():
        with open("tama.json", "w") as f:
                json.dump(creature, f)

#TODO: replace hardcoded menu with dynamic COMMANDS list using " | ".join(COMMANDS) e.g COMMANDS = ["feed", "play", "sleep", "status", "quit"] and then to print print(" | ".join(COMMANDS))

def action():
        
        while True:
                print("\nWhat would you like to do?")
                print("feed | play | sleep | status | quit")
                action = input("What do you want to do? ")
                if action == "feed":
                        feed()
                elif action == "sleep":
                        sleep()
                elif action == "play":
                        play()
                elif action == "quit":
                        break
                else:
                        print("Отличный...")
decay()
status()
action()
save()
status()

