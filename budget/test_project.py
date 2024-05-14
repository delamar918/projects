import pytest
from project import get_budget, get_expense, itemize_it

def test_get_budget():
    with pytest.raises(TypeError):
        get_budget("b")

def test_get_expense():
    with pytest.raises(TypeError):
        get_expense(0.09)

def test_itemize_it(): #HUFO
    assert itemize_it([10,25,5,0]) == {"Utilities": 25, "Housing": 10, "Food": 5, "Miscellaneous": 0}
    assert itemize_it([100,10,0,-240]) == {"Housing": 100, "Utilities": 10, "Food": 0, "Miscellaneous": -240}
