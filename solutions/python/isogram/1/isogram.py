def is_isogram(phrase):
    for letter in phrase.lower():
        if phrase.lower().count(letter) > 1 and letter.isalpha():
            return False
    return True