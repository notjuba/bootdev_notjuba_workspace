def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    chars = {}
    for char in text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def not_sort(text):
    pass
    # Sort the dictionnary based on value (descending)

    # Construct a list from the sorted dictionnary

    

