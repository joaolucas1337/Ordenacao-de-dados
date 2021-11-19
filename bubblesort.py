
import pandas as pd
import numpy as np
import time


start = time.time()

df = pd.read_csv('1k.csv')

df["a"]=''
first_column = df.pop("a")
df.insert(0, "a", first_column)

np_array = df.to_numpy()
np_array = list(np_array)

base = []


for a in np_array:
    base.append(list(a))


def BubbleSort(array, linha = 4):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1):
            e01 = array[j][linha]
            e02 = array[j + 1][linha]
            aux = array[j]

            if e01 > e02:
                array[j] = array[j + 1]
                array[j + 1] = aux

    return array

a = BubbleSort(base)

for b in a:
    print(b)

end = time.time()

tempo = (end - start)
print(tempo)