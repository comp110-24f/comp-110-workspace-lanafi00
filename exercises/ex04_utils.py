"""reverse engineering stuff?"""

__author__: str = "730732929"


def all(list: list[int], num: int) -> bool:
    indx: int = 0
    while indx < len(list):
        if num != list[indx]:
            return False
        indx = indx + 1
    return True


def max(list: list[int]) -> int:
    if len(list) == 0:
        raise ValueError("max() arg is an empty List")
    indx: int = 1
    max: int = list[0]
    while indx < len(list):
        if list[indx] > max:
            max = list[indx]
        indx = indx + 1
    return max


def is_equal(list1: list[int], list2: list[list]) -> bool:
    if len(list1) != len(list2):
        return False
    indx: int = 0
    while indx < len(list1):
        if list1[indx] != list2[indx]:
            return False
        indx = indx + 1
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    indx: int = 0
    while indx < len(list2):
        list1.append(list2[indx])
        indx = indx + 1
