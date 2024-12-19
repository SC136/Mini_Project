import random
import time
import json
import pyttsx3
from lore import books, bosses_attacks

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) 
    engine.say(text)
    engine.runAndWait()

def load_leaderboard(filename="leaderboard.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_leaderboard(leaderboard, filename="leaderboard.json"):
    with open(filename, "w") as file:
        json.dump(leaderboard, file, indent=4)

def update_leaderboard(leaderboard, name, time_taken):
    if name not in leaderboard or time_taken < leaderboard[name]:
        leaderboard[name] = time_taken

def display_leaderboard(leaderboard):
    print("\n--- Leaderboard ---")
    speak("Here is the leaderboard.")
    for name, time_taken in sorted(leaderboard.items(), key=lambda x: x[1]):
        print(f"{name}: {time_taken:.2f} seconds")

def battle(boss_name, boss_health, player_health, lore):
    print(f"\n{lore}\n")
    speak(lore)

    print(f"You are facing {boss_name}")
    speak(f"You are facing {boss_name}")

    while boss_health > 0 and player_health > 0:
        print("\nYour Options:")
        print("1. Sword Hit (Deals 10-15 damage, guaranteed to hit)")
        print("2. Strong Punch (Deals 15-20 damage, guaranteed to hit)")
        print("3. Fireball Spell (Deals 20-35 damage, 50% chance to fail)")
        print("4. Flaming Sword (Deals 30-40 damage, 50% chance to damage you for the same amount)")

        choice = input("Choose your action (1/2/3/4): ")

        if choice == "1":
            damage = random.randint(10, 15)
            boss_health -= damage
            print(f"You used Sword Hit and dealt {damage} damage!")
            speak(f"You used Sword Hit and dealt {damage} damage!")
        elif choice == "2":
            damage = random.randint(15, 20)
            boss_health -= damage
            print(f"You used Strong Punch and dealt {damage} damage!")
            speak(f"You used Strong Punch and dealt {damage} damage!")
        elif choice == "3":
            if random.choice([True, False]):
                damage = random.randint(20, 35)
                boss_health -= damage
                print(f"You used Fireball Spell and dealt {damage} damage!")
                speak(f"You used Fireball Spell and dealt {damage} damage!")
            else:
                print("Your Fireball Spell failed!")
                speak("Your Fireball Spell failed!")
        elif choice == "4":
            damage = random.randint(30, 40)
            boss_health -= damage
            print(f"You used Flaming Sword and dealt {damage} damage!")
            speak(f"You used Flaming Sword and dealt {damage} damage!")
            if random.choice([True, False]):
                player_health -= damage
                print(f"The Flaming Sword backfired, dealing {damage} damage to you!")
        else:
            print("Invalid choice! You lose your turn.")
            speak("Invalid choice! You lose your turn.")

        if boss_health > 0:
            boss_attack = random.choice(bosses_attacks[boss_name])
            damage = random.randint(*boss_attack["damage_range"])
            print(f"{boss_name} used {boss_attack['name']} and dealt {damage} damage!")
            speak(f"{boss_name} used {boss_attack['name']} and dealt {damage} damage!")
            player_health -= damage

        print(f"\n{boss_name}'s Health: {boss_health}")
        print(f"Your Health: {player_health}")
        speak(f"{boss_name}'s Health is now {boss_health}. Your Health is now {player_health}.")

    if player_health > 0:
        print(f"\nYou defeated {boss_name}! The book glows and pulls you back to the bookstore.")
        speak(f"You defeated {boss_name}! The book glows and pulls you back to the bookstore.")
        return True
    else:
        print(f"\nYou were defeated by {boss_name}. The adventure ends here.")
        speak(f"You were defeated by {boss_name}. The adventure ends here.")
        return False

def main():
    leaderboard = load_leaderboard()

    print("Welcome to the Magical Bookstore Adventure!")
    speak("Welcome to the Magical Bookstore Adventure!")

    print("Lucas loved books, especially those filled with fantastical tales. One rainy afternoon, he stumbled upon a dusty old bookstore with a peculiar sign: \"Enter to Explore.\"")
    speak("Lucas loved books, especially those filled with fantastical tales. One rainy afternoon, he stumbled upon a dusty old bookstore with a peculiar sign: Enter to Explore.")

    player_health = 100
    start_time = time.time()

    for book in books:
        print(f"\nLucas finds a book titled \"{book['title']}\" and opens it. Suddenly, he is transported to another world!")
        speak(f"Lucas finds a book titled {book['title']} and opens it. Suddenly, he is transported to another world!")
        success = battle(book["boss"], book["boss_health"], player_health, book["lore"])
        if not success:
            print("\nLucas failed in his quest. Better luck next time!")
            speak("Lucas failed in his quest. Better luck next time!")
            return

    end_time = time.time()
    time_taken = end_time - start_time

    print("\nCongratulations! You completed the game. Please enter your name for the leaderboard.")
    speak("Congratulations! You completed the game. Please enter your name for the leaderboard.")
    name = input("Enter your name: ")

    update_leaderboard(leaderboard, name, time_taken)
    save_leaderboard(leaderboard)

    display_leaderboard(leaderboard)

if __name__ == "__main__":
    main()
