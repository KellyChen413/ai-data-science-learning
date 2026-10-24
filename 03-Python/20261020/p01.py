from profiling.sampling import heatmap_collector
from profiling.sampling import heatmap_collector
hours_per_day = 2
days = 5
total_hours = hours_per_day * days

print(total_hours)
A = 10
a = 20
#print(中文變數名稱會出錯) #註解
# 單行註解
# 多行註解 三個引號 1個 3個都可以
"""
多行註解1
多行註解2
"""
# Ctrl+l for Antigravity terminal
# 無行尾結束符號
if a>10:
    print("a大於10")
else:
    print("a小於10")
#縮排很重要，縮排數量沒有限制，但同一個層級都要一樣
print("這是新增的一行")
#定位點如何設置？ 

mystr = "中文字"
mystr2 = '中文字'
mystr3 = "A = 10"
mystr4 = 'A = 10'
mystr5 = 'A = {10}'
mystr6 = "A = {10}"
mystr7 = f"A = {A}"
mystr8 = f'A = {A}'
mystr9 = f'A = {A * 20}'

my_money = 1000000

print(f"{my_money:,}")     # 印出 1,000,000
print(f"{my_money:.2f}")   # 印出 1000000.00
print(f"{my_money:,.2f}")  # 印出 1,000,000.00


print(mystr)
print(mystr2)
print(mystr3)
print(mystr4)
print(mystr5)
print(mystr6)
print(mystr7)
print(mystr8)
print(mystr9)
#在程式碼世界中運算只會有小括號，沒有大括號與花括號
#python中運算符由高到低
#小括號 > 指數 > 乘除 > 加減
print(100/3)  #一般除法
print(111//3) #這是整除
print(111%3)  #這是除餘數
print(2*6/3+1-1)
print((80+70+80)/3)
