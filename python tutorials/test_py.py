import math_func
import pytest

def test_add():
    assert math_func.add(3,7)==10
    assert math_func.add(7)==9

def test_Product():
    assert math_func.product(5,5)==25
    assert math_func.product(5)==10

def test_add_strings():
    result=math_func.add('hello','world')
    assert result =="helloworld"
    assert type(result) is str
    assert "hello" in result

def test_product_strings():
    assert math_func.product('hello',3)=="hellohellohello"
    result=math_func.product("hello")
    assert result=="hellohello"
