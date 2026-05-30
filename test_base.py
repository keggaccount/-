import pytest
import random

@pytest.mark.hhh
def test_ok(f):
    # print(f)
    assert 1==1

@pytest.mark.ut
def test_fail():
    c=random.randint(1,9)
    assert c>5


