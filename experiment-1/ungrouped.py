import pandas as pd
import numpy as np
l1=list(eval(input("enter dataset :- ")))
series=pd.Series(l1)

mean=series.mean()
print("mean: ",mean)

median=series.median()
print("median: ",median)

mode=series.mode()
print("mode: ",mode)