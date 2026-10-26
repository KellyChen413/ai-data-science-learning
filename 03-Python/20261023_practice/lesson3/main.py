from lesson3.learning_rules import build_report


def main():
    name = input("姓名：")
    goal = input("學習目標：")
    hours_per_day = float(input("每天學習幾小時："))
    days_per_week = int(input("每週學習幾天："))

    report = build_report(
        name,
        goal,
        hours_per_day,
        days_per_week,
    )

    print("--- 學習報告 ---")
    print(report)


if __name__ == "__main__":
    main()