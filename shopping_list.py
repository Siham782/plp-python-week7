

# Part B: Shopping List Manager

shopping_list = []

while True:
    print("\n--- Shopping List Menu ---")
    print("add / remove / show / done")

    action = input("What would you like to do? ").strip().lower()

    if action == "add":
        item = input("Enter an item to add: ").strip()
        if item:
            shopping_list.append(item)
            print(item, "added to your list.")
        else:
            print("Please enter a valid item.")

    elif action == "remove":
        item = input("Enter an item to remove: ").strip()
        if item in shopping_list:
            shopping_list.remove(item)
            print(item, "removed from your list.")
        else:
            print("That item is not on your list.")

    elif action == "show":
        print("\nYour shopping list:")
        if shopping_list:
            for item in shopping_list:
                print(item)
        else:
            print("Your shopping list is empty.")

    elif action == "done":
        print("Goodbye! Happy shopping!")
        break

    else:
        print("Invalid choice. Type add, remove, show, or done.")