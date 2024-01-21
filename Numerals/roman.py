"""The Roman numerals Module."""

class NumberOutOfRange(ValueError):
    """An extension in the standard exception."""


def to_roman(arabic):
    """Convert Hindu-Arabic number to Roman number."""
    if not 0 < arabic < 4000:
        raise NumberOutOfRange("Number out of range. (1 to 3,999)")
    
    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }
    
    result = ''
    for value, numeral in sorted(roman_numerals.items(), key=lambda x: x[0], reverse=True):
        while arabic >= value:
            result += numeral
            arabic -= value
            
    return result