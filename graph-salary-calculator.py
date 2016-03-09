__author__ = 'Dario Hermida'

import test_main as test
import numpy as np
import matplotlib.pyplot as plt

min_salary = 40000
max_salary = 76000
step = 500
difference_salary = []

normal_salary, ruling_salary = test.testing_main(min_salary, max_salary, step)
for index in range(0, len(normal_salary)):
    difference_salary.append(ruling_salary[index] - normal_salary[index])

X_axis = np.linspace(min_salary, max_salary, (max_salary - min_salary)/step)
plt.plot(X_axis, normal_salary, color='blue', label='normal')
plt.plot(X_axis, ruling_salary, color='red', label='ruling')
plt.plot(X_axis, difference_salary, color='green', label='difference')


plt.show()
