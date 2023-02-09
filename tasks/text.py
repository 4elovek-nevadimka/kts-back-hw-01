from typing import Optional
import re

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """

    regex = r'\b\w+\b'
    words_list = re.findall(regex, text)

    if len(words_list) > 0:
        longest = max(words_list, key=len)
        shortest = min(words_list, key=len)
        return shortest, longest

    return None, None
