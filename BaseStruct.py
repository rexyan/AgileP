def register_fields(cls):
    pass


class Meta(type):
    def __new__(cls, *args, **kwargs):
        """
        1. cls 为当前准备创建对象的类
        2. args 中第一个参数为类的名字
        3. args 中第二个参数为类继承的父类集合
        4. args 中第三个参数为类的方法集合
        :param args:
        :param kwargs:
        :return:
        """
        cls = type.__new__(cls, *args, **kwargs)
        register_fields(cls)
        return cls


class APBase(metaclass=Meta):
    def __init__(self, *args, **kwargs):
        self._fields = [x for x in self.__dir__() if not x.startswith("_")]

        # 字段基本校验。校验传入和定义是否一致
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')

        # 动态构建属性
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # 动态构建属性（声明式构建）
        extra_args = kwargs.keys() - self._fields
        for name in extra_args:
            setattr(self, name, kwargs.pop(name))

        # 字段基本校验
        if kwargs:
            raise TypeError(f'parameter {kwargs} beyond range')

        # todo 可选参数
