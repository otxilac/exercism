def is_pangram(sentence: str) -> bool:
    """Checks whether a given sentence uses all the letters in the English
        alphabet.
    """
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    return not any(letter not in sentence.lower() for letter in alphabet)
