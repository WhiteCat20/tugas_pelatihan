#!/usr/bin/python

"""
Identitas:
Nama: Muhammad Faiz Rahmadani
Email: fzrahmadan@gmail.com
Penjelasan : berikut adalah program yang menunjukan grafik pada kelipatan angka dua, tiga dan empat. Program ini menggunakan numpy untuk meng-generate array, dan menggunakan pyplot dari matplotlib untuk menghasilkan grafik
"""

# import numpy dan matplotlib
import matplotlib.pyplot as plt
import numpy as np

# data dasar
i = np.arange(0, 100, 2)
j = np.arange(0, 100, 3)
k = np.arange(0, 100, 4)
print(i)
print(j)
print(k)

# plotting ke matplotlib
x1 = i
x2 = j
x3 = k
plt.figure()
plt.plot(x1, label="Kelipatan 2")
plt.plot(x2, label="Kelipatan 3")
plt.plot(x3, label="Kelipatan 4")
plt.title('Grafik Kelipatan 2, 3, dan 4')
plt.legend()
plt.show()

