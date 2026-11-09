'''
請建立一個 4x4 的二維陣列，每個元素為一個字典，格式如下：
{"name": "stu-0", "score": 60}
name 為學生名稱，例如 stu-0。
score 為第一次段考成績。
請模擬第二次段考成績：
使用者需手動輸入每位學生的新分數。
計算每位學生的成績變化量（delta）：
delta 的公式為：
delta = 第二次成績 - 第一次成績
將結果輸出為 4x4 的二維陣列，元素格式如下：
{"name": "stu-0", "score": 60, "delta": -10}
'''

# 1. 建立 4x4 的二維陣列
# 每個元素為一個字典，包含學生名稱與第一次段考成績（預設 60 分）
rows, cols = 4, 4
students = []
count = 0

for i in range(rows):
    row = []
    for j in range(cols):
        student = {
            "name": f"stu-{count}",
            "score": 60
        }
        row.append(student)
        count += 1
    students.append(row)

# 顯示初始 4x4 陣列
print("=== 第一次段考初始資料 (4x4) ===")
for row in students:
    print(row)
print()

# 2. 模擬第二次段考成績：使用者手動輸入每位學生的新分數，並計算 delta
print("=== 請手動輸入第二次段考成績 ===")
for row in students:
    for student in row:
        while True:
            user_input = input(f"請輸入 {student['name']} 的第二次段考成績 (第一次為 {student['score']}): ").strip()
            try:
                second_score = int(user_input)
                break
            except ValueError:
                print("輸入格式錯誤，請輸入整數分數！")
        
        # 計算 delta = 第二次成績 - 第一次成績
        delta = second_score - student["score"]
        
        # 將 delta 加入字典中
        student["delta"] = delta

# 3. 將結果輸出為 4x4 的二維陣列
print("\n=== 成績變化量計算結果 (4x4 二維陣列) ===")
for row in students:
    print(row)

