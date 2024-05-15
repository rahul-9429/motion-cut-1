import re

def count_words(text):
    """
    Count the number of words in the given text using regular expression
    """
    words = re.findall(r'\b\w+\b', text)
    # Return the count of words
    return len(words)

def get_input():
    """
    Prompt the user to enter a sentence or paragraph.
    """
    print("Welcome to Word Counter!")
    while True:
        input_text = input("Please enter a sentence or paragraph: ").strip()
        # Check if input is empty
        if input_text:
            return input_text
        else:
            print("Error: Input cannot be empty. Please try again.")

def display_word_count(word_count):
    """
    Display the word count to the console.
    """
    print(f"\nWord count: {word_count}")

def main():
    # Get user input
    input_text = get_input()
    # Count words in input text
    word_count = count_words(input_text)
    # Display word count
    display_word_count(word_count)
if __name__ == "__main__":
    main()

