def test_divisible_by_3(test_data):
    assert test_data % 3 == 0


# Should fail
def test_divisible_by_6(test_data):
    assert test_data % 6 == 0


def test_divisible_by_13(test_data):
    assert test_data % 13 == 0
