import tkinter as tk
from tkinter import scrolledtext
import random
import time
from lore import books, bosses_attacks

class ChatbotAdventure:
    def __init__(self, root):
        self.root = root
        self.root.title("Magical Bookstore Adventure")
        self.root.geometry("600x500")

        self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='normal')
        self.chat_display.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        self.chat_display.config(state='disabled')

        self.input_box = tk.Entry(root, width=50)
        self.input_box.pack(pady=5, padx=10, fill=tk.X)
        self.input_box.bind("<Return>", self.handle_input)

        self.send_button = tk.Button(root, text="Send", command=self.handle_input)
        self.send_button.pack(pady=5)

        self.books = books
        self.current_book_index = 0
        self.player_health = 100
        self.boss_health = 0
        self.boss_name = ""
        self.lore = ""
        self.awaiting_input = False
        self.intro()

    def intro(self):
        self.display_message("Welcome to the Magical Bookstore Adventure!\n")
        time.sleep(1)
        self.display_message("Lucas loved books, especially those filled with fantastical tales. One rainy afternoon, he stumbled upon a dusty old bookstore with a peculiar sign: 'Enter to Explore.'\n")
        time.sleep(2)
        self.start_next_book()

    def start_next_book(self):
        if self.current_book_index >= len(self.books):
            self.display_message("After defeating all the bosses, Lucas finds the Librarian, who smiles and lets him return home. He promises to keep her secret and return one day.\n")
            return

        book = self.books[self.current_book_index]
        self.current_book_index += 1

        self.display_message(f"Lucas finds a book titled \"{book['title']}\" and opens it. Suddenly, he is transported to another world!\n")
        time.sleep(2)

        self.boss_name = book["boss"]
        self.boss_health = book["boss_health"]
        self.lore = book["lore"]

        self.display_message(f"{self.lore}\n")
        time.sleep(2)
        self.display_message(f"You are facing {self.boss_name}.\n")

        self.battle_prompt()

    def battle_prompt(self):
        self.display_message("\nYour Options:\n")
        self.display_message("1. Sword Hit (Deals 10-15 damage, guaranteed to hit)\n")
        self.display_message("2. Strong Punch (Deals 15-20 damage, guaranteed to hit)\n")
        self.display_message("3. Fireball Spell (Deals 20-35 damage, 50% chance to fail)\n")
        self.display_message("4. Flaming Sword (Deals 30-40 damage, 50% chance to damage you for the same amount)\n")
        self.awaiting_input = True

    def handle_input(self, event=None):
        user_input = self.input_box.get()
        self.input_box.delete(0, tk.END)
        if not self.awaiting_input:
            return

        self.awaiting_input = False
        self.display_message(f"You: {user_input}\n")

        if user_input == "1":
            damage = random.randint(10, 15)
            self.boss_health -= damage
            self.display_message(f"You used Sword Hit and dealt {damage} damage!\n")
        elif user_input == "2":
            damage = random.randint(15, 20)
            self.boss_health -= damage
            self.display_message(f"You used Strong Punch and dealt {damage} damage!\n")
        elif user_input == "3":
            if random.choice([True, False]):
                damage = random.randint(20, 35)
                self.boss_health -= damage
                self.display_message(f"You used Fireball Spell and dealt {damage} damage!\n")
            else:
                self.display_message("Your Fireball Spell failed!\n")
        elif user_input == "4":
            damage = random.randint(30, 40)
            self.boss_health -= damage
            self.display_message(f"You used Flaming Sword and dealt {damage} damage!\n")
            if random.choice([True, False]):
                self.player_health -= damage
                self.display_message(f"The Flaming Sword backfired, dealing {damage} damage to you!\n")
        else:
            self.display_message("Invalid choice! You lose your turn.\n")

        if self.boss_health > 0:
            boss_attack = random.choice(bosses_attacks[self.boss_name])
            damage = random.randint(*boss_attack["damage_range"])
            self.display_message(f"{self.boss_name} used {boss_attack['name']} and dealt {damage} damage!\n")
            self.player_health -= damage

        self.display_message(f"\n{self.boss_name}'s Health: {self.boss_health}\n")
        self.display_message(f"Your Health: {self.player_health}\n")

        if self.player_health <= 0:
            self.display_message(f"\nYou were defeated by {self.boss_name}. The adventure ends here.\n")
        elif self.boss_health <= 0:
            self.display_message(f"\nYou defeated {self.boss_name}! The book glows and pulls you back to the bookstore.\n")
            self.start_next_book()
        else:
            self.battle_prompt()

    def display_message(self, message):
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, message + "\n")
        self.chat_display.config(state='disabled')
        self.chat_display.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotAdventure(root)
    root.mainloop()
