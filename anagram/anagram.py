#!.venv/bin/python3


# File: anagram.py
# Author: Jonathan Belden


import itertools


def permutations(jumble:str, no_punct:bool=False) -> list:
    jumble = __remove_punctuation(jumble) if no_punct else jumble

    permutations = list(itertools.permutations(jumble))
    solutions = []
    for item in permutations:
        solution = f"{item[0]}{item[1]}{item[2]}"
        print(solution)
        solutions.append(solution)

    return solutions


def __remove_punctuation(jumble:str) -> str:
    return "".join(char for char in jumble if char.isalnum())
