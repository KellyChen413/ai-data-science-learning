#請輸入考試分數
score=float(input("請輸入考試分數(0~100):"))
if score >=0 and score <=100:
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")
else:
    print("分數輸入錯誤，請重新輸入")
