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

def sort_char_dict(char_dict):
    """
    Sorts a dictionary of characters and their counts in descending order of counts.

    Args:
        char_dict (dict): A dictionary where keys are characters (str) and values are their counts (int).

    Returns:
        list: A list of dictionaries, each containing:
            - "char" (str): The character.
            - "num" (int): The count of the character.
        The list is sorted in descending order based on the "num" value.
    """
    sorted_list = []

    for k, v in char_dict.items():
        sorted_list.append({"char": k, "num": v})

    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list
