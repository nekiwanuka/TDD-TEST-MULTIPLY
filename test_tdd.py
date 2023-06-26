"""
 Assignment TDD Test file of PYTHON
"""
from multiply import multiply

# TDD Cycle 1


# My first TDD first test cycle
# defining my function test_tdd_multiply1()
def test_tdd_multiply1():
    """Test"""  # docstring help define func params, return values, (Read about them)
    assert multiply(1, 1) == 1


# 1st Test using pytest
# => This test FAILED for i have no multiply()


# ====================================================================
# TDD Cycle 2
def test_tdd_multiply2():
    """
    This function multiplies 2 by 2 and return 4
    """
    assert multiply(2, 2) == 4


# 2nd Test using pytest
# => This test PASSED forit has the multiply()  defined


# ====================================================================
# TDD Cycle 3
def test_tdd_multiply3():
    """
    This function multiplies 3 by 3 and return 9
    """
    assert multiply(3, 3) == 9


def test_tdd_multiply4():
    """Testing multiply with (4,4)"""
    assert multiply(4, 4) == 16


def test_tdd_multiply5():
    """Testing multiply with (23,45)"""
    # With this test its better to put calculator value as result
    assert multiply(23, 45) == 1035
