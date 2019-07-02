from AgileP.central import Agp
from AgileP.model.extension import SizedString, UnsignedInteger, UnsignedFloat, Email, Bool


class Params(Agp):
    """
    定义数据校验类
    """
    name = SizedString(length=8)
    age = UnsignedInteger(max=100)
    salary = UnsignedFloat(max=10000)
    admin = Bool()
    email = Email()

# 按照位置输入
P1 = Params("", 100, 9800.1, True, "1234567@qq.com")

# 位置 + 名称
P2 = Params(100, 9800.1, True, name="zhang", email="1234567@qq.com")

# 字典
P3 = Params(**{"name": "zhang", "email": "1234567@qq.com", "admin": True, "age": 28, "salary": 199.0})

print(P1.values)
print(P2.values)
print(P3.values)
