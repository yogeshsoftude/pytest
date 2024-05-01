from companies.views import fibonacci_naive, fibonacci_cached





# this code is repeating many times
def test_fib_naive() ->None:
    result = fibonacci_naive(0)
    assert result == 0
    result = fibonacci_naive(1)
    assert result == 1
    result = fibonacci_naive(1)
    assert result == 1
    result = fibonacci_naive(20)
    assert result == 6765


# use this 

'''
@pytest.mark.parametrize is a decorator provided by the Pytest framework in Python. 
It allows you to define multiple sets of arguments and fixtures for a test function. 
When you decorate a test function with @pytest.mark.parametrize, Pytest will run the test function once for each set of parameters you provide.'''
import pytest
@pytest.mark.parametrize("n,expected",[(0,0),(1,1),(2,1),(20,6765),(6,8)])
def test_fib_naive_para(n:int,expected:int) -> None:
    result = fibonacci_naive(n=n)
    assert result == expected



@pytest.mark.parametrize("n,expected",[(0,0),(1,1),(2,1),(20,6765),(6,8)])
def test_fib_naive_para_cached(n:int,expected:int) -> None:
    result = fibonacci_cached(n=n)
    assert result == expected
