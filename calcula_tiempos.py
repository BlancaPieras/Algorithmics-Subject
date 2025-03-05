import copy
import random
import time
from Selection_sort import selectionSort
from Bubble_sort import bubbleSort
from Insertion_sort import insertionSort
from Merge_sort import mergeSort
from Merge3_sort import merge3Sort
from Quick_sort import quickSort
from Quick_sort import quickSort_posiciones
from Quick_sort import quickSort_aleatorio
from Heap_sort import heapSort


def check_sorted(algorithm, original, ordenada):
    for i in range(0, len(ordenada) - 1):
        if ordenada[i] > ordenada[i + 1]:
            print(algorithm.__name__)
            print(original)
            print(ordenada)
            raise "Error, lista no ordenada"


# realiza la medicion de algorithm (método de ordenación)
# pasándole una copia de nums
def measure_algorithm(algorithm, nums):
    nums_copy = copy.copy(nums)
    start_time = time.time_ns()
    algorithm(nums_copy)
    total_time = time.time_ns() - start_time
    check_sorted(algorithm, nums, nums_copy)
    return (total_time / 10 ** 9)


num_samples = 30  # numero de muestras
num_elements = 10000  # numero de elementos de la lista


def pythonSort(l):
    l.sort()


# algoritmos a evaluar
algorithms = [bubbleSort, selectionSort, insertionSort, mergeSort, merge3Sort, quickSort, quickSort_posiciones,
              quickSort_aleatorio, heapSort, pythonSort]
tiempos = [0] * len(algorithms)

for n in range(0, num_samples):
    print("Calculando sample =", n)
    # generamos una lista de enteros
    nums = [random.randint(-num_elements * 3, num_elements * 3) for i in range(num_elements)]
    for algorithm, i in zip(algorithms, range(0, len(algorithms))):
        # obtenemos el tiempo y lo sumamos a su tiempo acumulado
        tiempos[i] = measure_algorithm(algorithm, nums) / num_samples

# mostramos los resultados
print("Num Samples =", num_samples)
print("Num Elements =", num_elements)
for algorithm, t in zip(algorithms, tiempos):
    print(algorithm.__name__, ":", t)

"""
Ejemplo de Ejecución
Num Samples = 30
Num Elements = 10000
bubbleSort : 0.42915241000000004
selectionSort : 0.18453469
insertionSort : 0.20162079666666666
mergeSort : 0.0019794366666666665
merge3Sort : 0.00168594
quickSort : 0.0012269566666666667
quickSort_posiciones : 0.0015756766666666668
quickSort_aleatorio : 0.0022632333333333335
heapSort : 0.00788566
pythonSort : 6.846e-05

"""
