__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    """
    Функция возвращает отношение суммы четных элементов массив к сумме нечетных
    Пример:
    even_odd([1, 2, 3, 4, 5]) == 0.8889
    """
    even = sum([i for i in arr if i % 2 == 0])
    odd = sum([i for i in arr if i % 2 == 1])
    if odd != 0:
        return even / odd
    return 0
