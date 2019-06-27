# Base class. Uses a descriptor to set a value
class Descriptor:
    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Typed(Descriptor):
    """
    类型校验
    """
    expected_type = type(None)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"{value} The correct format is a {str(self.expected_type)}")
        super().__set__(instance, value)


class Unsigned(Descriptor):
    """
    值必须大于 0
    """
    __slots__ = ["required", "max", "min"]

    def __init__(self, name=None, **opts):
        pass
        super().__init__(name, **opts)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Value must be greater than 0')
        super().__set__(instance, value)


class MaxSized(Descriptor):
    _required = ["size"]
    _optional = ["required"]

    def check_required_field(self):
        if sorted(self.opts.keys()) != sorted(MaxSized._required):
            raise TypeError(f'Must contain {MaxSized._required} fields')

    def __init__(self, name=None, **opts):
        self.opts = opts
        self.check_required_field()
        super().__init__(name, **opts)

    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError('size must be < ' + str(self.size))
        super().__set__(instance, value)
