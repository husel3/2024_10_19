'''### 3. **Palindrome Number Checker**

Write a function `is_palindrome_number` that checks if a number reads the same forwards and backward.

**Bonus:** Extend it to check a list of numbers and return all palindromic numbers.'''

numbers=input().split() #split is for putting input_numbers into list
print(f'Palindrome numbers: {[num for num in numbers if num==num[::-1]]}') #used comprehension: run every strings in list if True
#[::-1] reverse, start at the end of string and finish at position 0, -1 means going backwards