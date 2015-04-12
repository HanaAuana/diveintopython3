roman_numeral_map = (('M', 1000),
                     ('CM', 900),
                     ('D', 500),
                     ('CD', 400),
                     ('C', 100),
                     ('XC', 90),
                     ('L', 50),
                     ('XL', 40),
                     ('X', 10),
                     ('IX', 9),
                     ('V', 5),
                     ('IV', 4),
                     ('I', 1))


class OutOfRangeError(ValueError):
    pass


class NotIntegerError(ValueError):
    pass


class InvalidNumeralError(ValueError):
    pass

to_roman_table = [None]
from_roman_table = {}


def to_roman(n):
    """convert integer to roman roman_numeral_map."""

    if int(n) != n:
        raise NotIntegerError('non-integers can not be converted')
    elif not (0 < n < 5000):
        raise OutOfRangeError('number out of range (must be between 1..4999)')
    return to_roman_table[n]


def from_roman(s):
    """convert roman numeral to integer."""

    if not isinstance(s, str):
        raise InvalidNumeralError('Input must be a string')
    elif not s:
        raise InvalidNumeralError('Input can not be blank')
    elif s not in from_roman_table:
        raise InvalidNumeralError('Invalid Roman numeral: {0}'.format(s))
    return from_roman_table[s]


def build_lookup_tables():
    def to_roman(n):
        result = ''
        for numeral, integer in roman_numeral_map:
            if n >= integer:
                result = numeral
                n -= integer
                break
        if n > 0:
            result += to_roman_table[n]
        return result

    for integer in range(1, 5000):
        roman_numeral = to_roman(integer)
        to_roman_table.append(roman_numeral)
        from_roman_table[roman_numeral] = integer

build_lookup_tables()
