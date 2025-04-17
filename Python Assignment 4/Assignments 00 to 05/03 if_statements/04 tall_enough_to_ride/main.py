MINIMUM_HEIGHT: int = 50  # Height in centimeters

def main():
    """Determine if user meets height requirement for attraction."""
    try:
        height = float(input("How tall are you (in centimeters)? "))
        if height >= MINIMUM_HEIGHT:
            print(f"\n🎉 Congratulations! At {height}cm, you're tall enough to ride!")
        else:
            print(f"\n📏 At {height}cm, you need {MINIMUM_HEIGHT - height:.1f}cm more to ride. Keep growing!")
            
    except ValueError:
        print("⚠️ Please enter a valid numerical height!")

if __name__ == '__main__':
    main()