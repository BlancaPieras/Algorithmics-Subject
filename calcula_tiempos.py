import copy
import random
import time
from Selection_sort import selectionSort
from Bubble_sort import bubbleSort
from Insertion_sort import insertionSort
from Merge_sort import mergeSort
from Merge3_sort import merge3Sort
from Quick_sort import quickSort

# realiza la medicion de algorithm (método de ordenación)
# pasándole una copia de nums
def measure_algorithm(algorithm, nums):
    nums_copy = copy.copy(nums)
    start_time = time.time_ns()
    algorithm(nums_copy)
    total_time = time.time_ns() - start_time
    return (total_time / 10 ** 9)


num_samples = 30  # numero de muestras
num_elements = 10000  # numero de elementos de la lista

def pythonSort(l):
    l.sort()

# algoritmos a evaluar
algorithms = [bubbleSort, selectionSort, insertionSort, mergeSort, merge3Sort, quickSort, pythonSort]
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
bubbleSort : 0.392868
selectionSort : 0.17272289333333332
insertionSort : 0.18218730666666666
mergeSort : 0.00179975
merge3Sort : 0.0016998966666666665
quickSort : 0.0011014966666666667
pythonSort : 3.3220000000000004e-05
"""
