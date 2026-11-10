import pandas as pd
df = pd.DataFrame({
    "timestamp": [
        "2024-05-01 09:30",
        "2024-05-01 10:00",
        "2024-05-01 14:00",
        "2024-05-02 09:00",
        "2024-05-02 11:00"
    ],
    "person": ["Alice", "Bob", "Alice", "Alice", "Bob"],
    "event": ["login", "login", "logout", "login", "logout"]
})

#轉型
df["timestamp"] = pd.to_datetime(df["timestamp"])

print(df.groupby(["person"]).size())
print("---")
result = df["event"].value_counts()
print(result)
df["date"] = df["timestamp"].dt.date
print(df.groupby("date").size())
