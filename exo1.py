def F_to_C(F: float):
    """
    Converts a Fahrenheit temperature to a Celsius temperature

    :param float F: The temperature to convert
    :return float F: The temperature in Celsius
    """

    assert F >= -459.67

    return round((F - 32) * 5 / 9, 2)


def C_to_F(C: float):
    """
    Converts a Celsius temperature to a Fahrenheit temperature

    :param float C: The temperature to convert
    :return float F: The temperature in Fahrenheit
    """

    assert C >= -273.15

    return round(9 * C / 5 + 32, 2)


assert F_to_C(-459.67) == -273.15, F_to_C(-459.67)
assert C_to_F(-273.15) == -459.67, C_to_F(-273.15)
