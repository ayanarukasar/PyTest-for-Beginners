import pytest

@pytest.mark.smoke
@pytest.mark.regression
def test_addition():
    print("This is Smoke Test")
    print("This is Regression Test")
    assert 2 + 2 == 4

@pytest.mark.sanity
@pytest.mark.regression
def test_substraction():
    print("This is Sanity Test")
    print("This is Regression Test")
    assert 5 - 3 == 2

@pytest.mark.smoke
def test_multiplication():
    print("This is Smoke Test")
    assert 5 - 3 == 2
