import random
import time
import json
import pyttsx3

tts = pyttsx3.init()
tts.setProperty('rate', 150)
voices = tts.getProperty('voices')
tts.setProperty('voice', voices[1].id)
def display(text):
    print(text)
    tts.say(text)
    tts.runAndWait()

def say(text):
    tts.say(text)
    tts.runAndWait()

player = {
    "health": 100,
    "inventory": [],
    "location": "forest"
}

locations = {
    "forest": {
        "description": "You are in a dark, enchanted forest. Paths lead north and east.",
        "items": ["map"],
        "enemies": []
    },
    "hut": {
        "description": "You are inside a small wooden hut. It seems abandoned. Path lead to south.",
        "items": ["healing potion"],
        "enemies": []
    },
    "cave": {
        "description": "You enter the Cave of Echoes. Shadows dance on the walls.",
        "items": ["amulet of eternity"],
        "enemies": ["goblin"]
    }
}
    
leaderboard_file = "leaderboard.json"

def load_leaderboard():
    try:
        with open(leaderboard_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_leaderboard(leaderboard):
    with open(leaderboard_file, "w") as file:
        json.dump(leaderboard, file, indent=4)

def display_leaderboard():
    leaderboard = load_leaderboard()
    sorted_leaderboard = sorted(leaderboard, key=lambda x: x["time"])[:5]
    print("\n=== Leaderboard ===")
    for idx, entry in enumerate(sorted_leaderboard, start=1):
        print(f"{idx}. {entry['username']} - {entry['time']} seconds")
    if not sorted_leaderboard:
        print("No entries yet!")
    print("===================")

def look_around():
    location = player["location"]
    loc_data = locations[location]
    display(loc_data["description"])
    if loc_data["items"]:
        display(f"You see the following items: {', '.join(loc_data['items'])}")
    if loc_data["enemies"]:
        display(f"Beware! Enemies nearby: {', '.join(loc_data['enemies'])}")

def move(direction):
    location = player["location"]
    if location == "forest" and direction == "north":
        player["location"] = "hut"
    elif location == "forest" and direction == "east":
        player["location"] = "cave"
    elif location == "hut" and direction == "south":
        player["location"] = "forest"
    else:
        display("You can't go that way!")
        return
    display(f"You move {direction} to the {player['location']}.")
    look_around()

def take_item(item):
    location = player["location"]
    loc_data = locations[location]

    if item in loc_data["items"]:
        if item == "amulet of eternity":
            if loc_data["enemies"]:
                display("You can't take the amulet while the goblin is still alive!")
                display("The goblin attacks you!")
                player["health"] -= 20
                display(f"You lose 20 health. Current health: {player['health']}")
                if player["health"] <= 0:
                    display("You have been killed by the goblin. Game over.")
                    exit()
                return
        player["inventory"].append(item)
        loc_data["items"].remove(item)
        display(f"You picked up {item}.")
    else:
        display(f"There is no {item} here.")

def attack():
    location = player["location"]
    loc_data = locations[location]
    if loc_data["enemies"]:
        enemy = loc_data["enemies"].pop(0)
        display(f"You attack the {enemy}!")
        if random.random() > 0.5:
            display(f"You defeated the {enemy}!")
        else:
            player["health"] -= 20
            display(f"The {enemy} injured you! Health: {player['health']}")
            if player["health"] <= 0:
                display("You have died. Game over.")
                exit()
    else:
        display("There's nothing to attack here.")

def check_inventory():
    if player["inventory"]:
        display(f"You have: {', '.join(player['inventory'])}")
    else:
        display("Your inventory is empty.")

def use_item(item):
    if item in player["inventory"]:
        if item == "healing potion":
            player["health"] += 20
            player["inventory"].remove(item)
            display("You used a healing potion. Your health increased by 20!")
            display(f"Current health: {player['health']}")
        else:
            display(f"You used {item}, but nothing happened.")
    else:
        display(f"You don't have {item} in your inventory.")

def update_leaderboard(username, time_taken):
    leaderboard = load_leaderboard()
    existing_entry = next((entry for entry in leaderboard if entry["username"] == username), None)
    if existing_entry:
        if time_taken < existing_entry["time"]:
            leaderboard.remove(existing_entry)
            leaderboard.append({"username": username, "time": time_taken})
            display("Congratulations! You beat your previous time!")
    else:
        leaderboard.append({"username": username, "time": time_taken})
        display("Your score has been added to the leaderboard!")
    save_leaderboard(leaderboard)

def main():
    display("Welcome to 'The Amulet of Eternity'!")
    display("Type 'help' for a list of commands.")
    look_around()

    start_time = time.time()
    while True:
        say("What do you want to do?")
        command = input("\nWhat do you want to do? ").strip().lower()

        if command == "help":
            print("Commands: look, move [direction], take [item], use [item], attack, inventory, quit")
        elif command == "look":
            look_around()
        elif command.startswith("move"):
            parts = command.split(maxsplit=1)
            if len(parts) > 1:
                direction = parts[1]
                move(direction)
            else:
                display("Please specify a direction (e.g., 'move north').")
        elif command.startswith("take"):
            parts = command.split(maxsplit=1)
            if len(parts) > 1:
                item = parts[1]
                take_item(item)
            else:
                display("Please specify an item to take (e.g., 'take potion').")
        elif command.startswith("use"):
            parts = command.split(maxsplit=1)
            if len(parts) > 1:
                item = parts[1]
                use_item(item)
            else:
                display("Please specify an item to use (e.g., 'use potion').")
        elif command == "attack":
            attack()
        elif command == "inventory":
            check_inventory()
        elif command == "quit":
            display("Thanks for playing! Goodbye.")
            break
        else:
            display("I don't understand that command.")

        if "amulet of eternity" in player["inventory"]:
            display("\nCongratulations! You have retrieved the Amulet of Eternity and completed the quest!")
            end_time = time.time()
            time_taken = int(end_time - start_time)
            display(f"You completed the game in {time_taken} seconds!")
            username = input("Enter your name for the leaderboard: ").strip()

            # Update leaderboard
            update_leaderboard(username, time_taken)
            display_leaderboard()
            break

if __name__ == "__main__":
    main()
