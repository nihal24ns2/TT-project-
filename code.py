import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Simulate creating a dummy aqi_data.csv DataFrame if it doesn't exist
# This ensures the rest of the code can run for demonstration purposes
if 'df' not in locals(): # Check if df is already defined
    # Generate dummy data for 'Date' and 'AQI'
    dates = pd.date_range(start='2022-01-01', periods=100, freq='D')
    aqi_values = np.random.randint(50, 200, size=100)
    df = pd.DataFrame({'Date': dates, 'AQI': aqi_values})
    print("Created dummy 'aqi_data.csv' DataFrame.")

# 2. Convert Date column to datetime and set as index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# 3. Resample the data to get the monthly average AQI
monthly_aqi = df['AQI'].resample('M').mean()

# 4. Plot the trend over time
plt.figure(figsize=(14, 6))
sns.lineplot(data=monthly_aqi, color='crimson', linewidth=2)
plt.title('Average Monthly AQI Trend Over Time', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average AQI', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.fill_between(monthly_aqi.index, monthly_aqi.values, color='crimson', alpha=0.1)
plt.show()