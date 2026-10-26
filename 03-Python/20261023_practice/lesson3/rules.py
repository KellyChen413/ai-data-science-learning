def clean_text(value):
    return value.strip()


def recommend_plan(hours, goal):
    if hours >= 6 and goal != "":
        return "密集方案"
    elif hours >= 3:
        return "一般方案"
    else:
        return "建議先進行預備學習"
def is_exit_command(name): #判斷輸入是否為q
    return name.lower() == "q" #轉成小寫再判斷
