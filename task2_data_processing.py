import pandas as  pd
import json 
import os
file_path = "data/trends_20260411.json"
with open(file_path, "r", encoding ="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)
print(f"Loaded {len(df)} stories from {file_path}")

df = df.drop_duplicates(subset="post_id")
print(f"After removing duplicates: {len(df)}")

df = df.dropna(subset=["post_id", "title", "score"])
print(f"After removing nulls: {len(df)}")

df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)
df = df[df["score"] >= 5]
print(f"After removing low scores: {len(df)}")

df["title"] = df["title"].str.strip()

os.makedirs("data", exist_ok=True)
output_path = "data/trends_clean.csv"
df.to_csv(output_path, index=False)

print(f"Saved {len(df)} rows to {output_path}")

print("\nStories per category:")
print(df["category"].value_counts())