# 1
from itertools import chain


def is_palindrome(s) -> bool:
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# 2
def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# 3
def count_vowels(text: str) -> int:
    return len([c for c in text.lower() if c in 'aeiouyó'])

# 4
def calculate_discount(price: float, discount: float) -> float:
    if discount < 0 or discount > 1:
        raise ValueError

    return price - price * discount

# 5
def flatten_list(nested_list: list) -> list:
    result = []
    for element in nested_list:
        if isinstance(element, list):
            result.extend(flatten_list(element))
        else:
            result.append(element)
    return result

# 6
def word_frequencies(text: str) -> dict:
    text = text.lower()

    cleaned = ""
    for ch in text:
        if ch.isalnum() or ch.isspace():
            cleaned += ch

    result = {}
    for word in cleaned.split():
        result[word] = result.get(word, 0) + 1

    return result

# 7
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
    return True

