import pandas as pd
import numpy as np

def array_to_csv(array, filename):
    df = pd.DataFrame(array)
    df.to_csv(filename, index=False, header=False)