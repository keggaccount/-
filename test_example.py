import pytest
import csv
def add(a, b):
    return a + b

def data(path):
    f=open(path)
    reader = csv.reader(f)
    return list(reader)[0:]

class Test_add:
    @pytest.mark.api
    def test_add(self):
        assert add(1,2) == 3
    @pytest.mark.api
    def test_str(self):
        assert add("1","2") == "12"
    @pytest.mark.pay
    def test_list(self):
        assert add([1],[2,3,4]) == [1,2,3,4]
    @pytest.mark.ddt
    @pytest.mark.parametrize(
        "a,b,c",
        data("data.csv")
    )
    def test_ddt(self,a,b,c):
        assert add(int(a),int(b))==int(c)
