'''### 4. **Prime Number Checker**

Write a function `is_prime` that takes a number and returns `True` 
if it’s a prime number and `False` otherwise. A prime number 
is a number greater than 1 that has no divisors other than 1 and itself.

**Bonus:** Modify the function to return all prime numbers up to the given number.'''

#check all 'not prime' numbers, and if it's false, it prints 'prime'
def is_prime() :
     get_number = int(input())
     for i in range(2, get_number): #goes through all numbers
          if get_number % i == 0: #if given_number is divisible by numbers other than 1 and itself, it's not a prime num
               return print('thats not a prime number') #return mmakes the function stop after a print
                                                        #if break used, it'll continue and print both 'not a prime' and 'a prime'
     print('thats a prime number')
is_prime()


def is_prime() :
     get_number = int(input()) 
     all_primes = [] #create empty list, cause there can be more than one prime number
     for all_numbers in range(2, get_number): #to check all numbers until get_number
          is_prime = 0 #I can use True instead of equalizing with 0
          for j in range(2, all_numbers): #to check all_numbers if they're divisible by numbers other than 1 and itself, they're not prime nums
               if all_numbers % j == 0: #if it's divisible, is_prime becomes 1 and doesn't go to next 'if' condition
                    is_prime += 1
                    break 
          if is_prime == 0: #the rest all_numbers goes here and added to list
               all_primes.append(all_numbers)
     print(all_primes)

is_prime()


