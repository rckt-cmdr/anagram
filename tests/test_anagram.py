#!.venv/bin/python3


# File: test_anagram.py
# Author: Jonathan Belden


import pytest
from anagram import anagram


@pytest.fixture()
def test_string() -> str:
    # return "bc-a"
    return "PWUMCOWLM.OONSI-A.WS"


def test_unscramble(test_string):
    potential_solutions = anagram.permutations(test_string)
    assert type(potential_solutions) is list
    assert len(potential_solutions) > 0
    # assert "cab" in potential_solutions


def test_unscramble_removing_punctuation(test_string):
    potential_solutions = anagram.permutations(test_string, no_punct=True)
    assert type(potential_solutions) is list
    assert len(potential_solutions) > 0
    # assert "cab" in potential_solutions
