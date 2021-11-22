import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("https://raw.githubusercontent.com/swapnilsaurav/Dataset/master/hotel_bookings.csv")
print(df.head(10))

print(df.columns)

# Select numeric data form dataset
df_numeric = df.select_dtypes(include=[np.number])
numeric_columns = df_numeric.columns.values
print("Numeric columns are:\n ", numeric_columns)
print("Shape of ", df_numeric.shape)

# # Select Non-numeric data form dataset
# df_nonnumeric = df.select_dtypes(exclude=[np.number])
# nonnumeric_columns = df_numeric.columns.values
# print("Numeric columns are:\n ", nonnumeric_columns)
# print("Shape of ", df_nonnumeric.shape)

import seaborn as sns
sns.heatmap(df.isnull())
plt.show()

