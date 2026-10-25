for i in range(1,5):
    print(i)

for i in range(10,0,-1):
    print(i)

for i in range(1,10):
    print(i*i)

count = 0

while count < 3:
    print(count)
    count += 1

name = "  小明  "
clean_name = name.strip()
print(name)        # "  小明  "（原本的沒變）
print(clean_name)  # "小明"

command = " Q "
clean_command = command.strip().lower()
print(clean_command)   # "q"