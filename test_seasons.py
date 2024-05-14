import pytest
import sys
import inflect

from seasons import calculate


def test_calc():
    assert calculate("2023-03-09") == 1440
    assert calculate("2022-03-10") == 525600
    assert calculate("1985-06-22") == 19836000

p = inflect.engine()

def test_translate():
    assert p.number_to_words(1440, andword="").capitalize() == "One thousand, four hundred forty"
    assert p.number_to_words(1, andword="").capitalize() == "One"
    assert p.number_to_words(0, andword="").capitalize() == "Zero"

