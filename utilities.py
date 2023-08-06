import timeit
import numpy as np

def benchmark_time(matrices, method):
    start_time = timeit.default_timer()
    for idx, (matrix1, matrix2) in enumerate(matrices, 1):
        method(matrix1, matrix2)
    end_time = timeit.default_timer()
    return round(end_time - start_time, 5)


def generate_random_matrix():
    return np.random.randint(1, 11, (3, 3))


def generate_random_matrix_pairs(num_pairs):
    matrix_pairs = []
    for _ in range(num_pairs):
        matrix_pair = (generate_random_matrix(), generate_random_matrix())
        matrix_pairs.append(matrix_pair)
    return matrix_pairs


def print_benchmark(benchmark_time, new_time, benchmark_description = 'Benchmark time', new_description = 'New time'):
    improvement_factor = round(benchmark_time / new_time, 2)
    print(benchmark_description + ':', benchmark_time)
    print(new_description + ':', new_time)
    print(new_description, 'was', improvement_factor, 'times faster than', benchmark_description)
