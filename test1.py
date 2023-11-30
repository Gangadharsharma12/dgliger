import pandas as pd
pq = "C:/Users/DammannagariGangadha/Desktop/output/vlr.parquet"
pq1 = pd.read_parquet(pq, engine="auto")
print(pq1)