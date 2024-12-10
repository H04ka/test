from my_src.main import Calculation
import pytest

@pytest.mark.calc
def test_sum():
    assert Calculation().sum(3,2) == 5

@pytest.mark.calc
def test_sub():
    assert Calculation().sub(10, 3) == 7

@pytest.mark.calc
def test_mul():
    assert Calculation().mul(5, 5) == 25

@pytest.mark.calc
def test_div():
    assert Calculation().div(20, 2) == 10

@pytest.mark.skip("эта пристройка тут не нужна")
def test_invisible():
    assert 33 == 5

@pytest.mark.calc
def test_find_playndrome():
    assert 123

from my_src.main import Text_Greeting

@pytest.mark.parametrize('test_input,excepted',[('Ivan', 'My name Ivan'), ('Sarancha', 'my name Saranca')])
def test_greeting(test_input, excepted):
    assert Text_Greeting().greeting(test_input) == excepted

@pytest.mark.text
def test_empty_string():
    assert Text_Greeting().empty_string("vodka") == True
    
@pytest.mark.text
def test_register_check():
    assert Text_Greeting().register_check("shobla") == "shobla".lower

@pytest.mark.text
def test_long_check():
    assert Text_Greeting().long_check("sdaasdad") == True

@pytest.mark.text
def text_string_type():
    assert Text_Greeting().string_type("aaaa") == str("aaaa")

@pytest.mark.skip("Эта пристройка тоже не нужна")
def test_invisible():
    assert ""
