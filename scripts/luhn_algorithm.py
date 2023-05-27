def luhn_algorithm(card_number:str)->bool:
    """
    Func that checks the correctness of the card number
    Args:
        card_number (str): card number

    Returns:
        bool: correctness
    """
    digits = list(map(int, str(card_number)))[::-1]
    for i in range(1, len(digits), 2):
        digits[i]*=2
        if digits[i]>9:
            digits[i] = digits[i] // 10 + digits[i] % 10
    return sum(digits) % 10 == 0 