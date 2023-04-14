import pytest
from unittest.mock import patch

# The function we want to test
def my_function(arg1, arg2):
    return arg1 + arg2

# The mock object we want to use as a replacement
class MyMock:
    def __init__(self, return_value):
        self.return_value = return_value
    
    def __call__(self, *args, **kwargs):
        return self.return_value

@pytest.fixture
def mock_my_function():
    with patch(__name__+'.my_function', new=MyMock(5)):
        yield my_function

def test_my_function(mock_my_function):
    # Now when my_function is called in this context it will always return 5
    assert mock_my_function(1, 2) == 5
