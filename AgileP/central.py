import copy
from .rule import Descriptor


class CheckedMeta(type):
    def __new__(cls, cls_name, cls_bases, cls_methods):
        for m_name, m_instance in cls_methods.items():
            if isinstance(m_instance, Descriptor):
                m_instance.name = m_name
        return type.__new__(cls, cls_name, cls_bases, cls_methods)


class Agp(metaclass=CheckedMeta):
    def __init__(self, *args, **kwargs):
        self._fields = [x for x in self.__dir__() if not x.startswith("_")]
        args = list(args)

        # 字段基本校验。校验传入和定义是否一致
        if len(args) + len(kwargs) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')

        # 参数全为字典
        if not args:
            args = [""] * len(self._fields)
            for _k, _v in kwargs.items():
                index = self._fields.index(_k)
                args[index] = _v
        else:
            for _k, _v in kwargs.items():
                index = self._fields.index(_k)
                args.insert(index, _v)

        # 动态为描述起赋值，调用对应 set 方法
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # 动态为描述起赋值（声明式）
        extra_args = list(kwargs.keys())
        for name in extra_args:
            setattr(self, name, kwargs.pop(name))

        # 字段基本校验
        if kwargs:
            raise TypeError(f'parameter {kwargs} beyond range')

        instance_dict = self.__dict__
        result = copy.deepcopy(instance_dict)
        for name in instance_dict:
            if name.startswith("_"):
                result.pop(name)
        self.values = result
