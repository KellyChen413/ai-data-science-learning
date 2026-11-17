#基礎
#1. 變數與資料型態
# 字串
name = "kelly"
# 整數
age = 24
# 浮點數
height = 175.5
# 布林
is_student = True
print (name,age)

# 2.輸出與輸入
name = input("請輸入姓名:")
print("您好"+ name)
 #3.運算與字串
price = 120
count = 20
total = price * count
print(f"總共{total}")
# 判斷式if/elif/else
# 輸入分數判斷及格
score = int(input("請輸入分數:"))
if score >= 60:
    print("及格")
else:
    print("不及格")
# 5.迴圈for/while
# 印出1到100的偶數
for n in range (2,101,2):
    print(n)
# 從5倒數到1
count = 5
while count > 0:
    print(count)
    count = count -1
# 6.函式def/return
  