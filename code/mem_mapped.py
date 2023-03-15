import mmap
import os

import numpy as np


def intro():
    f_name = 'file.txt'
    
    with open(f_name, 'r+b') as f:
        with mmap.mmap(f.fileno(), length=0, offset=0, access=mmap.ACCESS_WRITE) as mm:
            print(mm[:5])
            mm[:1] = b'B'


def simple():
    # имя файла для отображения
    f_name = 'file_for_memmap.txt'
    try:    
        # заполняем его строками       
        with open(f_name, 'w', encoding='utf-8') as f:
            f.write('\n'.join(['Hello World'] * 1000))

        # отображаем файл на память
        with open(f_name, 'r+b') as f:
            with mmap.mmap(f.fileno(), length=1000, offset=0, access=mmap.ACCESS_WRITE) as mm:
                print(mm[:20])
                mm[:5] = b'12345'

        # проверяем изменения
        with open(f_name, 'r', encoding='utf-8') as f:
            print(f.readline())
    finally:
        #Удалям файл
        os.remove(f_name)


def numpy_mapping():
    # имя файла для отображения
    f_name = 'file_for_memmap.txt'
    try:    
        # записываем туда бинарное представление массива numpy      
        with open(f_name, 'wb') as f:
            arr = np.arange(0, 100, dtype=np.int64)            
            f.write(arr.data)
            
        # отображаем файл на память
        with open(f_name, 'r+b') as f:
            with mmap.mmap(f.fileno(), length=100*8, offset=0, access=mmap.ACCESS_WRITE) as mm:
               # восстанавливаем массив
               arr = np.frombuffer(mm, dtype=np.int64)
               print(arr)  
    finally:
        #Удалям файл
        os.remove(f_name)

if __name__ == '__main__':
    intro()
    simple()
    numpy_mapping()
