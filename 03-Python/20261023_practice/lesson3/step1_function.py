#套件區
#定義區
def calculate_total_hours(hours_per_day, days):
    """
    說明calculate_total_hours函式會將每天學習時數和總天數相乘
    hours_per_day:每天學習時數
    """
    total_hours = hours_per_day * days
    return total_hours
    print() #寫在return後面就不會執行到
#主程式計入點
hours_per_day = float(input("每天學習幾小時："))
days = int(input("學習幾天："))

total_hours = calculate_total_hours(hours_per_day, days)

print("--- 執行結果 ---")
print(f"總學習時數：{total_hours:.1f} 小時")