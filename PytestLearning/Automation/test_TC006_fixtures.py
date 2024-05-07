import pytest

@pytest.fixture(scope="session", autouse=True)
def execute_only_once():
    # Code to execute only once for the entire test session
    print("Executed only once")

def test_example():
    # Test case
    print("Test execution")
    assert True


# #After
# @pytest.fixture(scope="function")
# def teardown_after_test():
#     # Code to execute after the test case
#     yield
#     # Teardown code
#     print("Teardown after test")

# def test_example(teardown_after_test):
#     # Test case using the fixture
#     print("Test execution")
#     assert True

# #Before
# @pytest.fixture(scope="function")
# def setup_before_test():
#     # Code to execute before the test case
#     print("Setup before test")
#     yield
#     # Teardown code (optional)
#     print("Teardown after test")

# def test_example(setup_before_test):
#     # Test case using the fixture
#     print("Test execution")
#     assert True
