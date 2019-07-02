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



### 类型

| 名称            | 描述       | 示例|
| --------------- | ---------- ||
| UnsignedInteger | 无符号整数 ||
| UnsignedFloat | 无符号浮点数 ||
| SizedString | 指定长度的字符串 ||
| Email | 邮箱 ||
| Bool | 无符号整数 ||
| CH | 纯文字 ||
| Number | 正负数，小数 ||
| Positive | 正数 ||
| PositiveInteger | 正整数 ||
| Month | 月份 ||
| Day | 天数 ||
| Time | 时间 ||
| Username | 长度至少为1，包含大小写字母、数字、_、- ||
| Password | 大小写字母或数字，长度至少6位 ||
| PasswordEasy | 6到16位的任意（除开斜线） ||
| PasswordHardL1 | 数字 + 字母（大写或小写） + 长度6到12位 ||
| PasswordHardL2 | 数字 + 字母（大写和小写） + 长度6到12位 ||
| Date | 日期 ||
| Birthday | 生日 ||
| BirthdayHard | 生日 ||
| Credit | 银行卡 ||
| Carcode | 车牌号 ||
| QQ | QQ号码 ||
| PhoneCommon |  ||
| Fax | 传真 ||
| PhoneCommon |  ||
| Phone |  ||
| Mobile| 手机 ||
| Url|  ||
| URL|  ||
| Ipv4Agent| ipv4私有地址 ||
| Ipv4| ipv4地址 ||
| Ipv6| ipv6地址 ||
| JsonHeader| json_header ||
| RequestHeader| request_header ||
| All| 所有 ||



### 规划

+ [x] 去除字段类型中的名称 
+ [x] 支持更多类型 
+ [x] 支持更多参数传入方式 
+ [ ] 更新优化错误提示 
+ [ ] 优化必选参数，更多值类型校验等


