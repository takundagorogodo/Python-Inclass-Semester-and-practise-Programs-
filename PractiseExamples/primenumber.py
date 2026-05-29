def prime_checker(number):
      isPrime = True
      for num in range(2,number):
            if number % num ==0:
                  isPrime = False
            
      if isPrime == True:
            print(f"{number} is a prime number")
      else:
            print(f"{number} is not a prime number")
            
number = int(input("enter a number : \n"))
prime_checker(number)