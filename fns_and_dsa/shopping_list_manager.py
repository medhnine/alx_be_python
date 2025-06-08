def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    value = 0
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == '1':
            # Prompt for and add an item
            value = int(input("inter the item you want to add: "))
            if value:
              shopping_list.append(value)
            else:
                value = int(input("invalide input, reinter the item you want to add: "))
            pass
        elif choice == '2':
            # Prompt for and remove an item
            value = int(input("inter the item you want to remove: "))
            if value in shopping_list:
                shopping_list.remove(value)
            else:
                value = int(input("the item is not found in the list."))
            pass
        elif choice == '3':
            # Display the shopping list
            print(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
