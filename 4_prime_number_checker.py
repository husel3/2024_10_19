'''### 4. **Prime Number Checker**

Write a function `is_prime` that takes a number and returns `True` 
if it’s a prime number and `False` otherwise. A prime number 
is a number greater than 1 that has no divisors other than 1 and itself.

**Bonus:** Modify the function to return all prime numbers up to the given number.'''

def is_prime():
     get_number=int(input())
     for i in range(2, get_number): #goes through all numbers
          if get_number%i==0:
               return print('thats not a prime number')
     print('thats a prime number')
is_prime()


