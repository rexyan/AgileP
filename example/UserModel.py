from tools.AgileP.Types import SizedString, UnsignedInteger, UnsignedFloat
from tools.AgileP.BaseStruct import APBase

class LoginParams(APBase):
    """
    定义期望的数据模型
    """
    name = SizedString('name', size=8)
    age = UnsignedInteger('age')
    salary = UnsignedFloat('salary')


s1 = LoginParams("zhang", 20, 9800.1)
print(s1.name)