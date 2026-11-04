#原始資料
raw_expenses = [
    {
        "date": " 2026-10-01 ",
        "category": "早餐",
        "amount": "85",
        "note": " 便利商店 ",
    },
    {
        "date": "2026-10-02",
        "category": "交通 ",
        "amount": "120",
        "note": "捷運",
    },
    {
        "date": "2026-10-03",
        "category": "日用品",
        "amount": " 350 ",
        "note": "洗衣精",
    },
    {
        "date": "2026-10-04",
        "category": "晚餐",
        "amount": "240",
        "note": "",
    },
    {
        "date": "2026-10-05",
        "category": "交通",
        "amount": "60",
    },
]

# 使用者輸入本月預算
# 如果金額是浮點數，就列出錯誤
while True:
    budget_text = input("請輸入本月預算:").strip()
    try:
        budget = int(budget_text)
        break
    except ValueError:
        print("錯誤：金額不能包含小數點，請重新輸入！")
# 資料清洗-交代工作
def clean_text(text,default):
    cleaned = text.strip()
    if cleaned == "":
        return default
    return cleaned
def clean_expense(raw_expense):
    date = clean_text(raw_expense["date"],"")
    category = clean_text(raw_expense["category"],"")
    amount = float(clean_text(raw_expense["amount"],""))
    note = clean_text(raw_expense.get("note",""),"未填寫")

    return{
        "date":date,
        "category":category,
        "amount":amount,
        "note":note
    }

def clean_expenses(raw_expenses):
    expenses = []
    for raw_expense in raw_expenses:
        cleaned = clean_expense(raw_expense)
        expenses.append(cleaned)
    return expenses

expenses = clean_expenses(raw_expenses)
#告訴排序該看那一行
def get_amount(expense):
    return expense["amount"]
def validate_expense(expense):
    return(
        expense["date"] != "" and
        expense["category"] != "" and
        expense["amount"] > 0 and
        expense["note"] != ""    
    )
def print_report(expenses, budget):
    # 將金額列成清單
    amounts = []
    for expense in expenses:
        amounts.append(expense["amount"])
    # 總支出
    total = sum(amounts)
    # 標題
    print("--- 家庭月度支出報表 ---")
    # 逐筆印出
    for number, expense in enumerate(expenses, start=1):
        ratio = expense["amount"] / total
        print(f"{number:02d}. {expense['date']} {expense['category']:<8}"
              f"{expense['amount']:>8.2f} 元  占比 {ratio:>5.1%}  {expense['note']}")
     # 計算統計
    count = len(amounts)
    average = total / count
    highest = max(amounts)
    lowest = min(amounts)
    remainimg = budget - total
    #判斷預算狀態
    if total <= budget:
        status = "尚未超支"
    else:
        status = "已超支"
    has_large = any(amount >= 500 for amount in amounts)
    all_valid = all(amount > 0 for amount in amounts)
    #印出統計
    print()
    print(f"支出筆數:{count} 筆")
    print(f"總支出：{total:,.2f} 元")
    print(f"平均每筆：{average:,.2f} 元")
    print(f"最高支出：{highest:,.2f} 元")
    print(f"最低支出：{lowest:,.2f} 元")
    print(f"本月預算：{budget:,.2f} 元")
    print(f"剩餘預算：{remainimg:,.2f} 元")
    print(f"預算狀態：{status}")
    print(f"是否有單筆支出達 500 元：{has_large}")
    print(f"所有支出金額是否有效：{all_valid}")
# =====主程式=====
# 資料清洗
expenses = clean_expenses(raw_expenses)
# 覆核
valid_expenses = []
for expense in expenses:
    if validate_expense(expense):
        valid_expenses.append(expense)
# 排序
sorted_expenses = sorted(valid_expenses, key=get_amount,reverse=True)
# 出報表
print_report(sorted_expenses, budget)
