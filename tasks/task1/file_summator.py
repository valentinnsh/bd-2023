import sys
import time
import os
import threading
from multiprocessing import Process, Manager, Pool
import mmap

import numpy as np

global sum_result, min_result, max_result
lock = threading.Lock()


def straightforward_bin_read(filename):
    start_time = time.time()
    num_sum = 0
    min_value = float('inf')
    max_value = float('-inf')

    with open(filename, 'rb') as f:
        while True:
            int32_bytes = f.read(4)

            if not int32_bytes:
                break

            number = np.frombuffer(int32_bytes, dtype=np.uint32)[0]
            num_sum += number
            min_value = min(min_value, number)
            max_value = max(max_value, number)

    return num_sum, min_value, max_value, time.time() - start_time


def process_chunk(chunk_data):
    return sum(chunk_data), min(chunk_data), max(chunk_data)


# Split file into chunks and process them in parallel
# Calc length and offset parameters for each chunk based on chunk size
def get_mmap_params(file, max_threads):
    file_size = os.stat(file.name).st_size
    chunk_size = file_size // max_threads

    return (({'fileno': file.fileno(), 'length': min(file_size - i * chunk_size, chunk_size),
              'offset': i * chunk_size, 'access': mmap.ACCESS_READ}) for i in range(max_threads))


# targets are very similar for threads and processes
# But they use different locks objects
# and different ways to store results - global variables for threads and shared dict for processes,
# because processes can't share memory the same way threads do
def get_target(mmap_params, res=None, p_lock=None):
    global sum_result, min_result, max_result

    with mmap.mmap(**mmap_params) as mm:
        num_sum = 0
        local_min_value = float('inf')
        local_max_value = float('-inf')
        while True:
            int32_bytes = mm.read(4)

            if not int32_bytes:
                break

            number = np.frombuffer(int32_bytes, dtype=np.uint32)[0]
            num_sum += number
            local_min_value = min(local_min_value, number)
            local_max_value = max(local_max_value, number)

    if res is None:
        with lock:
            sum_result += num_sum
            min_result = min(local_min_value, min_result)
            max_result = max(local_max_value, max_result)
    else:
        with p_lock:
            res['sum'] = res.get('sum', 0) + num_sum
            res['min'] = min(local_min_value, res.get('min', 2 ** 32 + 1))
            res['max'] = max(local_max_value, res.get('max', -1))


# Read file using mmap and threads
# Here and in the next case num_threads was set to 8 by default empirically
def mmap_threads_read(filename, num_threads = 8):
    global sum_result, min_result, max_result
    sum_result = 0
    min_result = float('inf')
    max_result = -1
    start_time = time.time()
    threads = []
    with open(filename, 'rb') as f:
        for mmap_params in get_mmap_params(f, num_threads):
            thread = threading.Thread(target=get_target, args=[mmap_params])
            threads.append(thread)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

    return sum_result, min_result, max_result, time.time() - start_time


# Read file using mmap and processes
# Approach to shared memory is different here
# At first wanted to use Pool.map, but thought that it's not the point of the task
def mmap_process_read(filename, num_processes=8):
    global sum_result, min_result, max_result
    start_time = time.time()
    result = Manager().dict()
    p_lock = Manager().Lock()
    processes = []
    with open(filename, 'rb') as f:
        for mmap_params in get_mmap_params(f, num_processes):
            thread = Process(target=get_target, args=(mmap_params, result, p_lock))
            processes.append(thread)

        for process in processes:
            process.start()

        for process in processes:
            process.join()

    return result['sum'], result['min'], result['max'], time.time() - start_time


# Added to compare with my custom methods as an etalon. It's unsurprisingly the fastest approach
def mmap_numpy_read(filename):
    start_time = time.time()
    data = np.memmap(filename, dtype=np.uint32, mode='r')
    return data.sum(), data.min(initial=-1), data.max(initial=2 ** 32 + 1), time.time() - start_time


if __name__ == '__main__':
    filepath = sys.argv[1] if len(sys.argv) > 1 else 'numbers'

    approaches = [
        ('Straightforward Bin', straightforward_bin_read),
        ('MMAP files + threads', mmap_threads_read),
        ('MMAP files + processes', mmap_process_read),
        ('numpy.memmap', mmap_numpy_read)
    ]

    for approach_name, approach_func in approaches:
        bin_summ, min_value, max_value, elapsed_time = approach_func(filepath)
        print(f'{approach_name} on {filepath}: {bin_summ}, min value: {min_value}, max value: {max_value}, time: {elapsed_time}')
