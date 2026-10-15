def is_armstrong_number(number: int) -> bool:
    """Checks whether a number is an Armstrong number."""
    if number < 0:
        return False          
        
    digits = str(number) 
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == number
