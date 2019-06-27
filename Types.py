from Rule import Typed, Unsigned, MaxSized


class Integer(Typed):
    """
    整型
    """
    expected_type = int


class Float(Typed):
    """
    浮点数
    """
    expected_type = float


class String(Typed):
    """
    字符串
    """
    expected_type = str


class Bool(Typed):
    """
    bool
    """
    expected_type = bool


class UnsignedInteger(Integer, Unsigned):
    """
    无符号整数
    """
    pass


class UnsignedFloat(Float, Unsigned):
    """
    无符号浮点数
    """
    pass


class SizedString(String, MaxSized):
    """
    指定大小的字符串
    """
    pass

