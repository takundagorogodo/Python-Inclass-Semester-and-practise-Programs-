class Demo:
      #def add(self,a,b,c=0):
      #      return a+b+c
      #
      def add(self,*args):
            total = 0
            for i in args:
                  total += i
            return total
      
d = Demo()
print(d.add(2,3))
print(d.add(2,3,9))
print(d.add(29,33,8,9))