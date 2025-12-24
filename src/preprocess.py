import pandas as pd
import os

raw_file = "data/raw/MachineLearningRating_v3.txt"
processed_file = "data/processed/cleaned_data.csv"

# Ensure processed directory exists
os.makedirs(os.path.dirname(processed_file), exist_ok=True)

# Use chunksize for large file
chunksize = 100_000  # adjust according to your RAM

chunks = []

# Use default engine (C) and remove low_memory for compatibility
for chunk in pd.read_csv(raw_file, sep="|", chunksize=chunksize, engine='c'):
    chunks.append(chunk)

# Concatenate all chunks
data = pd.concat(chunks, ignore_index=True)

# Optional: save a sample for quick EDA
data_sample = data.sample(n=100_000, random_state=42)
data_sample.to_csv("data/processed/cleaned_data_sample.csv", index=False)

# Save full processed data (if your RAM allows)
data.to_csv(processed_file, index=False)

print(f"Processed data saved to {processed_file}")
print("Sample of 100k rows saved to data/processed/cleaned_data_sample.csv")
