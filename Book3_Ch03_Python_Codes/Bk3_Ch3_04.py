###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch3_04

import numpy as np
import matplotlib.pyplot as plt

n_start = 6

B_6 = np.sin(np.pi/n_start)*n_start
A_6 = np.tan(np.pi/n_start)*n_start

B_array = []
A_array = []
n_array = np.array([6, 12, 24, 48, 96])  # Convert to numpy array here

B_i = B_6
A_i = A_6

for i in n_array:
    B_array.append(B_i)
    A_array.append(A_i)
    
    # updating
    A_i = 2 * A_i * B_i / (A_i + B_i)
    B_i = np.sqrt(A_i * B_i)

B_array = np.array(B_array)
A_array = np.array(A_array)

fig, ax = plt.subplots()

ax.axhline(y=np.pi, color='r', linestyle='-', label='π')
ax.plot(n_array, B_array, color='b', marker='x', label='B (inscribed)')
ax.plot(n_array, A_array, color='g', marker='x', label='A (circumscribed)')
ax.fill_between(n_array, B_array, A_array, color='#DEEAF6', alpha=0.5)

ax.set_xticks(n_array)
ax.set_xlim(6, 96)
ax.set_xlabel('Number of sides, n')
ax.set_ylabel('Estimate of π')
ax.legend()

plt.tight_layout()
plt.show()
