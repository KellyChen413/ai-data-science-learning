number = input("輸入數字")
# 先檢查一次 我先印出number是什麼資料型態
#print(type("number"))
number_type = type("number")
while number.isdigit() == False:
    print(f"請輸入數字!,你剛輸入的是{number_type}")