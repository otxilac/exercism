def is_pangram(sentence: str) -> bool:
    """Checks whether a given sentence uses all the letters in the English
        alphabet.
    """
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    for letter in alphabet:
        if letter not in sentence.lower():
            return False
    return True
