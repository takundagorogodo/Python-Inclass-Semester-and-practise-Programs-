
try:
      a = 5 / 1
      b = a + "10"
except ZeroDivisionError as e:
      print(e)

except TypeError as e:
      print(e)
else:
      print("everthing is fine")
finally:
      print("cleaning up")

class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        super().__init__(message)
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError("value is too high")
    if x < 5:
        raise ValueTooSmallError("value is too small", x)

try:
    test_value(-5)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e, e.value)
