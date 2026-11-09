import pandas as pd

df = pd.DataFrame({
    "ts": [1772413500, 1772413260, 1772413620, 1772413380],
    "person": ["worker_B", "worker_A", "worker_A", "worker_A"],
    "event": ["enter_zone", "enter_zone", "leave_zone", "no_helmet"],
    "value": [0.92, 0.95, 0.90, 0.88],
})
df["ts"] = pd.to_datetime(df["ts"])
print(df.dtypes)

df = df.sort_values("ts")
df["ts"] = pd.to_datetime(df["ts"])
df["delta"] = df["ts"].diff()
print(df)
print(df[(df["ts"] >= "2026-03-02 09:02") & (df["ts"] <= "2026-03-02 09:06")])
