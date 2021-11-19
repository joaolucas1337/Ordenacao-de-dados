#!/usr/bin/env python
import pandas as pd
import numpy as np
import time


start = time.time()

df = pd.read_csv('metadados_fotos_APS_20212.csv')

df["a"]=''
first_column = df.pop("a")
df.insert(0, "a", first_column)

np_array = df.to_numpy()
np_array = list(np_array)

base = []


for a in np_array:
    base.append(list(a))

def InsertSort(array, linha = 4):
  for i in range(1, len(array)):
    aux = array[i]
    j = i-1
    while j >= 0 and aux[linha] < array[j][linha]:
      array[j + 1] = array[j]
      j -= 1
    array[j + 1] = aux
  return array

a = InsertSort(base)

for b in a:
    print(b)

end = time.time()

print(end - start)