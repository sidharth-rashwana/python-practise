
def dayOfProgrammer(year):
    # Check if it's a Julian or Gregorian calendar
    if year < 1918:
        is_julian = True
    elif year > 1918:
        is_julian = False
    elif year == 1918:
        return "26.09.1918"
    # if julian and leap year or not julian and leap year
    if (is_julian and year %
        4 == 0) or (not is_julian and ((year %
                                        400 == 0) or (year %
                                                      4 == 0 and year %
                                                      100 != 0))):
        # leap year
        return f"12.09.{year}"
    else:
        # not leap year
        return f"13.09.{year}"


print(dayOfProgrammer(1800))
