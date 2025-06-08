def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item you want to add: ")
            if item.strip():  
                shopping_list.append(item)
                print(f"'{item}' has been added to your shopping list.")
            else:
                print("Invalid input. Item cannot be empty.")
                
        elif choice == '2':
            # Prompt for and remove an item
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                item = input("Enter the item you want to remove: ")
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"'{item}' has been removed from your shopping list.")
                else:
                    print("The item is not found in the list.")
                    
        elif choice == '3':

            if shopping_list:
                print("\nYour Shopping List:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")
                
        elif choice == '4':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")
        
        print()

if __name__ == "__main__":
    main()
