import pandas as pd

events = [
    {"timestamp": "2026-03-02 09:05:00", "person": "worker_B", "event": "enter_zone", "value": 0.92},
    {"timestamp": "2026-03-02 09:01:00", "person": "worker_A", "event": "enter_zone", "value": 0.95},
    {"timestamp": "2026-03-02 09:03:00", "person": "worker_A", "event": "no_helmet", "value": 0.88},
]

df = pd.DataFrame(events)
df = df.sort_values("timestamp")

print("---")
print(df)
print("---")
print(df.iloc[0])
print("---")
print(df.loc[0])
