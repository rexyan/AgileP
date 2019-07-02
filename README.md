# AgileP

### 简介
AgileP 是一个灵活的参数校验工具，支持绝大多数参数校验。



### 安装

```
pip install AgileP
```



### 示例

```python
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
```



### 规划

+ [x] 去除字段类型中的名称 
+ [x] 支持更多类型 
+ [x] 支持更多参数传入方式 
+ [ ] 更新优化错误提示 
+ [ ] 优化必选参数，更多值类型校验等


