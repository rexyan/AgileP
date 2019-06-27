from Types import SizedString, UnsignedInteger, UnsignedFloat, Bool
from Central import Agp


class LoginParams(Agp):
    """
    定义期望的数据模型
    """
    name = SizedString(size=8)
    age = UnsignedInteger(max=100, min=20)
    salary = UnsignedFloat()
    admin = Bool()


s1 = LoginParams("zhang", 10, 9800.1, False)
print(s1.name)
