from pandas.core.arrays.arrow import dtype
import pandas as pd

df = pd.DataFrame({
    "ts": [1772413500, 1772413260, 1772413620, 1772413380],
    "person": ["worker_B", "worker_A", "worker_A", "worker_A"],
    "event": ["enter_zone", "enter_zone", "leave_zone", "no_helmet"],
    "value": [0.92, 0.95, 0.90, 0.88],
})


print(dtype(df["ts"]))