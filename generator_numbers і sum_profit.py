import re
from typing import Callable


def generator_numbers(text: str):
    for match in re.findall(r"\d+\.\d+", text):
        yield float(match)


def sum_profit(text: str, func: Callable[[str], float]) -> float:
    return sum(func(text))


text = "Загальний дохід працівника: 1000.01 основний дохід, 27.45 і 324.00 доларів."
print(f"Загальний дохід: {sum_profit(text, generator_numbers)}")
