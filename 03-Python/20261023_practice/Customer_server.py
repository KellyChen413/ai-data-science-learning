"""
設計一個系統選單
=====客服系統====
1.呼叫客服
2.文字聯繫
3.留下資料
4.離開系統
================
輸入1-4選擇功能,或輸入Q離開系統
"""

while True:
    print("=====客服系統=====")
    print("1.呼叫客服")
    print("2.文字聯繫")
    print("3.留下資料")
    print("4.離開系統")
    print("================")
    user_input = input("請輸入選擇項目 1-4 或 Q離開系統:")

    if user_input == "1":
        print("您選擇了呼叫客服")
    elif user_input == "2":
        print("您選擇了文字聯繫")
    elif user_input == "3":
        print("您選擇了留下資料")
    elif user_input == "4" or user_input.upper() == "Q":
        print("感謝您的使用,再見!")
        break
    else:
        print("輸入錯誤,請重新選擇")