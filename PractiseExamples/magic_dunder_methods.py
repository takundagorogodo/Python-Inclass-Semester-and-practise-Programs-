print(dir(int))
class Author:
      def __init__(self,name,book_name,pages):
            self.name = name
            self.book_name = book_name
            self.pages = pages
      
      def __len__(self):
            return self.pages
            
      def __call__(self, *args, **kwds):
            print("hi dunder method called")
      
      def __del__(self):
            print("Author object has been deleted")

      def __str__(self):
            return f"{self.book_name} by {self.name}"
d = Author("takunda","mpho's search",79)
print(d)
print(str(d))
print(len(d))
d()
del d
#print(d)