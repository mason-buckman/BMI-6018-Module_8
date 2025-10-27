import numpy as np
import pandas as pd

#1. Import NumPy as np and print the version number.
print("\nProblem 1: NumPy version =", np.__version__)

#2. Create a 1D array of numbers from 0 to 9 and print it.
problem2_array= np.arange(10)
print("\nProblem 2: 1D array from 0 to 9 =", problem2_array)

#3. Import a dataset with numbers and texts keeping the text intact in python numpy. Use the iris dataset.
iris_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
iris_data = np.genfromtxt(iris_url, delimiter=',', dtype=None, encoding='utf-8') #utf-8 encoding should keep text intact
print("\nProblem 3: Iris dataset =", iris_data)


#4. Find the position of the first occurrence of a value greater than 1.0 in petalwidth 4th column of the iris dataset.
petalwidth = iris_data['f3']
positions_of_interest = np.where(petalwidth > 1.0) # Where function returns the indices of elements where a condition is satisfied
first_occurrence = positions_of_interest[0][0]
print("\nProblem 4: Position of first occurrence of pedalwidth > 1.0 in 4th column =", first_occurrence)

#5. From the array 'a', replace all values greater than 30 with 30, and all values less than 10 with 10.
np.random.seed(100)
a = np.random.uniform(1, 50, 20)
print("\n(For reference) Original Array a =", a)

for i in range(len(a)):
    if a[i] > 30:
        a[i] = 30
    elif a[i] < 10:
        a[i] = 10

print("\nProblem 5: Modified Array a =", a)