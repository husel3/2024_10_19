'''### 11. **Pyramid of Numbers**

Write a program that generates a pyramid of numbers based on user input. For example, if the user inputs `4`, the program outputs:
```
   1
  121
 12321
1234321
```

**Bonus:** Allow the user to specify whether the pyramid should be left-aligned, right-aligned, or centered.'''

n = int(input("number: "))
choice = int(input('''1. Left-aligned 
2. Right-aligned 
3. Centered
Choose 1, 2, or 3: '''))

#to make n lines
for i in range(1, n + 1):
    space = ' ' * (n - i)  
    #use str cz if it's int, output will be like the sum
    #our expected output is "1"+"2"+"3" = 123, not 1+2+3=6
    increase = ""
    for j in range(1, i + 1):
        increase += str(j)

    decrease = ""
    for j in range(i - 1, 0, -1):
        decrease += str(j)

    #logic of space in right aligned pyramid is little different
    #it is similar with logic of space but in each line it is added by 2
    right_aligned_space=' ' * (2 * (n - i))

    if choice == 1:  # Left-aligned
        print(increase + decrease)
    elif choice == 2:  # Right-aligned
        print(right_aligned_space + increase + decrease)
    else:  # Centered
        print(space + increase + decrease)