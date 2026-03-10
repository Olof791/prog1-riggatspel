import random

attacker = ["Slag", "Spark", "Eldklot"]
skador = [5, 10, 20] 

hp_spelare = 100
hp_monster = 100

print("--- FIGHT START ---")

while hp_spelare > 0 and hp_monster > 0:
    val = random.choice([0, 1, 2])
    
    skada = skador[val]
    hp_monster -= skada
    print(f"Du använder {attacker[val]}! Monstern tar {skada} skada.")

    if hp_monster > 0:
        hp_spelare -= 15
        print(f"Monstret biter dig! Du tar 15 skada.")

    if random.random() < 0.2:
        hp_monster -= 30 
        hp_spelare += 30
        print("du fick en super attack, monstret tar 30hp skada o du får 30hp")
    
    if random.random() < 0.2:
        hp_spelare -= 20
        hp-hp_monster += 15
        print("monstret kasstade ett eldklott på dig")
    
    print(f"Din HP: {hp_spelare} | Monster HP: {hp_monster}\n")

if hp_spelare > 0:
    print("Du vann!")
else:
    print("Du dog...")