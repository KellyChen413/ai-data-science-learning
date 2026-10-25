for i in range (0,10):
    for j in range (0,10):
        print(f"{i+1} * {j+1} = {(i+1)*(j+1)}")

#同數字列一行
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i}*{j}={i*j}", end="\t")
    print()
# 分3欄
for i in range(1, 10, 3):
    for j in range(1, 10):
        print(f"{i}*{j}={i*j}", end="\t")
        print(f"{i+1}*{j}={(i+1)*j}", end="\t")
        print(f"{i+2}*{j}={(i+2)*j}")
    print()