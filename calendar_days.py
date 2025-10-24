import calendar
def number_of_days(year, month):
    """Return the number of days in a given month of a given year."""

    assert isinstance(year, int), "Year must be an integer"
    assert isinstance(month, int), "Month must be an integer"
    assert year >= 0, "Year must be non-negative"
    assert 1 <= month <= 12, "Month must be between 1 and 12"

    return calendar.monthrange(year, month)[1]

def number_of_leap_years(year1, year2):
    """Return the number of leap years between year1 and year2, inclusive."""
    assert isinstance(year1, int), "Year1 must be an integer"
    assert isinstance(year2, int), "Year2 must be an integer"
    assert year1 >= 0, "Year1 must be non-negative"
    assert year2 >= 0, "Year2 must be non-negative"
    assert year1 <= year2, "Year1 must be less than or equal to Year"

    return calendar.leapdays(year1, year2 + 1)

def get_day_of_week(year,month,day):
    """Return the day of the week for a given date."""
    assert isinstance(year, int), "Year must be an integer"
    assert isinstance(month, int), "Month must be an integer"
    assert isinstance(day, int), "Day must be an integer"
    assert year >= 0, "Year must be non-negative"
    assert 1 <= month <= 12, "Month must be between 1 and 12"
    assert 1 <= day <= number_of_days(year, month), "Day is out of range for the given month and year"
    
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day = calendar.weekday(year, month, day)
    return days[day]