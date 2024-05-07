import pytest

@pytest.mark.sanity
def test_addition_pytest():
    print("This is Sanity Test")
    assert 2 + 6 == 8

@pytest.mark.sanity
@pytest.mark.regression
#@pytest.mark.skip("Skipping this test case as this functionality is not working developer will fix it in new built")
def test_helloWorld():
    print("This is Sanity Test")
    print("This is Regression Test")
    print("*********************Hello PyTest************************")

@pytest.mark.smoke
@pytest.mark.regression
# a=101
# @pytest.mark.skipif(a>30,reason="Skipping this test case as this functionality is not working developer will fix it in new built")
def test_condition():
    print("This is Smoke Test")
    print("This is Regression Test")
    print("*********************Executing if greater than 30************************")