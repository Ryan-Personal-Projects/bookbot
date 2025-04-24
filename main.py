import sys
from stats import (
    word_counter, 
    char_counter, 
    sort_char_dict
)

def get_book_text(file_path):
    """
    Reads the content of a book file and returns it as a string.
    
    Args:
        file_path (str): The path to the book file.
        
    Returns:
        str: The content of the book.
    """
    with open(file_path) as f:
        return f.read()

def print_report(book_path, word_count, sorted_chars):
    """
    Prints a formatted report of the analysis of a book.

    Args:
        book_path (str): The file path to the book being analyzed.
        word_count (int): The total number of words in the book.
        sorted_chars (list of dict): A list of dictionaries containing character 
            counts, where each dictionary has the keys:
            - "char" (str): The character.
            - "num" (int): The count of the character.

    Returns:
        None
    """
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():
            char = item["char"]
            num = item["num"]
            print(f"{char}: {num}")   
    print("============= END ===============")


def main():
    args = sys.argv
    if not len(args) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = args[1]
    text = get_book_text(book_path)
    word_count = word_counter(text)
    char_count = char_counter(text)
    sorted_char_count = sort_char_dict(char_count)
    print_report(book_path, word_count, sorted_char_count)

main()
