from book import BOOK
# if answer is anything other than a number, it's invalid
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

# the page. (The title), (The descrpition), (and the options)
def show_page(page):
    print(page["title"])
    print(page["text"])
    for i, option in enumerate(page["options"]):
        print(f"{i + 1}. {option['text']}")

# inventory and how the options continue the adventure, i guess?
def main():
    current_id = 1
    inventory = []
    while True and current_id is not None:
        current_page = get_page(BOOK, current_id)
        show_page(current_page)
        if "loot" in current_page:
            print(f"You found {current_page['loot']}!")
            inventory.append(current_page["loot"])
        choice = input_int("Enter your choice: ")
        if 1 <= choice <= len(current_page["options"]):
            current_id = current_page["options"][choice - 1]["next_id"]
        else:
            print("Invalid choice. Please try again.")
            current_id = None


if __name__ == "__main__":
    main()
