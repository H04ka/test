from my_src.pow import Kolbasa
import pytest

@pytest.mark.kvadrat
def test_pow2():
    assert Kolbasa().pow2(5, 5) 
