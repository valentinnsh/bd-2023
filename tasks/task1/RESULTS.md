# Резельтаты задания 1

Straightforward Bin on numbers sum: 1152941456387294955, min value: 3, max value: 4294967237, time: 345.5031201839447s
MMAP files + threads on numbers sum: 1152941456387294955, min value: 3, max value: 4294967237, time: 353.88285279273987s
MMAP files + processes on numbers sum: 1152941456387294955, min value: 3, max value: 4294967237, time: 59.241475343704224s
numpy.memmap on numbers sum: 1152941456387294955, min value: 3, max value: 4294967237, time: 0.5555229187011719s

Такое плохое время для тредов вызывает конечно большие вопросы. Либо проблема в моей реализации, либо такой подход не очень хорошо подходит для задачи. Возможно что-то связанное с 
глобальной блокировкой интерпритатора (https://habr.com/ru/companies/wunderfund/articles/586360/)? Не успел разобраться 
