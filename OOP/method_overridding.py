class Father:
      def sleep(self):
            print("sleeps from 10:00 to 5:00 AM")
      def eat(self):
            print("eating")
class Son(Father):
      def sleep(self):
            super().sleep()
            print("sleeps from 2:00 AM to 10:00 AM")
      def eat(self):
            super().eat()
            print("i love to eat junk foods")

Ram = Son()
Ram.eat()
Ram.sleep()
