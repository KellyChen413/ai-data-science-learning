import pandas as pd

df1 = pd.DataFrame({
    "camera": ["cam_A", "cam_A"],
    "event": ["person_detected", "no_helmet"]
})

df2 = pd.DataFrame({
    "camera": ["cam_B", "cam_B", "cam_B"],
    "event": ["person_detected", "person_detected", "no_helmet"]
})

#合併
result = pd.concat([df1, df2])
print(result)

#重新編號
result = pd.concat([df1, df2], ignore_index=True)
print(result)
print("---")
#合併後事件總數
print(f"\n總事件數: {result['event'].count()}")
#每台攝影機各有幾筆事件
print(result.groupby("camera").size())