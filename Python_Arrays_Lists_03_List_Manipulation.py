"""
=========================================================
      PYTHON ARRAYS (LISTS) - FILE 3
      List Manipulation Programs
=========================================================

Programs Included
11. Reverse a List
12. Sort List in Ascending Order
13. Sort List in Descending Order
14. Merge Two Lists
15. Split List into Even and Odd

=========================================================
"""

# =========================================================
# Program 11 : Reverse a List
# =========================================================
"""
Reverse the elements of a list.

Sample Input
1 2 3 4 5

Output
5 4 3 2 1
"""

print("\n========== Program 11 : Reverse List ==========")

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

reverse = []

for i in range(n - 1, -1, -1):
    reverse.append(arr[i])

print("Original List =", arr)
print("Reversed List =", reverse)


# =========================================================
# Program 12 : Sort List in Ascending Order
# =========================================================
"""
Sort the elements of a list in ascending order using
Bubble Sort.

Sample Input
5 3 1 4 2

Output
1 2 3 4 5
"""

print("\n========== Program 12 : Ascending Order ==========")

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

for i in range(n - 1):
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted List =", arr)


# =========================================================
# Program 13 : Sort List in Descending Order
# =========================================================
"""
Sort the elements of a list in descending order using
Bubble Sort.

Sample Input
5 3 1 4 2

Output
5 4 3 2 1
"""

print("\n========== Program 13 : Descending Order ==========")

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

for i in range(n - 1):
    for j in range(n - 1 - i):
        if arr[j] < arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted List =", arr)


# =========================================================
# Program 14 : Merge Two Lists
# =========================================================
"""
Merge two lists into a single list.

Sample Input

List 1
1 2 3

List 2
4 5 6

Output
1 2 3 4 5 6
"""

print("\n========== Program 14 : Merge Two Lists ==========")

n1 = int(input("Enter number of elements in first list: "))

list1 = []

for i in range(n1):
    list1.append(int(input(f"Enter element {i+1}: ")))

n2 = int(input("\nEnter number of elements in second list: "))

list2 = []

for i in range(n2):
    list2.append(int(input(f"Enter element {i+1}: ")))

merged = []

for num in list1:
    merged.append(num)

for num in list2:
    merged.append(num)

print("Merged List =", merged)


# =========================================================
# Program 15 : Split List into Even and Odd
# =========================================================
"""
Separate even and odd elements into two different lists.

Sample Input
1 2 3 4 5 6

Output

Even List
2 4 6

Odd List
1 3 5
"""

print("\n========== Program 15 : Split Even and Odd ==========")

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

even = []
odd = []

for num in arr:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even List =", even)
print("Odd List =", odd)

print("\n========== End of File 3 ==========")

"""
=========================================================
      PYTHON ARRAYS (LISTS) - FILE 4
      Array Rotation Programs
=========================================================

Programs Included
16. Rotate Left by One Position
17. Rotate Right by One Position
18. Find Common Elements in Two Lists
19. Find Missing Number in a Sequence
20. Move All Zeros to the End

=========================================================
"""

# =========================================================
# Program 16 : Rotate Left by One Position
# =========================================================
"""
Rotate the elements of a list one position to the left.

Sample Input
1 2 3 4 5

Output
2 3 4 5 1
"""

print("\n========== Program 16 : Rotate Left ==========")

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

first = arr[0]

for i in range(n - 1):
    arr[i] = arr[i + 1]

arr[n - 1] = first

print("List after left rotation =", arr)


# =========================================================
# Program 17 : Rotate Right by One Position
# =========================================================
"""
Rotate the elements of a list one position to the right.

Sample Input
1 2 3 4 5

Output
5 1 2 3 4
"""

print("\n========== Program 17 : Rotate Right ==========")

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

last = arr[n - 1]

for i in range(n - 1, 0, -1):
    arr[i] = arr[i - 1]

arr[0] = last

print("List after right rotation =", arr)


# =========================================================
# Program 18 : Find Common Elements in Two Lists
# =========================================================
"""
Find common elements between two lists.

Sample Input

List 1
1 2 3 4 5

List 2
3 4 5 6 7

Output
3 4 5
"""

print("\n========== Program 18 : Common Elements ==========")

n1 = int(input("Enter number of elements in first list: "))

list1 = []

for i in range(n1):
    list1.append(int(input(f"Enter element {i+1}: ")))

n2 = int(input("\nEnter number of elements in second list: "))

list2 = []

for i in range(n2):
    list2.append(int(input(f"Enter element {i+1}: ")))

common = []

for num in list1:
    if num in list2 and num not in common:
        common.append(num)

print("Common Elements =", common)


# =========================================================
# Program 19 : Find Missing Number in a Sequence
# =========================================================
"""
Find the missing number from 1 to N.

Sample Input

5
1 2 4 5

Output
3
"""

print("\n========== Program 19 : Missing Number ==========")

n = int(input("Enter value of N: "))

arr = []

print("Enter", n - 1, "elements:")

for i in range(n - 1):
    arr.append(int(input()))

expected_sum = n * (n + 1) // 2

actual_sum = 0

for num in arr:
    actual_sum += num

missing = expected_sum - actual_sum

print("Missing Number =", missing)


# =========================================================
# Program 20 : Move All Zeros to the End
# =========================================================
"""
Move all zeros in the list to the end while maintaining
the order of non-zero elements.

Sample Input

0 2 0 5 8 0 7

Output

2 5 8 7 0 0 0
"""

print("\n========== Program 20 : Move Zeros ==========")

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

result = []

for num in arr:
    if num != 0:
        result.append(num)

zero_count = n - len(result)

for i in range(zero_count):
    result.append(0)

print("Updated List =", result)


print("\n========== End of File 4 ==========")
