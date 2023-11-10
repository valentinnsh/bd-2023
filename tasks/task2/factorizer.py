import numpy as np
import sys
import time
import ray
import multiprocessing
from multiprocessing import Lock, Queue, Pool
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import mmap

lock = multiprocessing.Lock()
ray.init(num_cpus=8)


def factorize(num):
    div_list = []
    div = 2
    while div ** 2 <= num:
        if num % div == 0:
            div_list.append(div)
            num //= div
        else:
            div += 1
    if num > 1:
        div_list.append(num)
    return div_list


def factorize_numbers(numbers):
    return sum(len(factorize(x)) for x in numbers)


@ray.remote
def factorize_numbers_ray(numbers):
    return sum(len(factorize(x)) for x in numbers)


def mp_sum(filename, use_processes=False):
    start = time.time()
    split_array = get_splitted_array(filename)

    if use_processes:
        with ProcessPoolExecutor() as executor:
            results = executor.map(factorize_numbers, split_array)
    else:
        with ThreadPoolExecutor() as executor:
            results = executor.map(factorize_numbers, split_array)

    return sum(results), time.time() - start


def get_splitted_array(filename):
    num_list = []
    with open(filename, "r+b") as f:
        with mmap.mmap(f.fileno(), length=0, prot=mmap.PROT_READ) as map_file:
            for line in iter(map_file.readline, b""):
                num_list.append(int(line))
    split_array = np.array_split(np.array(num_list), 8)
    return split_array


def straightforward_sum(filename):
    start = time.time()
    with open(filename, 'r') as file:
        numbers = [int(line) for line in file.readlines()]

    return factorize_numbers(numbers), time.time() - start


def ray_sum(filename):
    start = time.time()
    split_array = get_splitted_array(filename)

    factors_counts = [factorize_numbers_ray.remote(subarray) for subarray in split_array]
    final_sum = sum(ray.get(factors_counts))

    return final_sum, time.time() - start


def numpy_sum(filename):
    start = time.time()
    data = np.memmap(filename, mode='r')
    return np.sum(np.array(factorize(x)).count for x in data), time.time() - start


if __name__ == '__main__':
    file_path = sys.argv[1] if len(sys.argv) > 1 else 'numbers'

    methods = [("Straightforward", straightforward_sum), ("Multithreading", mp_sum, False),
               ("Multiprocessing", mp_sum, True), ("Ray", ray_sum)]

    for method, *args in methods:
        result, ttime = args[0](file_path, *args[1:]) if len(args) > 1 else args[0](file_path)
        print("{} sum: {} time: {} seconds".format(method, result, ttime))

