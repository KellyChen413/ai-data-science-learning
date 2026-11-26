import pandas as pd

df = pd.DataFrame({
    "timestamp": [
        "2026-03-02 08:55", "2026-03-02 09:12", "2026-03-02 09:40", "2026-03-02 10:03",
        "2026-03-02 10:40", "2026-03-02 11:15", "2026-03-03 08:50", "2026-03-03 09:20",
        "2026-03-03 09:45", "2026-03-03 10:30", "2026-03-03 11:05", "2026-03-03 14:10",
    ],
    "person": [
        "worker_B", "worker_A", "worker_C", "worker_A",
        None, "worker_B", "worker_A", "worker_C",
        "worker_A", "worker_B", None, "worker_C",
    ],
    "event": [
        "enter_zone", "no_helmet", "no_helmet", "no_helmet",
        "no_helmet", "enter_zone", "no_helmet", "leave_zone",
        "enter_zone", "no_helmet", "no_helmet", "no_helmet",
    ],
})
#步驟1_印出資料筆數與各欄型別
print("1. 原始資料:", len(df), "筆")
print(df.dtypes)
print("---\n")
#步驟2_印出各欄缺值數，刪掉有缺值的列，印出剩幾筆
print("2. 各欄缺值數:")
print(df.isna().sum())
df_clean = df.dropna()
print("刪除缺值後:", len(df_clean), "筆")
print("---\n")
#步驟3_篩出 no_helmet 的事件
print("3. 未戴安全帽事件:")
# 語法拆解：df_clean["event"] == "no_helmet" 會先逐列比對是否符合並標記 True/False，
# 外面的 df_clean[...] 再只保留 True 的列，最後存成 df_no_helmet 給下一步使用。
df_no_helmet = df_clean[df_clean["event"] == "no_helmet"]
print(df_no_helmet)
print("---\n")
#步驟4_依人統計未戴安全帽次數
print("4. 每人未戴安全帽次數:")
# 語法拆解：groupby("person") 會把相同人員的資料歸成同一組，
# 後面加上 .size() 則會統計每一組共有幾筆違規紀錄。
df_counts =df_no_helmet.groupby("person").size()
print(df_counts)
print("---\n")
#步驟5_整理成 list of dict，作為給 LLM 的摘要
print("5. 給LLM的摘要:")
# 語法拆解：reset_index(name="no_helmet_count") 先把索引轉回一般欄位並命名次數為 no_helmet_count，
# 再用 to_dict(orient="records") 讓每一列變成一個字典，放進串列中。
df_summary = df_counts.reset_index(name="no_helmet_count").to_dict(orient="records")
print(df_summary)