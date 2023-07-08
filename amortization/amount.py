

def calculate_amortization_amount(principal: float, interest_rate: float, period: int) -> float:
    """
    Calculates Amortization Amount per period

    >>> calculate_amortization_amount(150000, 0.1, 36)
    4840.08

    :param principal: Principal amount
    :param interest_rate: Interest rate per period
    :param period: Total number of period
    :return: Amortization amount per period
    """
    x = (1 + interest_rate) ** period
    return principal * interest_rate * x / (x - 1)
