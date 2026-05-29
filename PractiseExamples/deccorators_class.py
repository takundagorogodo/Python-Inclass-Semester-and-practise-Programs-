class CountCalls:

      def __init__(self,func):
            self.func = func
            self.num_calls = 0

      def __call__(self, *args, **kwargs):
            self.num_calls += 1 
            print(f'this is executed {self.num_calls} times ')
            return self.func(*args ,**kwargs)


@CountCalls
def sayhello():
      print('hello')

sayhello()
sayhello()