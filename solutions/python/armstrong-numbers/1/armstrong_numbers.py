def is_armstrong_number(number: int) -> bool:
    """Checks whether a number is an Armstrong number."""
    if number < 0:
        return False          
        
    digits = str(number) 
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return total == number
