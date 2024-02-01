import pandas as pd
import numpy as np
import rpy2.robjects as ro
from rpy2.robjects import pandas2ri

pandas2ri.activate()
ro.r['load']('allgre.PB_V2.RData')
r_dataframe = ro.r['allgre.PB_V2']
# Convert the R DataFrame into a Pandas DataFrame
df = pandas2ri.ri2py(r_dataframe)

# Now 'df' is a Pandas DataFrame
print(df.head())
