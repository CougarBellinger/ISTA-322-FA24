import pandas as pd
import numpy as np

employee = pd.read_csv("https://docs.google.com/spreadsheets/d/1P09i7aisrfk3iexaZOuSdEA2uYDZlBb0r2ZvYjqjyG4/gviz/tq?tqx=out:csv")
# print(employee.head)

employee_supervisor = employee.merge(employee, left_on=['MANAGER_ID'], right_on=['EMPLOYEE_ID'])
print(employee_supervisor.head(2))

