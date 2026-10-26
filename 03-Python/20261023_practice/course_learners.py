raw_learners = [
    {
        "name": "  阿哲",
        "hours_per_day": "1.5",
        "days_per_week": 4,
        "goal": "完成 Python 作品",
    },
    {
        "name": "小玲 ",
        "hours_per_day": "2",
        "days_per_week": 3,
        "goal": "  熟悉資料處理  ",
    },
    {
        "name": "小安",
        "hours_per_day": "1",
        "days_per_week": 2,
    },
]
#raw_learners：檔案櫃，裝了三份申請書
#[ ]：list，用編號排好，[0] 阿哲、[1] 小玲、[2] 小安
#{ }：每一份申請書是一個 dictionary
#小安少了 "goal" 這一欄

def clean_learner(raw):
    name = raw["name"].strip()

#整理一位學員，定義工作 clean_learner，收到一份申請書，叫它 raw
# 拿出姓名欄清掉前後空白，存進name
    
    goal = raw.get("goal", "").strip()
    if goal == "":
        goal = "未提供目標"
#拿出目標欄，沒有這欄就給空字串在清理空白
#若目標為空改成未提供目標

    hours_per_day = float(raw["hours_per_day"])
    days_per_week = int(raw["days_per_week"])
    weekly_hours = hours_per_day * days_per_week
#拿出每天時數，文字轉成小數
#拿出每週天數，轉成整數
#算出每週時數
    return {
        "name": name,
        "goal": goal,
        "hours_per_day": hours_per_day,
        "days_per_week": days_per_week,
        "weekly_hours": weekly_hours,
    }
#把整理好的資料裝進新的 dictionary 交回去。左邊有引號的是欄位名稱，右邊沒引號的是剛剛算好的變數

def clean_learners(raw_list):
    learners = []
    for raw in raw_list:
        learner = clean_learner(raw)
        learners.append(learner)
    return learners
#整理多位學員
#定義工作 clean_learners，收到整個檔案櫃，叫它 raw_list
#準備一個空的新檔案櫃，用來放整理好的資料
#從舊檔案櫃一份一份抽出來，每次抽到的叫 raw
#把這一份交給第二段的 clean_learner 整理，整理好的結果叫 learner
#把整理好的這份，放進新檔案櫃
learners = clean_learners(raw_learners)
#把原始檔案櫃交給 clean_learners，拿回整理好的新檔案櫃，存進 learners
for learner in learners:
    print(learner)
#從新檔案櫃一份一份拿出來，印出每一份
