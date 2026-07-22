"""
=========================================================
            PYTHON ARRAYS (LISTS) - FILE 1
                  Programs 1 - 5
=========================================================

Topic: Basics of Arrays (Lists)

Programs Included:
1. Read and Print a List
2. Sum of All Elements
3. Find the Largest Element
4. Find the Smallest Element
5. Calculate the Average of Elements

=========================================================
"""

# =========================================================
# Program 1: Read and Print a List
# =========================================================
"""
Problem:
Read N elements from the user and print the list.

Sample Input:
Enter number of elements: 5
Enter element 1: 10
Enter element 2: 20
Enter element 3: 30
Enter element 4: 40
Enter element 5: 50

Sample Output:
List = [10, 20, 30, 40, 50]
"""

print("\n========== Program 1 ==========")

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    value = int(input(f"Enter element {i+1}: "))
    arr.append(value)

print("List =", arr)


# =========================================================
# Program 2: Sum of All Elements
# =========================================================
"""
Problem:
Find the sum of all elements in a list.

Sample Input:
List = [10,20,30,40]

Sample Output:
Sum = 100
"""

print("\n========== Program 2 ==========")

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input("Enter element: ")))

total = 0

for num in arr:
    total += num

print("Sum =", total)


# =========================================================
# Program 3: Find the Largest Element
# =========================================================
"""
Problem:
Find the largest element in a list.

Sample Input:
[4,8,2,9,5]

Sample Output:
Largest = 9
"""

print("\n========== Program 3 ==========")

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input("Enter element: ")))

largest = arr[0]

for num in arr:
    if num > largest:
        largest = num

print("Largest element =", largest)


# =========================================================
# Program 4: Find the Smallest Element
# =========================================================
"""
Problem:
Find the smallest element in a list.

Sample Input:
[8,3,5,1,9]

Sample Output:
Smallest = 1
"""

print("\n========== Program 4 ==========")

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input("Enter element: ")))

smallest = arr[0]

for num in arr:
    if num < smallest:
        smallest = num

print("Smallest element =", smallest)


# =========================================================
# Program 5: Calculate the Average
# =========================================================
"""
Problem:
Calculate the average of all elements in a list.

Sample Input:
[10,20,30,40]

Sample Output:
Average = 25.0
"""

print("\n========== Program 5 ==========")

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input("Enter element: ")))

total = 0

for num in arr:
    total += num

average = total / n

print("Average =", average)


print("\n==============================")
print("End of Arrays File 1")
print("==============================")