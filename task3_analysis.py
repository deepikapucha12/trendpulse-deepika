import pandas as pd
import numpy as np
import os

file_path = "data/trends_clean.csv"

df = pd.read_csv(file_path)

print(f"Loaded data: {df.shape}")
print("\nFirst 5 rows:")
print(df.head())

avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()
print(f"\nAverage score: {avg_comments}")
print(f"Average comments: {avg_comments}")

scores = df["score"].values
print("\nNumpy States:")
print(f"Mean score: {np.mean(scores)}")
print(f"Median score: {np.median(scores)}")
print(f"Std deviation: {np.std(scores)}")
print(f"Max score: {np.max(scores)}")
print(f"Min score: {np.min(scores)}")

top_category = df["category"].value_counts().idxmax()
top_count = df["category"].value_counts().max()

print(f"\nMost stories in: {top_category}({top_count} stories)")

top_story = df.loc[df["num_comments"].idxmax()]
print(f"Most commented story: '{top_story['title']}' - {top_story['num_comments']} comments")

df["engagement"] = df["num_comments"] / (df["score"] + 1)
df["is_popular"] = df["score"] > avg_score

os.makedirs("data", exist_ok=True)
output_path = "data/trend_analysised.csv"

df.to_csv(output_path, index=False)
print(f"\Saved to {output_path}")
                
                                        