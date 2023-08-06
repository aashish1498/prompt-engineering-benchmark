import numpy as np

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_nearest_prime(number):
    lower_prime = number - 1
    upper_prime = number + 1
    while True:
        if is_prime(lower_prime):
            return lower_prime
        elif is_prime(upper_prime):
            return upper_prime
        lower_prime -= 1
        upper_prime += 1

def matrix_multiplication_sum(matrix1, matrix2):
    matrix1 = np.array(matrix1)
    matrix2 = np.array(matrix2)

    if matrix1.shape != (3, 3) or matrix2.shape != (3, 3):
        raise ValueError("Input matrices must be 3x3")

    result_matrix = np.matmul(matrix1, matrix2)
    sum_of_elements = np.sum(result_matrix)

    return sum_of_elements, find_nearest_prime(sum_of_elements)

# Example usage:
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

sum_of_elements, nearest_prime = matrix_multiplication_sum(matrix1, matrix2)
print("Matrix multiplication sum:", sum_of_elements)
print("Nearest prime number:", nearest_prime)
