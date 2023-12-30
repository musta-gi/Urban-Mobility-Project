import pandas as pd
import numpy as np

def array_to_csv(array, filename):
    dataframe = pd.DataFrame(array)
    dataframe.to_csv(filename, index=False, header=False)
    return "Done"