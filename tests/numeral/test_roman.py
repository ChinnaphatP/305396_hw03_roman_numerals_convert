"""Test cases for Roman numerals."""

# Standard library

# Third party library
import pytest

# Project library
from Numerals.roman import to_roman


@pytest.mark.parametrize(
    "arabic_number, roman_number",
    [
        # Base case
        (1, "I"),
        (5, "V"),
        (10, "X"),
        (50, "L"),
        (100, "C"),
        (500, "D"),
        (1000, "M"),
        
        # Addition case
        (2, "II"),
        (3, "III"),
        (6, "VI"),
        (8, "VII"),
        
        # Subtraction case
        (4, "IV"),
        (9, "IX"),
        
    ]
)    

def test_to_roman(arabic_number, roman_number):
    """Convert Hindu-Arabic number to Roman number."""
    # Arrange
    
    # Act
    result = to_roman(arabic_number)
    
    # Assert
    assert result == roman_number