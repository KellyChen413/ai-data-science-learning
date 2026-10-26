def clean_text(value): #定義一個工作，叫 clean_text，它會收到一個東西，暫時叫它 value
    return value.strip() #把 value 清掉空白，交回去

def recommend_plan(learning_hours_week, goal): #定義一個工作，叫做recommend_plan
  if learning_hours_week >= 6 and goal != "":
    return "密集方案" #傳回密集方案
  elif learning_hours_week >= 3:
    return "一般方案" #傳回一般方案
  else:
    return "建議先進行預備學習" #傳回建議先進行預備學習

name = clean_text(input("請輸入姓名:")) #清掉空白存進變數name
learning_hours_week = float(input("每週可學習時數(小時): ")) #轉成浮點數
goal = clean_text(input("請輸入學習目標(例如:Python): "))   #清掉空白存進變數goal
plan = recommend_plan(learning_hours_week, goal) #把 hours 和 goal 交給 recommend_plan 處理，它 return 回來的答案存進 plan。

print(f"{name}您好，目標{goal}，您的學習方案：{plan}")  #輸出結果
