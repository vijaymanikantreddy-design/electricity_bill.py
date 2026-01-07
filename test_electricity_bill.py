import pytest
from electricity_bill import calculate_bill

def test_zero_units():
    assert calculate_bill(0) == 50  # Only fixed charge

def test_negative_units():
    try:
        calculate_bill(-10)
    except ValueError as e:
        assert str(e) == "Units consumed cannot be negative."

def test_100_units():
    assert calculate_bill(100) == 50 + 100 * 1.50

def test_150_units():
    assert calculate_bill(150) == 50 + (100 * 1.50) + (50 * 2.50)

def test_250_units():
    assert calculate_bill(250) == 50 + (100 * 1.50) + (100 * 2.50) + (50 * 4.00)

def test_350_units():
    assert calculate_bill(350) == 50 + (100 * 1.50) + (100 * 2.50) + (100 * 4.00) + (50 * 6.00)