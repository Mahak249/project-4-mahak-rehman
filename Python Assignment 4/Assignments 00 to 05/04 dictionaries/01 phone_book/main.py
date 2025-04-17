def display_header():
    """Display a stylish header for the phonebook application"""
    print("\n" + "=" * 50)
    print("||" + " " * 46 + "||")
    print("||           PHONEBOOK APPLICATION           ||")
    print("||" + " " * 46 + "||")
    print("=" * 50 + "\n")

def read_phone_numbers(phonebook):
    """
    Ask the user for names/numbers to store in the phonebook.
    """
    print("\n" + "-" * 50)
    print("📝 ADD CONTACTS (Leave name blank to finish)")
    print("-" * 50)
    
    while True:
        name = input("\nName: ").strip()
        if not name:
            break
        number = input("Number: ").strip()
        phonebook[name] = number
        print(f"✅ Added {name} to phonebook!")
    
    return phonebook

def print_phonebook(phonebook):
    """
    Prints out all the names/numbers in the phonebook.
    """
    if not phonebook:
        print("\n📭 The phonebook is empty!")
        return
    
    print("\n" + "-" * 50)
    print("📖 PHONEBOOK CONTENTS")
    print("-" * 50)
    
    for name, number in sorted(phonebook.items()):
        print(f"\n👤 {name.upper():<20} 📞 {number}")
    
    print("\n" + "-" * 50)
    print(f"Total contacts: {len(phonebook)}")
    print("-" * 50)

def lookup_numbers(phonebook):
    """
    Allow the user to lookup phone numbers.
    """
    if not phonebook:
        print("\n⚠️  Cannot lookup - phonebook is empty!")
        return
    
    print("\n" + "-" * 50)
    print("🔍 CONTACT LOOKUP (Leave blank to return)")
    print("-" * 50)
    
    while True:
        name = input("\nEnter name to lookup: ").strip()
        if not name:
            break
        
        if name not in phonebook:
            print(f"❌ {name} is not in the phonebook")
        else:
            print(f"✅ Found {name}: {phonebook[name]}")

def display_menu():
    """Show the main menu options"""
    print("\n" + "-" * 50)
    print("📱 MAIN MENU")
    print("-" * 50)
    print("1. Add new contacts")
    print("2. View all contacts")
    print("3. Lookup a contact")
    print("4. Exit")
    print("-" * 50)
    return input("Enter your choice (1-4): ").strip()

def main():
    phonebook = {}
    display_header()
    
    while True:
        choice = display_menu()
        
        if choice == "1":
            phonebook = read_phone_numbers(phonebook)
        elif choice == "2":
            print_phonebook(phonebook)
        elif choice == "3":
            lookup_numbers(phonebook)
        elif choice == "4":
            print("\n" + "=" * 50)
            print("Thank you for using the Phonebook Application!")
            print("=" * 50 + "\n")
            break
        else:
            print("\n⚠️  Invalid choice. Please enter 1-4.")

if __name__ == '__main__':
    main()