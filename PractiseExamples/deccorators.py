def start_end_decorator( func):

      def wrapper():
            print("start")
            func()
            print("end")
      return wrapper

#def print_name():
#      print('Alex')
#
#print_name = start_end_decorator(print_name)
@start_end_decorator
def print_name():
      print('Alex')
print_name()
