def get_expected_data():
    mul = 3 * 2
    return mul

def get_actual_data():
    sum = 3 + 3
    return sum

def get_unexpected_data():
    mul = 3 * 8
    return mul

def test_compare_data_custom_message():
    actual_data = get_actual_data()
    expected_data = get_expected_data()
    try:
        assert actual_data == expected_data
    except AssertionError:
        raise AssertionError("Customized message: Actual data does not match expected data")

# def test_compare_data_not_same():
#     actual_data = get_actual_data()
#     unexpected_data = get_unexpected_data()
#     assert actual_data != unexpected_data, "Actual data matches unexpected data"

# def test_compare_data_same():
#     actual_data = get_actual_data()
#     expected_data = get_expected_data()
#     assert actual_data == expected_data, "Actual data does not match expected data"