'''
建立一個 3x4 的二維陣列
將每個元素賦予數值，如下圖
'''

rows = 3
cols = 4
matrix =[]
count = 0
for i in range(rows):          
    row = []                     
    for j in range(cols):        
        row.append(count)      
        count += 2               
    matrix.append(row)        
print(matrix)                  