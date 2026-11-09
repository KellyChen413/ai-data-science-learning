import pandas as pd

data = [0.95, 0.88, 0.92, 0.90]

events = [
    {"timestamp": "2026-03-02 09:01:00", "person": "worker_A", "event": "enter_zone", "value": data[0]},
    {"timestamp": "2026-03-02 09:03:00", "person": "worker_A", "event": "no_helmet", "value": data[1]},
    {"timestamp": "2026-03-02 09:05:00", "person": "worker_B", "event": "enter_zone", "value": data[2]},
    {"timestamp": "2026-03-02 09:07:00", "person": "worker_A", "event": "leave_zone", "value": data[3]},
]

df = pd.DataFrame(events)
df = df.rename(columns={
    "person":"worker"
})
print(df)
