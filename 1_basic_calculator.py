'''### 1. **Basic Calculator**

Write a program that asks the user to input two numbers and an arithmetic operation (`+`, `-`, `*`, `/`)
and then performs that operation on the numbers. Handle cases where division by zero may occur.
**Bonus:** Add support for more operations, such as exponentiation (`**`) and modulu me know
if you’d like more advanced tasks or additional hints for any of these assignments!'''


while True:
     operation = input('''CHOOSE AN OPERATOR:
                    "+", "-", "*", "/", 
                    "remainder=%", 
                    "exponentiation=**", 
                    "floor division=//",
                    "factorial=!"
                    ''')
     if operation == '!':
          fac = int(input('number: '))
          for i in range(1, fac+1):
               i *= fac
          print(i)
          break
     elif operation in ["+", "-", "*", "/", "**", "//"]:
          first_number = float(input('1st number: '))
          second_number = float(input('2st number: '))
          if operation == "+":
               print(first_number + second_number)
               break
          elif operation == "-":
               print(first_number - second_number)
               break
          elif operation == "*":
               print(first_number * second_number)
               break
          elif operation == "/":
               print(first_number / second_number)
               break
          elif operation == "**":
               print(first_number ** second_number)
               break
          elif operation == "//":
               print(first_number // second_number)
               break
     else:
          print('That operator is invalid, try again!')