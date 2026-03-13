import random

attacks = [

    {
        "name": "Slag",
        "damage": 5,
    },
    {
        "name":"Spark",
        "damage": 10,
    },
    {
        "name": "Eldklot",
        "damage": 20
    }
]

hp_spelare = 100
hp_monster = 100

print("--- FIGHT START ---")

while hp_spelare > 0 and hp_monster > 0:
    
    attack = random.choice(attacks)
    hp_monster -= attack["damage"]
    print(f"du använder {attack['name']}! Monstret tar {attack['damage']} skada.")


    if hp_monster > 0:
        hp_spelare -= 15
        print(f"Monstret biter dig! Du tar 15 skada.")

    if random.random() < 0.2:
        hp_monster -= 30 
        hp_spelare += 30
        print("du fick en super attack, monstret tar 30hp skada o du får 30hp")
    
    if random.random() < 0.2:
        hp_spelare -= 20
        hp_monster += 15
        print("monstret kastade ett eldklott på dig")
    
    print(f"Din HP: {hp_spelare} | Monster HP: {hp_monster}\n")

if hp_spelare > 0:
    print("Du vann!")
else:
    print("Du dog...")