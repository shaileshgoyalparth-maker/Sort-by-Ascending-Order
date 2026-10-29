import numpy as np
data_type = [("name", "S15"), ("class", int), ("height", float)]
students_details = [("James", 5, 67.9), ("Mohan", 7, 67.2), ("Paul", 8, 98.7), ("Sam", 6, 88.75)]
students = np.array(students_details, dtype = data_type)
print("Original Array: ")
print(students)
print("Sort by height: ")
print(np.sort(students, order="height"))