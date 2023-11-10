import numpy as np
import sys


def generate_file(num_count = 5000, filename = 'numbers'):
    numbers = np.random.randint(0, 2**32, num_count, dtype=np.dtype(np.uint32))
    res = "\n".join(list(map(lambda x: str(x), numbers)))
    with open(filename, 'w') as f:
        f.writelines(res)


if __name__ == '__main__':
    file_path = sys.argv[1] if len(sys.argv) > 1 else 'numbers'
    numbers_count = int(sys.argv[2]) if len(sys.argv) > 2 else 5000

    generate_file(numbers_count, file_path)
