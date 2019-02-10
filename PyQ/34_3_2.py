class TextCalc:
    @classmethod
    def class_method(cls, price):
        assert cls.__name__ == TextCalc.__name__
        return int(price * 0.08)

    @staticmethod
    def static_method(price):
        return int(price * 0.08)


print(TextCalc.class_method(1000))
print(TextCalc.static_method(1000))
