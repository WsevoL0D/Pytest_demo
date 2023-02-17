
def test_example():
  assert "amazing" in "Python is amazing"
  assert "java" not in "Python is amazing"
  assert len("PyTest is amazing") == 17
  print("Print in test")

def some_function():
  assert "Black" == "White"


def test_example_2():
  strings = [ "Batm" + 'a' * x + 'n'  for x in range(10)]
  for i, s in enumerate(strings):
    assert s.count('a') == i + 1
  print("Some print")

# def test_failed_test():
#   assert "python" in "Python is amazing"

# TASK (10 min) : Write tests for:
#   upper / lower functions
#   split() function
#   join() function
#   reversed() function