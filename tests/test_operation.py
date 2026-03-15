from src.math_functions import add, subtract, multiply, divide

def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0
    
def test_subtract():
    assert subtract(5,3)==2
    assert subtract(4,3)==1
    assert subtract(3,3)==0
    assert subtract(2,3)==-1

def test_multiply():
    assert multiply(2,3)==6
    assert multiply(-1,1)==-1

def test_divide():
    assert divide(6,3)==2
    assert divide(4,2)==2
    try:
        divide(5,0)
        assert False, "Expected ValueError"
    except ValueError:
        pass