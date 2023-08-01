from pytest_example import add_numbers

def test_add_numbers():
  assert add_numbers(5, 10) == 15
