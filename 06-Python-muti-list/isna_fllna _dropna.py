import pandas as pd

df = pd.DataFrame({
    "person": ["Alice", "Bob", "Charlie", "Alice"],
    "event": ["login", "login", "login", "logout"],
    "value": [1, 1, None, None]
})
# 缺值檢查
print(df.isna())
#補值
df["value"] = df["value"].fillna(3)
print(df)
