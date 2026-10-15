def is_isogram(phrase):
    return not any(phrase.lower().count(letter) > 1 and letter.isalpha() for letter in phrase.lower())