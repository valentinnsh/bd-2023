import numpy as np
import sys


def write_binfile(file_path, gb):
    file_size = gb * 2 ** 30
    number_array = np.random.randint(0, 2 ** 32 - 1, size=int(file_size / 4), dtype=np.uint32)
    number_array.tofile(file_path)


def write_short_binfile(file_path, gb):
    file_size = gb * 2 ** 20
    number_array = np.random.randint(0, 2 ** 32 - 1, size=int(file_size / 4), dtype=np.uint32)
    number_array.tofile(file_path)


if __name__ == '__main__':
    file = sys.argv[1] if len(sys.argv) > 1 else 'numbers'
    file_size_gb = int(sys.argv[2]) if len(sys.argv) > 2 else 2

    # for quick testing purposes
    if file == 'test':
        write_short_binfile(file, file_size_gb)
    else:
        write_binfile(file, file_size_gb)
