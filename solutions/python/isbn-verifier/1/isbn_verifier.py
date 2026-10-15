def is_valid(isbn):
    clean_isbn = isbn.strip().replace("-", "")
    if len(clean_isbn) != 10:
        return False
    check_sum = 0
    for i, digit in enumerate(clean_isbn):
        if digit in "Xx" and i == 9:
            check_sum += 10 * (10 - i)
        elif digit.isdigit():
            check_sum += int(digit) * (10 - i)
        else:
            return False
    return check_sum % 11 == 0
        
            
