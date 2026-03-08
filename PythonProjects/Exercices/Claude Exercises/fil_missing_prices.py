import pandas as pd
import numpy as np

# Create a DataFrame with missing values
data = {'price': [100, 150, np.nan, 200, np.nan, 180, 120]}
df = pd.DataFrame(data)

# Print the DataFrame before filling missing values
print("Before filling missing values:")
print(df)

# Fill missing values with the median
median_price = df['price'].median()
df['price'] = df['price'].fillna(median_price)


# Print the DataFrame after filling missing values
print("\nAfter filling missing values:")
print(df)