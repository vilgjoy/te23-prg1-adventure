from book import BOOK 
from equip import Inventory
from enemies import enemies
from battle import battle, check_and_start_battle

# om svaret är något annat än en int, blir svaret fel
def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_page(book_data, page_id):
    for page in book_data:
        if page["id"] == page_id:
            return page
    return None

# sidan. (titeln), (beskrivningen), (och) options)
def show_page(page):
    print("\n" + "=" * 50) # separator linje
    print(f"\n {page['title'].upper()}\n")
    print(page["text"] + "\n")
    for i, option in enumerate(page["options"]):
        print(f"{i + 1}. {option['text']}")

    print(f"{len(page['options']) + 1}. Open inventory (Change Weapon)")

# inventory och hur options fortsätter äventyret
def main():
    current_id = 1
    inventory = Inventory()
    inventory.main_inventory["weapon"] = {"name": "Basic Pistol", "damage": 5}  # startvapen
    player = {"health": 30}  # spelarens hälsa
    
    while True and current_id is not None:
        current_page = get_page(BOOK, current_id)
        if current_page is None:
            print(f"ERROR: Ingen sida hittades med ID {current_id}!")
            break
        
        show_page(current_page)
        
        if "loot" in current_page:
            loot = current_page["loot"]
            print(f"Du hittade {loot}!")

            if loot == "EMP-granat":
                inventory.add_item("EMP-granat")  
            elif loot == "Medkit":
                inventory.add_item("Medkit")
            elif loot in ["Databricka med Zeniths hemligheter", "Dyrkverktyg", "Kreditchips"]:
                inventory.add_item(loot)  # Quest-item läggs till
            elif loot == "Laser Rifle":  
                inventory.add_weapon("Laser Rifle", 12)  # Laser Rifle med 12 i skada
        
        choice = input_int("Enter your choice: ")
        
        if 1 <= choice <= len(current_page["options"]):
            next_id = current_page["options"][choice - 1]["next_id"]
            
            # kontrollera om en strid ska startas och uppdatera next_id efter strid
            next_id = check_and_start_battle(player, current_id, next_id, inventory)
            
            if next_id is None:  # om spelaren dog
                print("Game over.")
                break
            # kontrollera om sida existerar
            if get_page(BOOK, next_id) is None:
                print(f"ERROR: Ingen sida hittades med ID {next_id}!")
                break
            
            current_id = next_id
            
        elif choice == len(current_page["options"]) + 1:
            inventory.weapon_menu()

        else:
            print("Invalid choice. Please try again.")
            current_id = None

if __name__ == "__main__":
    main()