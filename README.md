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
    name = SizedString(size=8)
    age = UnsignedInteger(min=100)
    salary = UnsignedFloat(max=10000)
    admin = Bool()
    email = Email()

params = Params("zhang", 100, 9800.1, True, "1234567@qq.com")
print(params.values)

```



### 规划

+ [x] 去除字段类型中的名称 
+ [x] 支持更多类型 
+ [ ] 支持更多参数传入方式 
+ [ ] 更新优化错误提示 


