import numpy as np
import math as m

print("PART I\n")

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


print(f"1. There are {a[a<0].size} negative numbers, they are {a[a<0]}")

print(f"2. There are {a[a>0].size} positive numbers, they are {a[a>0]}")

only_evens = a[a%2==0]
only_pos = only_evens[only_evens > 0]
a[a%2==0]
print(f"3. There are {only_pos.size} positive even numbers, they are {only_pos}")

#can also use .size in place of len()
a_plus_three = a + 3
print(f"4. When 3 is added to each number there are {a_plus_three[a_plus_three > 0].size} positive numbers, they are {a[(a+3) > 0]}")

new_a = a**2
new_mean = new_a.mean()
new_std = new_a.std()
print(f"5. When each value is squared the mean is {new_mean} (old {a.mean()}) and the standard deviaton {new_std} (old {a.std()})")

mean_a = a.mean()
centered_a = a-mean_a
print(f"6. When the data is centered is is {centered_a}")

std_a = a.std()
print(f"7. The z scores for the data are {(a-mean_a)/std_a}")


print("\nPART II  a.k.a. question 8\n")
print("II.a")
## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = sum(a)
print(f"1. sum_of_a = {sum_of_a}")

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = min(a)
print(f"2. min_of_a = {min_of_a}")

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a)
print(f"3. max_of_a = {max_of_a}")

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = sum_of_a/len(a)
print(f"4. mean_of_a={mean_of_a}")

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
product_of_a = 1
for num in a:
    product_of_a *= num
print(f"5. product_of_a = {product_of_a}")

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = [x**2 for x in a]
print(f"6. squares_of_a = {squares_of_a}")

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = [x for x in a if x%2]
print(f"7. odds_in_a = {odds_in_a}")

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = [x for x in a if not x%2]
print(f"8. evens_in_a = {evens_in_a}\n")


## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

# these are going to be slower than the numpy versions for two reasons:
# they are not in C, and they require two for loops (depending on how 
# the built-in functions are coded). These will also not work
# for higher dimensions
def sum_matrix(matrix):
    ##returns the sum of a list of lists of numerics
    return sum([sum(r) for r in matrix])

def max_matrix(matrix):
    ##returns the max of a list of lists of numerics
    return max([max(r) for r in matrix])

def min_matrix(matrix):
    return min([min(r) for r in matrix])

def mean_matrix(matrix):
    sum_of_elem = sum([sum(r) for r in matrix])
    num_of_elem = sum([len(r) for r in matrix])
    return sum_of_elem/num_of_elem

def prod_matrix(matrix):
    #not sure how to do this one, but it would be two for loops
    pass

#print(f"{sum_matrix(b)}\n{max_matrix(b)}\n{min_matrix(b)}\n{mean_matrix(b)}")

print("Part II.b")
# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. 
# **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)
np_b = np.array(b)
print(f"1. sum_of_b = {np_b.sum()}")

# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  
print(f"2. min_of_b = {np_b.min()}")

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
print(f"3. max_of_b = {np_b.max()}")


# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
print(f"4. mean_of_b = {np_b.mean()}")

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number
print(f"5. product_of_b = {np_b.prod()}")

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)
print(f"6. squares_of_b = {np_b**2}")

# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)
print(f"7. odds_of_b = {np_b[np_b%2 != 0]}")


# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)
print(f"8. evens_of_b = {np_b[np_b%2 == 0]}")

# Exercise 9 - print out the shape of the array b.
print(f"9. shape_of_b = {np_b.shape}")

# Exercise 10 - transpose the array b.
print(f"10. b_transposed = {np_b.transpose()}\nalt is:\n {np_b.T}")

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
print(f"11. b_as_1x6 = {np_b.reshape(1,6)}")

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
print(f"12. b_as_6x1 = {np_b.reshape(6,1)}")


print(f"\nPART II.c")
## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
np_c = np.array(c)

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
print(f"1. c_min = {np_c.min()}\n\tc_max = {np_c.max()}\n\tc_sum = {np_c.sum()}\n\tc_prod = {np_c.prod()}")

# Exercise 2 - Determine the standard deviation of c.
print(f"2. c_std = {np_c.std()}")

# Exercise 3 - Determine the variance of c.
print(f"3. c_variance = {np_c.var()}")

# Exercise 4 - Print out the shape of the array c
print(f"4. c_array shape = {np_c.shape}")

# Exercise 5 - Transpose c and print out transposed result.
print(f"5. c_transposed = {np_c.transpose()}")

# Exercise 6 - Get the dot product of the array c with c. 
print(f"6. c_dot_c = {np_c.dot(np_c)}")
print(f"alt method = {np.dot(np_c, np_c)}")
print(f"alt method 2 = {np.matmul(np_c, np_c)}")

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
c_transposed = np_c.transpose()
c_prod = np_c*c_transposed
c_sum = c_prod.sum()
print(f"7. sum_of_prod_c_transposed = {c_sum}")

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
print(f"8. c times c_transposed  = {np.prod(np_c*np_c.T)}")


print("PART II.d\n")
## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]
np_d = np.array(d)

# Exercise 1 - Find the sine of all the numbers in d
print(f"1. sin(d) = {np.sin(np_d)}")

# Exercise 2 - Find the cosine of all the numbers in d
print(f"2. cos(d)={np.cos(np_d)}")

# Exercise 3 - Find the tangent of all the numbers in d
print(f"3. tan(d) = {np.tan(np_d)}")

# Exercise 4 - Find all the negative numbers in d
print(f"4. neg(d) = {np_d[np_d < 0]}")

# Exercise 5 - Find all the positive numbers in d
print(f"5. pos(d) = {np_d[np_d > 0]}")

# Exercise 6 - Return an array of only the unique numbers in d.
print(f"6. unique(d) = {np.unique(np_d)}")

# Exercise 7 - Determine how many unique numbers there are in d.
print(f"7. number of unique items in d = {np.unique(np_d).size}")

# Exercise 8 - Print out the shape of d.
print(f"8. shape of d = {np_d.shape}")

# Exercise 9 - Transpose and then print out the shape of d.
print(f"9. transposed shape of d = {np_d.transpose().shape}")

# Exercise 10 - Reshape d into an array of order 9 x 2
print(f"10. Reshape d into 9 x 2: {np_d.reshape(9,2)}")