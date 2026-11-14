import pandas as pd
from pathlib import Path

RAW = Path("data/raw")

biz = pd.read_json(RAW / "yelp_academic_dataset_business.json", lines=True)
print(len(biz), "businesses in total")

cats = biz["categories"].fillna("")
biz = biz[cats.str.contains("Restaurants|Bars|Nightlife")]

print(biz.groupby(["city", "state"]).size().sort_values(ascending=False).head(10))