import functools
def start_end_decorator( func):
      @functools.wraps(func)
      def wrapper(*args, **kwargs):
            print("start")
            result = func(*args,**kwargs)
            print("end")
            return result
      return wrapper

@start_end_decorator
def add(x):
      return x + 5
result = add(10)
print(help(add))
print(add.__name__)
print(result)
