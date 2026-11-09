import pandas as pd
df = pd.DataFrame({
    "person": ["Alice", "Bob", "Alice", "Charlie"],
    "event": ["login", "login", "logout", "login"],
    "value": [1, 1, 0, 1]
})
print("1. 取出 event 欄位")
print(df["event"])
print("---")
print("2. 取出前兩筆資料")
print(df.head(2))
print("---")
print("3. 篩選 event == login")
print(df[df["event"] == "login"])
print("---")
print("4. 篩選 person == Alice")
print(df[df["person"] == "Alice"])