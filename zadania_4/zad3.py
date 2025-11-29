def check_if_number_is_even(num: int) -> bool:
    return num % 2 == 0


ans = check_if_number_is_even(9)
if ans:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")