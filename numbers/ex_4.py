def is_divisible_by_4(year):
    return not year % 4


def is_divisible_by_100(year):
    return not year % 100


def is_divisible_by_400(year):
    return not year % 400


def is_leap_year(year):
    """
    is_leap_year function takes year and return 'leap year' if it is leap year or 'not leap year' otherwise
    year is leap if
    1) year is divisible by 4.
    1.1) year is not divisible by 100.
    1.2) year is divisible by 100 and divisible by 400.
    """
    if is_divisible_by_4(year):
        if not is_divisible_by_100(year):
            return "leap year"
        if is_divisible_by_400(year):
            return "leap year"

    return "not leap year"


year = int(input("Enter year : "))

print(is_leap_year(year))
