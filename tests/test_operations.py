from src.math_operations import add,sub

def test_add():
    assert add(5, 3) == 8
    assert add("Vishal"," Mendhikar") == "Vishal Mendhikar"
    assert add(1,1) ==2

def test_sub():
    assert sub(5, 3) == 2
    assert sub(1,1) == 0