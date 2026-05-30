import allure
import pytest

#@allure.epic  #项目
#@allure.feature  #模块
#@allure. story  #功能
#@allure.title  #用例

@allure.epic('XXX')  #项目
@allure.feature('YYY') #模块
@allure. story('ccc') #功能
@allure.title('hhh')  #用例
@pytest.mark.ut
def test_hh():
    pass


@allure.epic('XXX')  #项目
@allure.feature('YYY') #模块
@allure. story('cc') #功能
@allure.title('hh')  #用例
@pytest.mark.ut
def test_ff():
    pass


