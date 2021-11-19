
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

def SelectionSort(array, linha = 4):
  for j in range(len(array) - 1):
    min_index = j
    for i in range(j, len(array)):
      for d in range(j, len(array)):
        range(j, len(array))
      if array[i][linha] < array[min_index][linha]:
        min_index = i
    if array[j][linha] > array[min_index][linha]:
      aux = array[j]
      array[j] = array[min_index]
      array[min_index] = aux
  return array

a = SelectionSort(base)

for b in a:
    print(b)

end = time.time()

print(end - start)