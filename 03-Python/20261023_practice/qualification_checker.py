while True:
    name = input("請輸入姓名:").strip()
    if name.lower() == "q":    # 如果姓名轉成小寫後是q就跳出迴圈
        break

    learning_hours_week = float(input("每週可學習時數(小時): "))
    goal = input("請輸入學習目標(例如:Python): ").strip()

    if learning_hours_week >= 6 and goal != "":    # goal != "" 意思是學習目標不是空白
        plan = "密集方案"
    elif learning_hours_week >= 3:
        plan = "一般方案"
    else:
        plan = "建議先進行預備學習"

    print(f"{name}您好,目標{goal},您的學習方案:{plan}")

print("課程報名檢查結束")