"""
=========================================================
      PYTHON ARRAYS (LISTS) - FILE 2
      Searching and Counting Programs
=========================================================

Programs Included
6. Linear Search
7. Count Occurrences of an Element
8. Find Second Largest Element
9. Find Second Smallest Element
10. Remove Duplicate Elements

=========================================================
"""

# =========================================================
# Program 6 : Linear Search
# =========================================================
"""
Search an element in a list.

Sample Input
5
10 20 30 40 50
30

Sample Output
Element found at position 3
"""

print("\n========== Program 6 : Linear Search ==========")

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

key = int(input("Enter element to search: "))

found = False

for i in range(len(arr)):
    if arr[i] == key:
        print("Element found at position", i + 1)
        found = True
        break

if not found:
    print("Element not found")


# =========================================================
# Program 7 : Count Occurrences
# =========================================================
"""
Count how many times an element appears.

Sample Input
1 2 3 2 5 2
Search = 2

Output
3
"""

print("\n========== Program 7 : Count Occurrences ==========")

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

key = int(input("Enter element to count: "))

count = 0

for num in arr:
    if num == key:
        count += 1

print("Occurrences =", count)


# =========================================================
# Program 8 : Second Largest Element
# =========================================================
"""
Find the second largest element.

Sample Input
10 5 8 25 15

Output
15
"""

print("\n========== Program 8 : Second Largest ==========")

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

largest = second = float('-inf')

for num in arr:

    if num > largest:
        second = largest
        largest = num

    elif num > second and num != largest:
        second = num

if second == float('-inf'):
    print("Second largest element does not exist.")
else:
    print("Second Largest =", second)


# =========================================================
# Program 9 : Second Smallest Element
# =========================================================
"""
Find the second smallest element.

Sample Input
12 8 5 20 15

Output
8
"""

print("\n========== Program 9 : Second Smallest ==========")

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

smallest = second = float('inf')

for num in arr:

    if num < smallest:
        second = smallest
        smallest = num

    elif num < second and num != smallest:
        second = num

if second == float('inf'):
    print("Second smallest element does not exist.")
else:
    print("Second Smallest =", second)


# =========================================================
# Program 10 : Remove Duplicate Elements
# =========================================================
"""
Remove duplicate elements while maintaining order.

Sample Input
1 2 2 3 4 4 5

Output
1 2 3 4 5
"""

print("\n========== Program 10 : Remove Duplicates ==========")

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

unique = []

for num in arr:
    if num not in unique:
        unique.append(num)

print("Original List :", arr)
print("Without Duplicates :", unique)

print("\n========== End of File 2 ==========")
