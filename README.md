# AgileP

### 简介
AgileP 是一个灵活的参数校验工具，支持绝大多数参数校验。

### 示例
```python
class UserInfoParams(Agp):
    """
    定义期望的数据模型
    """
    name = SizedString(size=8)
    age = UnsignedInteger(max=100, min=20)
    salary = UnsignedFloat()
    admin = Bool()

check_result = UserInfoParams("zhang", 10, 9800.1, False)
```

### 规划
+ [x] 去除字段类型中的名称 
+ [ ] 支持更多类型 
+ [ ] 支持更多参数传入方式 
+ [ ] 更新优化错误提示 


