def clean_text(value):
    return value.strip()


def calculate_weekly_hours(hours_per_day, days_per_week):
    return hours_per_day * days_per_week


def recommend_plan(weekly_hours, has_goal):
    if weekly_hours >= 6 and has_goal:
        return "密集方案"
    elif weekly_hours >= 3:
        return "一般方案"
    else:
        return "預備學習"


def build_report(name, goal, hours_per_day, days_per_week):
    clean_name = clean_text(name)
    clean_goal = clean_text(goal)
    weekly_hours = calculate_weekly_hours(
        hours_per_day,
        days_per_week,
    )
    has_goal = bool(clean_goal)
    plan = recommend_plan(weekly_hours, has_goal)

    return (
        f"姓名：{clean_name}\n"
        f"學習目標：{clean_goal}\n"
        f"每週學習時數：{weekly_hours:.1f} 小時\n"
        f"建議方案：{plan}"
    )