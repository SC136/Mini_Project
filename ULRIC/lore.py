books = [
    {
        "title": "The Dragon's Lair",
        "boss": "Ignathar, the Infernal Flame",
        "boss_health": 50,
        "lore": "Ignathar, the Fire Dragon, was once the noble guardian of the Flame Crystal. Consumed by greed, he tried to claim its power, transforming into a monstrous tyrant. Now, he rules the scorched lands, his fiery breath melting steel, and his scales impervious to mortal weapons. Deep within Mount Ember, Ignathar hoards treasures and enslaves creatures, guarding the crystal with cunning and fury. To defeat him, you must face him in his volcanic lair and shatter his reign of fire."
    },
    {
        "title": "The Pirate's Curse",
        "boss": "Dread Captain Blacktide",
        "boss_health": 80,
        "lore": "Once a loyal navy officer, Captain Blacktide turned rogue after uncovering the cursed Trident of Tempests, a relic granting control over the seas. The trident’s dark magic twisted him into a merciless pirate, his ship, The Abyssal Wraith, sailing through storms he conjures at will.\n\nBlacktide plunders relentlessly, leaving wreckage and despair in his wake. His crew, bound by fear and the trident’s curse, haunt the seas like ghosts. To end his reign, you must face him on the storm-lashed deck of The Abyssal Wraith and wrest the trident from his cursed grasp."
    },
    {
        "title": "The Wizard's Tower",
        "boss": "Malakar, the Evil Wizard",
        "boss_health": 100,
        "lore": "Malakar was once a wise and kind wizard who helped the people. But one day, he found a book of dark spells that changed him. The magic in the book made him evil and hungry for power.\n\nNow, Malakar hides in an old, crumbling tower, guarded by monsters and traps. He uses his dark magic to bring fear and suffering to the land. To stop him, you must enter his tower, face his spells, and destroy the book that made him so dangerous."
    }
]

bosses_attacks = {
    "Ignathar, the Infernal Flame": [
        {"name": "Fiery Breath", "damage_range": (20, 30)},
        {"name": "Lava Tail Swipe", "damage_range": (15, 25)},
        {"name": "Molten Claw", "damage_range": (15, 20)}
    ],
    "Dread Captain Blacktide": [
        {"name": "Storm Slash", "damage_range": (20, 30)},
        {"name": "Wave Crash", "damage_range": (15, 25)},
        {"name": "Tempest Strike", "damage_range": (18, 28)}
    ],
    "Malakar, the Evil Wizard": [
        {"name": "Dark Bolt", "damage_range": (25, 35)},
        {"name": "Cursed Grip", "damage_range": (30, 40)},
        {"name": "Shadow Surge", "damage_range": (20, 30)}
    ]
}
