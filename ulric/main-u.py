import random
import time
from lore import books, bosses_attacks

def battle(boss_name, boss_health, player_health, lore):
    print(f"\n{lore}\n")
    time.sleep(10)
    print(f"You are facing {boss_name}")

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
        elif choice == "2":
            damage = random.randint(15, 20)
            boss_health -= damage
            print(f"You used Strong Punch and dealt {damage} damage!")
        elif choice == "3":
            if random.choice([True, False]):
                damage = random.randint(20, 35)
                boss_health -= damage
                print(f"You used Fireball Spell and dealt {damage} damage!")
            else:
                print("Your Fireball Spell failed!")
            time.sleep(2)
        elif choice == "4":
            damage = random.randint(30, 40)
            boss_health -= damage
            print(f"You used Flaming Sword and dealt {damage} damage!")
            if random.choice([True, False]):
                player_health -= damage
                print(f"The Flaming Sword backfired, dealing {damage} damage to you!")
            time.sleep(2)
        else:
            print("Invalid choice! You lose your turn.")

        if boss_health > 0:
            boss_attack = random.choice(bosses_attacks[boss_name])
            damage = random.randint(*boss_attack["damage_range"])
            print(f"{boss_name} used {boss_attack['name']} and dealt {damage} damage!")
            player_health -= damage
            time.sleep(2)

        print(f"\n{boss_name}'s Health: {boss_health}")
        print(f"Your Health: {player_health}")
        time.sleep(2)

    if player_health > 0:
        print(f"\nYou defeated {boss_name}! The book glows and pulls you back to the bookstore.")
        return True
    else:
        print(f"\nYou were defeated by {boss_name}. The adventure ends here.")
        return False

def main():
    print("Welcome to the Magical Bookstore Adventure!")
    time.sleep(2)
    print("Lucas loved books, especially those filled with fantastical tales. One rainy afternoon, he stumbled upon a dusty old bookstore with a peculiar sign: \"Enter to Explore.\"")
    time.sleep(3)

    player_health = 100

    for book in books:
        print(f"\nLucas finds a book titled \"{book['title']}\" and opens it. Suddenly, he is transported to another world!")
        time.sleep(3)
        success = battle(book["boss"], book["boss_health"], player_health, book["lore"])
        if not success:
            print("\nLucas failed in his quest. Better luck next time!")
            return

    print("\nAfter defeating all the bosses, Lucas finds the Librarian, who smiles and lets him return home. He promises to keep her secret and return one day.")

if __name__ == "__main__":
    main()
