import pandas as pd
import numpy as np

rides = pd.read_csv("https://docs.google.com/spreadsheets/d/1tHArxAroG14mKf-AHjdvYsXhaXI5nE08bUUW4UDHCRw/gviz/tq?tqx=out:csv")
rides_copy = rides.copy
# print(rides_copy)

newr = rides
# print(newr.head)

newr = newr.reset_index()
# print(newr.head)

newr.loc['2018-01-01 3:00:00']





