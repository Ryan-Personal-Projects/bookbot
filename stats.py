def word_counter(text):
    """
    Counts the number of words in a given text.

    A word is defined as any sequence of characters separated by whitespace.

    Args:
        text (str): The input string to count words from.

    Returns:
        int: The number of words in the input text.
    """
    return len(text.split())

def char_counter(text):
    """
    Counts the occurrences of each character in the given text.
    Args:
        text (str): The input string to analyze.
    Returns:
        dict: A dictionary where the keys are characters from the input text
              (converted to lowercase) and the values are their respective counts.
    """
    text = text.lower()
    char_count = {}

    for c in text:
        char_count[c] = 1 + char_count.get(c, 0)
    
    return char_count
