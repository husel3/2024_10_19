'''### 3. **Palindrome Number Checker**

Write a function `is_palindrome_number` that checks if a number reads the same forwards and backward.

**Bonus:** Extend it to check a list of numbers and return all palindromic numbers.'''

numbers=input().split()
print(f'Palindrome number: {[int(num) for num in numbers if num==num[::-1]]}')