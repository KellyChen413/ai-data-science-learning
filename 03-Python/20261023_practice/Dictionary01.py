learner = {            #冒號左邊叫 key（鍵）：資料的名稱
                        #冒號右邊叫 value（值）：實際放的資料
    "name": "小明",     #key:value，一個key只能對應一個value
    "hours_per_week": 8,   #value也可以是數字
    "goal": "學會 Python",
    "courses": ["Python", "AI agent"],
    "newcourses":[["LLM", 4],["DB", 3]]
}

print(learner["name"]) #輸出name這個key的值，也就是小明
print(learner["courses"]) #輸出courses這個key的值，value 可以是 List
print(learner["courses"][0]) #先拿 List，再用編號，learner["courses"] → ["Python", "AI agent"] 再取 [0] → "Python"
#value 是二維 List
print(learner['newcourses'][0][0]) #先拿 List，再用編號，learner['newcourses'] → [["LLM", 4],["DB", 3]] 再取 [0] → ["LLM", 4] 再取 [0] → "LLM"
#value 是 Dictionary
print(learner['time_management']['deadline']) #先拿 Dictionary，再用key，learner['time_management'] → {"deadline": "Week 5", "preferred_hours": ["Mon", "Wed", "Fri"]} 再取 ["deadline"] → "Week 5"
print(learner['newcourses'][1][1])  #先拿 List，再用編號，learner['newcourses'] → [["LLM", 4],["DB", 3]] 再取 [1] → ["DB", 3] 再取 [1] → 3


learners = [
{
        "name": "小明",
        "hours_per_day": "8",
        "goal": "學會 Python",
        "courses": ["Python", "AI agent"],
        "newcourses": [["LLM", 4], ["DB", 3]]
        
},
{
        "name": "小華",
        "hours_per_day": "8",
        "goal": "學會 Python",
        "courses": ["Python", "AI agent"],
        "newcourses": [["LLM", 4], ["DB", 3]]
}
]
print(learners[0]["name"]) #List 的第一個人，learners[0] → 第 0 位學員的整張資料表 →["name": "小明", ...]
print(learners[1]["name"]) #List 的第二個人，learners[1] → 第 1 位學員的整張資料表 →["name": "小華", ...]
print(learners[0]['newcourses'][0][0]) #List 的第一個人的 List 中的第一個，learners[0]['newcourses'] → [["LLM", 4], ["DB", 3]] → ["LLM", 4] → "LLM"