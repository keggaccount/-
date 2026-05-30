import time
from selenium import webdriver
import pytest

@pytest.fixture(scope='function')
def ff():
    print('我也是fixture，被另一个fixtrue使用')

@pytest.fixture(autouse=True,scope='function')
def f(ff):
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),'用例开始执行时间')
    #前置操作
    yield '123'
    #后置操作
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), '用例结束执行时间')


@pytest.fixture
def selenium():
   d = webdriver.Chrome()
   yield d
   d.quit()