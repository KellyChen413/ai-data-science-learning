# 請使用者輸入身高(cm)與體重(kg)，計算並印出 BMI 值與體位判斷  
print("BMI值計算")  
height = int(input("請輸入身高(cm): "))  
weight = int(input("請輸入體重(kg): "))  
height_m = height / 100
bmi = weight / (height_m * height_m)  
print("BMI值為: ", bmi)

if bmi < 18.5:  
    print("體位為：體重過輕")  
elif bmi < 23:  
    print("體位為：正常")  
elif bmi < 27:  
    print("體位為：體重過重")  
else:  
    print("體位為：肥胖")
