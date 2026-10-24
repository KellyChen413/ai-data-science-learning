"""
#BMI=體重除以身高(公尺)的平方
標準分為過輕、健康、過重、肥胖
過輕:BMI<18.5
健康:18.5<=BMI<24
過重:24<=BMI<27
肥胖:BMI>=27
#請使用者輸入身高與體重,並計算出BMI值與體位判斷
#請輸出結果
"""
#input() 回傳的一定是字串（str），就算你輸入 164，Python 拿到的是文字 "164"，不是數字 164。
#修正方式：用 float() 把輸入轉成數字（身高、體重可能有小數，用 float 比 int 好）
print("BMI計算機")
height=float(input("請輸入你的身高(公分)"))
height_m=height/ 100
weight=float(input("請輸入你的體重(公斤)"))
BMI=(weight/(height_m*height_m))
print("BMI值為:",BMI)

if BMI<=18.5:
   print("體重過輕")
elif 18.5<=BMI<24:
   print("體重正常")
elif 24<=BMI:
   print("體重過重")
else:
    print("肥胖")
