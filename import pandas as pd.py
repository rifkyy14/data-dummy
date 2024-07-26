import pandas as pd
import numpy as np

n_rows = 100
n_cols = 5
arr = np.random.randint(10, 110, size = (n_rows, n_cols))
arr

pd.DataFrame(arr, columns=('ABCDE'))
