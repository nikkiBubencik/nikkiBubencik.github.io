import math
from typing import Callable


class Rational:
    """
    Rational Class with two private integers (numerator and denominator)

    has two methods called equals and as_float
    """
    _gcd_helper: Callable[[int, int], int] = None

    def __init__(self, numerator: int, denominator: int):
        """
        sets the value of Class' numerator and denominator
        makes sure denominator is valid
        :param numerator: integer
        :param denominator: integer
        :return:
        """
        if denominator == 0:
            raise ValueError("Denominator must not be zero")
        self._numerator: int = numerator
        self._denominator: int = denominator

    def equals(self, rational_number) -> bool:
        """
        method to see if two rational numbers are equal with same numerator and _denominator

        :param : rational_number:  another rational number

        :return: true when numerators and denominators are the same
        """
        if self._numerator == rational_number._numerator:
            return self._denominator == rational_number._denominator

        return False

    def as_float(self) -> float:
        """ method to return the rational number as a float value

        :param: none

        :return: float of rational number
        """
        return self._numerator / self._denominator

    def standard_form(self) -> 'Rational':
        """ Returns an equivalent Rational in standard form.
        The standard, or canonical, form of a Rational has a
        positive denominator and the numerator and denominator
        are coprime -- their greatest common factor is 1.
        (Thinking of the rational as a fraction, the fraction
        cannot be reduced/simplified.)
        if denominator is < 0 multiply both numerator and denominator by -1
        :return: a new, equivalent Rational in standard form
        """
        std_numerator = self._numerator
        std_denominator = self._denominator
        if std_denominator < 0:
            std_numerator = -std_numerator
            std_denominator = -std_denominator
        divisor = Rational._gcd_helper(std_numerator, std_denominator)
        std_numerator //= divisor
        std_denominator //= divisor
        return Rational(std_numerator, std_denominator)


if __name__ == '__main__':
    rational12 = Rational(1, 2)
    rational23 = Rational(2, 3)
    print("Test rational12 equals another Rational(1,2):", "passed" if rational12.equals(Rational(1, 2)) else "failed")
    print("Test rational12 not equals rational23:", "passed" if not rational12.equals(rational23) else "failed")