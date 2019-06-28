from central import Agp
from model.extension import SizedString, UnsignedInteger, UnsignedFloat, Email, Bool


class Params(Agp):
    """
    定义期望的数据模型
    """
    name = SizedString(size=8)
    age = UnsignedInteger(min=100)
    salary = UnsignedFloat(max=10000)
    admin = Bool()
    email = Email()


params = Params("zhang", 100, 9800.1, True, "1234567@qq.com")
print(params.values)
