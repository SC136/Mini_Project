import random
import time
import json
import pyttsx3
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter.scrolledtext import ScrolledText
from lore import books, bosses_attacks

class MagicalBookstoreGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Magical Bookstore Adventure")
        
        self.leaderboard = self.load_leaderboard()
        self.player_health = 100
        self.start_time = None
        self.current_book = None
        
        self.create_widgets()

    def create_widgets(self):
        self.text_area = ScrolledText(self.root, wrap=tk.WORD, height=20, width=80)
        self.text_area.pack(pady=10)
        self.text_area.insert(tk.END, "Welcome to the Magical Bookstore Adventure!\n")
        
        self.action_frame = tk.Frame(self.root)
        self.action_frame.pack()

        self.action_button = tk.Button(self.action_frame, text="Start Adventure", command=self.start_adventure)
        self.action_button.pack(pady=5)

        self.quit_button = tk.Button(self.action_frame, text="Quit", command=self.root.quit)
        self.quit_button.pack(pady=5)

    def speak(self, text):
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()

    def load_leaderboard(self, filename="leaderboard.json"):
        try:
            with open(filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_leaderboard(self, filename="leaderboard.json"):
        with open(filename, "w") as file:
            json.dump(self.leaderboard, file, indent=4)

    def update_leaderboard(self, name, time_taken):
        if name not in self.leaderboard or time_taken < self.leaderboard[name]:
            self.leaderboard[name] = time_taken

    def display_leaderboard(self):
        leaderboard_text = "\n--- Leaderboard ---\n"
        for name, time_taken in sorted(self.leaderboard.items(), key=lambda x: x[1]):
            leaderboard_text += f"{name}: {time_taken:.2f} seconds\n"
        messagebox.showinfo("Leaderboard", leaderboard_text)

    def start_adventure(self):
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, "Lucas loved books, especially those filled with fantastical tales. One rainy afternoon, he stumbled upon a dusty old bookstore with a peculiar sign: \"Enter to Explore.\"\n")
        self.speak("Lucas loved books, especially those filled with fantastical tales. One rainy afternoon, he stumbled upon a dusty old bookstore with a peculiar sign: Enter to Explore.")
        
        self.player_health = 100
        self.start_time = time.time()

        self.next_book()

    def next_book(self):
        if not books:
            self.end_game()
            return

        self.current_book = books.pop(0)
        self.text_area.insert(tk.END, f"\nLucas finds a book titled \"{self.current_book['title']}\" and opens it. Suddenly, he is transported to another world!\n")
        self.speak(f"Lucas finds a book titled {self.current_book['title']} and opens it. Suddenly, he is transported to another world!")

        self.battle()

    def battle(self):
        self.boss_name = self.current_book["boss"]
        self.boss_health = self.current_book["boss_health"]

        self.text_area.insert(tk.END, self.current_book["lore"])
        self.speak(self.current_book["lore"])

        self.text_area.insert(tk.END, f"\nYou are facing {self.boss_name}!\n")
        self.speak(f"You are facing {self.boss_name}!")

        self.update_battle_ui()

    def update_battle_ui(self):
        if self.boss_health <= 0 or self.player_health <= 0:
            self.resolve_battle()
            return

        self.text_area.insert(tk.END, f"\n{self.boss_name}'s Health: {self.boss_health}\nYour Health: {self.player_health}\n")

        self.action_frame.pack_forget()
        self.action_frame = tk.Frame(self.root)
        self.action_frame.pack()

        actions = [
            ("Sword Hit", self.sword_hit),
            ("Strong Punch", self.strong_punch),
            ("Fireball Spell", self.fireball_spell),
            ("Flaming Sword", self.flaming_sword)
        ]

        for text, command in actions:
            btn = tk.Button(self.action_frame, text=text, command=command)
            btn.pack(side=tk.LEFT, padx=5, pady=5)

    def sword_hit(self):
        damage = random.randint(10, 15)
        self.boss_health -= damage
        self.text_area.insert(tk.END, f"\nYou used Sword Hit and dealt {damage} damage!\n")
        self.speak(f"You used Sword Hit and dealt {damage} damage!")
        self.boss_attack()

    def strong_punch(self):
        damage = random.randint(15, 20)
        self.boss_health -= damage
        self.text_area.insert(tk.END, f"\nYou used Strong Punch and dealt {damage} damage!\n")
        self.speak(f"You used Strong Punch and dealt {damage} damage!")
        self.boss_attack()

    def fireball_spell(self):
        if random.choice([True, False]):
            damage = random.randint(20, 35)
            self.boss_health -= damage
            self.text_area.insert(tk.END, f"\nYou used Fireball Spell and dealt {damage} damage!\n")
            self.speak(f"You used Fireball Spell and dealt {damage} damage!")
        else:
            self.text_area.insert(tk.END, "\nYour Fireball Spell failed!\n")
            self.speak("Your Fireball Spell failed!")
        self.boss_attack()

    def flaming_sword(self):
        damage = random.randint(30, 40)
        self.boss_health -= damage
        self.text_area.insert(tk.END, f"\nYou used Flaming Sword and dealt {damage} damage!\n")
        self.speak(f"You used Flaming Sword and dealt {damage} damage!")
        if random.choice([True, False]):
            self.player_health -= damage
            self.text_area.insert(tk.END, f"\nThe Flaming Sword backfired, dealing {damage} damage to you!\n")
        self.boss_attack()

    def boss_attack(self):
        if self.boss_health > 0:
            boss_attack = random.choice(bosses_attacks[self.boss_name])
            damage = random.randint(*boss_attack["damage_range"])
            self.player_health -= damage
            self.text_area.insert(tk.END, f"\n{self.boss_name} used {boss_attack['name']} and dealt {damage} damage!\n")
            self.speak(f"{self.boss_name} used {boss_attack['name']} and dealt {damage} damage!")

        self.update_battle_ui()

    def resolve_battle(self):
        if self.player_health > 0:
            self.text_area.insert(tk.END, f"\nYou defeated {self.boss_name}! The book glows and pulls you back to the bookstore.\n")
            self.speak(f"You defeated {self.boss_name}! The book glows and pulls you back to the bookstore.")
            self.next_book()
        else:
            self.text_area.insert(tk.END, f"\nYou were defeated by {self.boss_name}. The adventure ends here.\n")
            self.speak(f"You were defeated by {self.boss_name}. The adventure ends here.")
            messagebox.showinfo("Game Over", "Better luck next time!")

    def end_game(self):
        end_time = time.time()
        time_taken = end_time - self.start_time

        self.text_area.insert(tk.END, "\nCongratulations! You completed the game.\n")
        self.speak("Congratulations! You completed the game.")

        name = simpledialog.askstring("Leaderboard", "Enter your name:")
        if name:
            self.update_leaderboard(name, time_taken)
            self.save_leaderboard()
            self.display_leaderboard()

if __name__ == "__main__":
    root = tk.Tk()
    game = MagicalBookstoreGame(root)
    root.mainloop()
