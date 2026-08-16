from typing import List

def word_len(word):
    return len(word)

def absolute_value(num):
    return abs(num)

def sort_words(words: List[str]) -> List[str]:
    words.sort(key = word_len, reverse=True)
    return words


def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(key=absolute_value)
    return numbers


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
