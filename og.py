import random

# Define Codedium's possible attacks
codedium_attacks = [
    {"name": "Incendio", "damage": 10},
    {"name": "Confringo", "damage": 15},
    {"name": "Crucio", "damage": 5},
    {"name": "Bombarda", "damage": 20},
]

codedium_final_moves = [
    {"name": "Lacarnum Inflamarae", "damage": 20},
    {"name": "Bombarda", "damage": 25},
    {"name": "Confringo", "damage": 15},
]

print('================================================================')
print('Hello wizard or witch, today your opponent is Pythaseus Codedium')
print('================================================================')
hpPlayer = 100
hpPC = 100
print("Pythaseus Codedium was a master wizard, known for his unparalleled skill in coding spells and enchantments. \nHe could weave magical code into intricate runes, casting powerful hexes and charms with a few keystrokes. \nLegend says that he once programmed a spell that could control time itself, but it came with a dangerous price. \nNow, his name lives on in the annals of wizardry, a reminder of the intersection between magic and the digital realm.")
print(f"\nYour current health points is: {hpPlayer}")
print(f"\nCodedium's health points is: {hpPC}")

print('Select one of the following moves to attack him:')
playerMove = int(input('1)Sectumsempra \n2)Confringo \n3)Crucio \n'))

if playerMove == 1:
  hpPC -= 10
  print(f"Nice Sectumsempra, \nCodedium's health points is now {hpPC}")
elif playerMove == 2:
  hpPC -= 15
  print(f"Nice Confringo, \nCodedium's health points is now {hpPC}")
elif playerMove == 3:
  hpPC -= 5
  print(f"Nice Crucio, \nCodedium's health points is now {hpPC}")

codedium_move = random.choice(codedium_attacks)
print(f'\nCodedium used {codedium_move["name"]}!')
hpPlayer -= codedium_move["damage"]
print(f"It dealt {codedium_move['damage']} damage. Your health points are now {hpPlayer}")

print('\nTime to give him proper attack, quickly choose on of the following attacks:')
playerMove = int(input('1)Stupefy \n2)Incendio \n3)Crucio \n'))

if playerMove == 1:
  hpPC -= 30
  print(f"Nice Stupefy, \nCodedium's health points is now {hpPC}")
elif playerMove == 2:
  hpPC -= 45
  print(f"Nice Incendio, \nCodedium's health points is now {hpPC}")
elif playerMove == 3:
  hpPC -= 15
  print(f"Nice Crucio, \nCodedium's health points is now {hpPC}")

print('\nHe looks weak, time to finish him with a finishing spell:')
playerMove = int(input('1)Avada Kedavra \n2)Lacarnum Inflamarae \n3)Expelliarmus \n'))

if playerMove == 1:
  hpPC = 0
  print(f"Well done, the attack worked, \nCodedium's health points is now {hpPC}")
elif playerMove == 2:
  hpPC = 0
  print(f"Nice attack, he fell on his knees, \nCodedium's health points is now {hpPC}")
elif playerMove == 3:
  hpPC = 10
  print(f"He sure looks weak, but isnt defeated yet. \nCodedium's health points is now {hpPC}")

if hpPC == 10:
  codedium_move = random.choice(codedium_final_moves)  # Choose a random final move
  print(f'\nCodedium gathers all his strength and casts {codedium_move["name"]}!')

  print('\nDefend yourself! Choose one of the following moves:')
  playerMove = int(input('1) Protego \n2) Scutum Charm \n3) Aegis Glacia \n'))

  if playerMove == 1:  # Protego
    hpPlayer -= codedium_move["damage"] // 2  # Reduces damage by half
    print(f"You defended with Protego! The attack dealt {codedium_move['damage'] // 2} damage.")
    print(f"\nYour health points are now {hpPlayer}.")
  elif playerMove == 2:  # Scutum Charm
    hpPlayer -= codedium_move["damage"] * 2 // 3  # Reduces damage by 1/3
    print(f"You defended with Scutum Charm! The attack dealt {codedium_move['damage'] * 2 // 3} damage.")
    print(f"\nYour health points are now {hpPlayer}.")
  elif playerMove == 3:  # Aegis Glacia
    hpPlayer -= codedium_move["damage"] // 3  # Strongest defense, reduces damage by 2/3
    print(f"You defended with Aegis Glacia! The attack dealt {codedium_move['damage'] // 3} damage.")
    print(f"\nYour health points are now {hpPlayer}.")
  else:
    hpPlayer -= codedium_move["damage"]  # No defense, full damage
    print(f"You failed to defend! The attack dealt {codedium_move['damage']} damage.")
    print(f"\nYour health points are now {hpPlayer}.")

  print('\nNow that you have defended yourself, time to end this fight. \nChoose your final move:')
  playerMove = int(input('1) Lacarnum Inflamarae \n2) Bombarda \n3) Avada Kedavra\n'))

  if playerMove == 1:
    hpPC = 0
    print(f"Well done, the attack worked, \nCodedium's health points is now {hpPC}")
  elif playerMove == 2:
    hpPC = 0
    print(f"Nice attack, he fell on his knees, \nCodedium's health points is now {hpPC}")
  elif playerMove == 3:
    hpPC = 0
    print(f"Good, you burned him down to ashes. \nCodedium's health points is now {hpPC}") 


print('\nThe room was silent, save for the soft hum of the dissipating magical code that once powered Codediums mighty spells. \nThe air shimmered, heavy with the residue of their epic duel, as the hero stood amidst the debris, victorious but weary. \nPythaseus Codedium lay defeated, his wand shattered, his once-unstoppable power reduced to mere sparks fading into nothingness. \nThe hero gazed into the distance, knowing that this victory was not just their own—it was for the freedom of wizards everywhere, a new chapter in the annals of magical history.')

print ('\nGAME OVER')
print('================================================================')
