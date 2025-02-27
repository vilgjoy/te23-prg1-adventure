from equip import Inventory
from enemies import enemies

BATTLE_MAP = {
    (8, 14): "zenith_drone",
    (9, 14): "cyber_bandit",
    (17, 19): "cyber_bandit",
}

def check_and_start_battle(player, current_id, next_id, inventory):
    """Kollar om en strid ska startas baserat på BATTLE_MAP"""
    enemy_key = (current_id, next_id)
    if enemy_key in BATTLE_MAP:
        battle(player, BATTLE_MAP[enemy_key], inventory)
        if player["health"] > 0:
            return next_id  # uppdatera till nästa ID efter vinst
        else:
            return None  # spelaren dog, spelet slutar
    return next_id  # ingen strid, fortsätt spelet

def battle(player, enemy_name, inventory):
    base_enemy = enemies.get(enemy_name)
    if not base_enemy:
        print("Fiende inte hittad!")
        return
    
    enemy = base_enemy.copy()
    
    print(f"En {enemy.name} kom fram!")
    
    while player["health"] > 0 and enemy.health > 0:
        print("\nBattle Menu:")
        print("1. Attack")
        print("2. Använd Item")
        print("3. Skydda")
        print("4. Använd Skill")
        print("5. Kolla Status")
        
        choice = input("Välj (nummer): ")
        
        if choice == "1":
            damage = inventory.get_weapon_damage()  # Hämta vapenskada
            print(f"Du attackerar {enemy.name} för {damage} skada!")
            enemy.health -= damage
        elif choice == "2":
            print("Du kollade ditt inventory...")
            inventory.use_combat_item(player, enemy)
        elif choice == "3":
            print("Du förbereder dig för skada, vilket minskar skadorna denna sväng.")
        elif choice == "4":
            print("Du förbereder att använda en skill... (Not implemented yet)")
        elif choice == "5":
            print(f"Din HP: {player['health']}, {enemy.name} HP: {enemy.health}")
            continue  # Hoppa inte över turen
        else:
            print("Invalid choice!")
            continue
        
        if enemy.health > 0:
            print(f"{enemy.name} attackerar!")
            player["health"] -= enemy.attack
            print(f"Du tar {enemy.attack} skada!\n")
    
    if player["health"] <= 0:
        print("Du har blivit besegerad...")
    else:
        print(f"{enemy.name} har blivit besegerad!")
