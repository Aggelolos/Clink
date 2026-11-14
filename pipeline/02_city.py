# Step 2: keep only Philadelphia restaurants and bars, and only their reviews.
# Why: the review file is 5.3 GB. One city is small enough to work with.
import pandas as pd
from pathlib import Path

RAW = Path("data/raw")
OUT = Path("data/processed")
OUT.mkdir(parents=True, exist_ok=True)

# 1. Pick the places: Philadelphia, PA, and a food or drink category.
biz = pd.read_json(RAW / "yelp_academic_dataset_business.json", lines=True)
cats = biz["categories"].fillna("")
mask = (
    (biz["city"] == "Philadelphia")
    & (biz["state"] == "PA")
    & cats.str.contains("Restaurants|Bars|Nightlife")
)
biz = biz[mask]
biz.to_json(OUT / "business_city.jsonl", orient="records", lines=True)
print(len(biz), "places in Philadelphia")

# 2. Read the review file in chunks and keep only reviews of those places.
ids = set(biz["business_id"])
total = 0
with open(OUT / "reviews_city.jsonl", "w", encoding="utf-8") as f:
    chunks = pd.read_json(
        RAW / "yelp_academic_dataset_review.json", lines=True, chunksize=200_000
    )
    for chunk in chunks:
        keep = chunk[chunk["business_id"].isin(ids)]
        if len(keep):
            text = keep.to_json(orient="records", lines=True, force_ascii=False)
            f.write(text.rstrip("\n") + "\n")
            total += len(keep)
        print("kept so far:", total, flush=True)
print(total, "reviews kept")

# 3. Quick look: how many reviews does each place have?
rev = pd.read_json(OUT / "reviews_city.jsonl", lines=True)
print(rev.groupby("business_id").size().describe())
