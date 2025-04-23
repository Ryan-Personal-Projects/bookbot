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
    print(get_book_text(frankenstein_file_path))

main()
