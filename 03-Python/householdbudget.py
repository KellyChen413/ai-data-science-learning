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
budget=float(input("請輸入本月預算:"))
# 資料清洗
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
def validate_expense(expense):
    return(
        expense["date"] != "" and
        expense["category"] != "" and
        expense["amount"] > 0 and
        expense["note"] != ""    
    )
print(validate_expense(expenses[0]))   # 預期：True

# 故意做一張壞單據測試
bad = {"date": "", "category": "早餐", "amount": 85.0, "note": "便利商店"}
print(validate_expense(bad))           # 預期：False（日期是空的）