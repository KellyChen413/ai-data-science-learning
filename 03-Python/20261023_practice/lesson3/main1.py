from rules import clean_text, recommend_plan, is_exit_command #匯入rules檔案的clean_text和recommend_plan這兩個函式
def main():
  while True:
    name = clean_text(input("請輸入姓名:")) #
    if is_exit_command(name):
        break
    learning_hours_week = float(input("每週可學習時數(小時): ")) 
    goal = clean_text(input("請輸入學習目標(例如:Python): ")) 

    plan = recommend_plan(learning_hours_week, goal)

    print(f"{name}您好,目標{goal},您的學習方案:{plan}")

  print("課程報名檢查結束!")

if __name__ == "__main__": #如果這個檔案是被直接執行的，才啟動 main()
  main()
