import math

from fahrenheit_converter import (
    convert_celsius_to_fahrenheit,
    convert_fahrenheit_to_celsius,
)


def test_celsius_to_fehrenheit_with_zero():
    assert convert_celsius_to_fahrenheit(0) == 32


def test_celsius_to_fehrenheit():
    assert math.isclose(convert_celsius_to_fahrenheit(32.2), 89.96)


def test_convert_fahrenheit_to_celsius_with_zero():
    assert math.isclose(convert_fahrenheit_to_celsius(0), -17.77777777777778)


def test_convert_fahrenheit_to_celsius():
    assert math.isclose(convert_fahrenheit_to_celsius(89.96), 32.2)
