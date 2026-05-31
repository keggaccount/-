import pytest
import random
from test_example import add
@pytest.mark.hhh
def test_ok(f):
    # print(f)
    assert 1==1

@pytest.mark.ut
def test_fail():
    c=add(1,9)
    assert c>5


