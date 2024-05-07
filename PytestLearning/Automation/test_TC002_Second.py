import pytest

def test_addition_pytest():
    assert 2 + 6 == 8

@pytest.mark.skip("Skipping this test case as this functionality is not working developer will fix it in new built")
def test_helloWorld():
    print("*********************Hello PyTest************************")

a=101
@pytest.mark.skipif(a>30,reason="Skipping this test case as this functionality is not working developer will fix it in new built")
def test_condition():
    print("*********************Executing if greater than 30************************")