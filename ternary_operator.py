def rebate_calculator(sales: float | int) -> int:
    if sales < 3:
        rebate = 10
    else:
        rebate = 15
    return rebate


def bonus_calculator(sales: float | int) -> int:
    bonus = 10 if sales < 3 else 15
    return bonus
