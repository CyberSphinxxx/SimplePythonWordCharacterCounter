while True:
    print("-------------------------------------------------------")
    input_text = input("Enter your text: ")
    choice = input("Do you want to count words (w) or characters (c)? ")

    if choice.lower() == "w":
        word_count = len(input_text.split())
        print("Word count:", word_count)

    elif choice.lower() == "c":
        char_count = len(input_text)
        print("Character count:", char_count)

    else:
        print("Invalid choice. Please choose 'w' for word count or 'c' for character count.")

    again = input("Do you want to count again? (y/n): ")
    if again.lower() != 'y':
        break
