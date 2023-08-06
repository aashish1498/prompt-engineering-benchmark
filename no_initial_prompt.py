def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def nearest_prime(num):
    lower_prime = num
    upper_prime = num
    while True:
        lower_prime -= 1
        upper_prime += 1
        if is_prime(lower_prime):
            return lower_prime
        if is_prime(upper_prime):
            return upper_prime

def matrix_multiplication(matrix1, matrix2):
    result_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
    return result_matrix

def sum_of_elements(matrix):
    return sum(sum(row) for row in matrix)


def matrix_prime_no_initial_prompt(matrix1, matrix2):
    # Matrix multiplication
    result_matrix = matrix_multiplication(matrix1, matrix2)

    # Calculate sum of elements in the resulting matrix
    matrix_sum = sum_of_elements(result_matrix)

    # Find the nearest prime number to the sum
    nearest_prime_num = nearest_prime(matrix_sum)

    print("Resultant matrix:")
    for row in result_matrix:
        print(*row)

    return matrix_sum, nearest_prime_num


def matrix_prime_no_initial_prompt_no_print(matrix1, matrix2):
    # Matrix multiplication
    result_matrix = matrix_multiplication(matrix1, matrix2)

    # Calculate sum of elements in the resulting matrix
    matrix_sum = sum_of_elements(result_matrix)

    # Find the nearest prime number to the sum
    nearest_prime_num = nearest_prime(matrix_sum)

    return matrix_sum, nearest_prime_num


def main():
    # Taking input for two 3x3 matrices
    matrix1 = []
    matrix2 = []

    print("Enter the elements of the first 3x3 matrix:")
    for _ in range(3):
        row = list(map(int, input().split()))
        matrix1.append(row)

    print("Enter the elements of the second 3x3 matrix:")
    for _ in range(3):
        row = list(map(int, input().split()))
        matrix2.append(row)

    # Matrix multiplication
    result_matrix = matrix_multiplication(matrix1, matrix2)

    # Calculate sum of elements in the resulting matrix
    matrix_sum = sum_of_elements(result_matrix)

    # Find the nearest prime number to the sum
    nearest_prime_num = nearest_prime(matrix_sum)

    print("Resultant matrix:")
    for row in result_matrix:
        print(*row)

    print("Sum of elements in the resultant matrix:", matrix_sum)
    print("Nearest prime number to the sum:", nearest_prime_num)

if __name__ == "__main__":
    main()
