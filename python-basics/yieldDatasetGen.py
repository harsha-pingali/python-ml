import numpy as np

np.random.seed(42)  # for reproducibility

rows = 100_000

temperature = np.random.uniform(15, 45, rows)
rainfall = np.random.uniform(0, 300, rows)
humidity = np.random.uniform(20, 95, rows)

dataset = np.column_stack((temperature, rainfall, humidity))

# Optional: save to CSV
np.savetxt(
    "weather_data.csv",
    dataset,
    delimiter=",",
    header="temperature,rainfall,humidity",
    comments=""
)

dataset
