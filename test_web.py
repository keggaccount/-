import pytest
import time

@pytest.mark.web
def test_web(selenium):

    selenium.get('https://www.baidu.com/')
    print(selenium)
    time.sleep(1)
