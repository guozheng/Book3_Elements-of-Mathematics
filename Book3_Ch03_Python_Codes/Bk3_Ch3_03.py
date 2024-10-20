###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch3_03

import numpy as np
import matplotlib.pyplot as plt
n_start = 6
n_stop  = 50
n_array = np.linspace(n_start,n_stop,n_stop-n_start + 1)

pi_lower_b = np.sin(np.pi/n_array)*n_array
pi_upper_b = np.tan(np.pi/n_array)*n_array

fig, ax = plt.subplots()

ax.axhline(y=np.pi, color='r', linestyle='-', label='Actual π')
ax.plot(n_array, pi_lower_b, color='b', label='Lower bound')
ax.plot(n_array, pi_upper_b, color='g', label='Upper bound')
ax.fill_between(n_array, pi_lower_b, pi_upper_b, color='#DEEAF6', alpha=0.5)

ax.set_xlabel('Number of sides, n')
ax.set_ylabel('Estimate of π')
ax.set_title('Estimation of π using polygon approximation')
ax.legend()

plt.tight_layout()
plt.show()
