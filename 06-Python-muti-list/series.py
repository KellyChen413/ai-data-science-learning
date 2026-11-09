import pandas as pd

counts = pd.Series([0, 2, 1])

print("三天的事件數")
print(counts)
print("那些天有事件")
print(counts > 0)
print("只留下有事件的天")
print(counts[counts > 1])

