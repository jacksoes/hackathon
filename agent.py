import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

import dspy

 

# Step 1: Create random data

np.random.seed(42)

df = pd.DataFrame({

    'Day': np.arange(1, 11),

    'Temperature': np.random.randint(60, 100, size=10),

    'Humidity': np.random.randint(30, 80, size=10)

})

 

# Save to CSV

csv_filename = "random_weather.csv"

df.to_csv(csv_filename, index=False)

 

# Step 2: Load the CSV

data = pd.read_csv(csv_filename)

print("CSV Data:\n", data)

 

# Step 3: Plot and save as JPEG

plt.figure(figsize=(8, 5))

plt.plot(data['Day'], data['Temperature'], marker='o', label='Temperature')

plt.plot(data['Day'], data['Humidity'], marker='x', label='Humidity')

plt.xlabel("Day")

plt.ylabel("Value")

plt.title("Temperature and Humidity Over 10 Days")

plt.legend()

plt.grid(True)

 

# Save as JPEG

jpeg_filename = "weather_plot.jpg"

plt.savefig(jpeg_filename, format='jpg')

plt.close()

 

print(f"\n✅ Graph saved as '{jpeg_filename}'")