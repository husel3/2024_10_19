'''### 25. **Remove Duplicates from a List**

Write a function `remove_duplicates` that takes a list and removes all duplicate values.

**Bonus:** Preserve the original order of the elements.'''

def remove_dublicates():
     #split() makes list
     #create dictionary using list as keys, dict has no dublicates and ordered
     print(list(dict.fromkeys(input().split()))) 
remove_dublicates()