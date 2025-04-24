from stats import word_counter, char_counter

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

def main():
    frankenstein_file_path = "./books/frankenstein.txt"
    frankenstein_text = get_book_text(frankenstein_file_path)
    word_count = word_counter(frankenstein_text)
    char_count = char_counter(frankenstein_text)
    print(f"{word_count} words found in the document")
    print(char_count)

main()
