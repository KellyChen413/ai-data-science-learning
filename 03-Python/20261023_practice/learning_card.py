"""
## 輸入
1. 姓名。
2. 本期最想完成的作品。
3. 每天學習幾小時。
4. 每週學習幾天。
5. 預計學習幾週。
## 輸出
1. 姓名。
2. 學習目標。
3. 每週預計學習時數。
4. 預計總學習時數。
5. 一句學習提醒。
## 要求
- 使用 `input()` 取得資料。
- 將每天學習時間轉成小數。
- 將每週學習天數與學習週數轉成整數。
- 計算每週與總學習時數。
- 使用 f-string 輸出結果。
- 變數使用 `snake_case`。
- 從終端機執行 `learning_card.py`。
"""
name=input("請輸入姓名:")
project=input("請輸入本期最想完成的作品:")
per_day_hours=float(input("請輸入每天學習小時數:"))
per_week_days=int(input("請輸入每週學習天數:"))
weeks_to_study=int(input("請輸入預計學習週數:"))
per_week_hours=float(input("請輸入每週學習小時數:"))
total_learning_hours=per_week_hours*per_week_days*weeks_to_study

print(f"姓名: {name}")
print(f"學習目標: {project}")
print(f"每週預計學習時數: {per_week_hours}")
print(f"預計總學習時數: {total_learning_hours}")
print("一句學習提醒: 堅持就是勝利")
