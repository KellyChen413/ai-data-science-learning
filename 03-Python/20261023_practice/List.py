#串列初始化
course_names=[
    "Python",
    "FastAPI",
    "MySQL",
]
print(course_names[0]) #輸出串列的第一個元素
tmp=[] # 空的 list，之後再放東西進去

print(course_names[0])
print(course_names[2])  # 索引為 0~2，最後一個元素為索引 2

mystr="I Love Python" # 陣列是[]，字串是""
print(mystr[0]) #字串也可以用索引取得元素，輸出I

#透過 for 迴圈走訪串列
for course_name in course_names:  #從 course_names 裡一次拿一個出來，暫時叫它 course_name，然後印出來
    print(course_name)

courses = [          # list 裡包含 list，每一筆是一個 list，包含 [課程名稱, 時數]，就像一張表格
    ["Python", 4],
    ["Java", 6],
    ["LLM", 4],
    ["DB", 3]
]     
print(courses[0])  # 輸出第一筆 ["Python", 4]
print(courses[0][0]) #輸出第一筆的第一個元素 ["Python"]
print(courses[0][1]) #輸出第一筆的第二個元素 [4]
print(courses[1][1]) #輸出第二筆的第二個元素 [6]


newcourse ="AI Security"  #單一個字串
newcourses = ["PA","Cymulate"] #單一個 list
courses.append(newcourse) #新增一個 list 中的元素
print(courses) #輸出[["Python", 4], ["Java", 6], ["LLM", 4], ["DB", 3], "AI Security"]
courses.extend(newcourses) #新增多個 list 中的元素
print(courses) #輸出[["Python", 4], ["Java", 6], ["LLM", 4], ["DB", 3], "PA", "Cymulate"]
courses.extend(newcourse) #將單一個 list 中的元素拆開來新增
print(courses) #輸出['P', 'A', 'C', 'y', 'm', 'u', 'l', 'a', 't', 'e']
