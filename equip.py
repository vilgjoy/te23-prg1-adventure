class Inventory: 
    def __init__(self):
        self.main_inventory = {"weapon": {"name": "Basic Pistol", "damage": 5}}  # Huvudinventariet med utrustat vapen
        self.inventory = []  # Vanligt inventory för vapen
        self.items = {  # Items som kan användas i strid
            "EMP-granat": {"type": "combat", "effect": "stun_enemy"},
            "Medkit": {"type": "combat", "effect": "heal_player"},
        }

    def add_weapon(self, weapon_name, damage):
        for weapon in self.inventory:
            if weapon["name"] == weapon_name:
                print(f"Du har redan {weapon_name} i ditt inventory.")
                return

        if self.main_inventory["weapon"]["name"] == weapon_name:
            print(f"Du har redan {weapon_name} som ditt huvudvapen.")
            return

        print(f"Du hittade ett nytt vapen: {weapon_name}!")
        self.inventory.append({"name": weapon_name, "damage": damage})
    
    def get_weapon_damage(self):
        return self.main_inventory["weapon"]["damage"]

    def add_weapon(self, weapon_name, damage):
        print(f"Du hittade ett nytt vapen: {weapon_name}!")
        self.inventory.append({"name": weapon_name, "damage": damage})

    def add_item(self, item):
        if item in self.items:
            print(f"Du hittade {item}!")
        else:
            print(f"{item} lades till i ditt inventory!")
            self.items[item] = {"type": "combat", "effect": None}  # Default om ingen effekt finns

    def use_combat_item(self, player, enemy):
        # visar och låter spelaren använda stridsföremål
        combat_items = {k: v for k, v in self.items.items() if v["type"] == "combat"}

        if not combat_items:
            print("Du har inga användbara föremål i strid.")
            return

        print("\nAnvändbara föremål:")
        for i, (item, details) in enumerate(combat_items.items(), 1):
            print(f"{i}. {item}")

        choice = input("Välj föremål (nummer) eller 0 för att avbryta: ")
        if choice == "0":
            return

        try:
            item_name = list(combat_items.keys())[int(choice) - 1]
            effect = combat_items[item_name]["effect"]
        except (IndexError, ValueError):
            print("Ogiltigt val.")
            return

        if effect == "stun_enemy":
            print(f"Du kastar en {item_name}! Fienden tar 10 skada!")
            enemy.health -= 10
        elif effect == "heal_player":
            print(f"Du använder en {item_name} och återfår 10 HP!")
            player["health"] += 10

        del self.items[item_name]  # Ta bort föremålet efter användning

    def show_inventory(self):
        print("\n=== INVENTORY ===")
        print(f"Main Weapon: {self.main_inventory['weapon']['name']} (Skada: {self.main_inventory['weapon']['damage']})")
        if self.inventory:
            print("Other Weapons:")
            for weapon in self.inventory:
                print(f"- {weapon['name']} (Skada: {weapon['damage']})")
        else:
            print("Other Weapons: None")
        print("Items:", ', '.join(self.items.keys()) if self.items else "None")

    def weapon_menu(self):
        while True:
            self.show_inventory()
            print("Välj ett vapen att använda eller skriv 'exit' för att gå tillbaka:")
            choice = input("Vapens namn: ")
            if choice.lower() == 'exit':
                break
            self.equip_weapon(choice)

