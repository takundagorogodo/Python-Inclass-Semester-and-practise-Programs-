import os
result = 0
continue_Result = 0
end_Main_Program = False
while not end_Main_Program:
      first_Number =int(input("\nEnter first number : "))
      print(" + \n \n - \n \n * \n \n / \n ")
      operation =input("Pick an operation : ")
      second_Number = int(input("\nEnter next number : "))

      def CalcOperation(first,operator,second):
            if(operator == "+"):
                  return first + second
            elif operator == "-":
                  return first - second
            elif operator == "*":
                  return first * second
            elif operator == "/":
                  return first / second
            else:
                  return
            
      result = continue_Result + CalcOperation(first_Number,operation,second_Number)
      print(f"{continue_Result} + ({first_Number} {operation} {second_Number}) = {result}")

      continue_Result = result


      continue_Program = input(f"\nenter 'y' to continue calcuation with {result} or 'n' to start new calculation and 'x' to end program : ") 
      if continue_Program == 'y':
            end_Main_Program = False
      elif continue_Program =='n':
            result = 0
            continue_Result = result
            os.system('cls')

      elif continue_Program =='x':
            print("\n exiting prohgram !!!")
            end_Main_Program = True
