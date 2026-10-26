def clean_text(value, default_value):
    value = value.strip()

    if value == "":
        return default_value

    return value


def clean_learner(raw_learner):
    name = clean_text(
        raw_learner.get("name", ""),
        "未提供姓名",
    )
    goal = clean_text(
        raw_learner.get("goal", ""),
        "未提供目標",
    )

    hours_per_day = float(
        raw_learner.get("hours_per_day", 0)
    )
    days_per_week = int(
        raw_learner.get("days_per_week", 0)
    )

    return {
        "name": name,
        "weekly_hours": hours_per_day * days_per_week,
        "goal": goal,
    }


def clean_learners(raw_learners):
    learners = []

    for raw_learner in raw_learners:
        learner = clean_learner(raw_learner)
        learners.append(learner)

    return learners


def main():
    raw_learners = [
        {
            "name": "  小明 ",
            "hours_per_day": "2",
            "days_per_week": 5,
            "goal": "學會 Python",
        },
        {
            "name": "小華",
            "hours_per_day": "1",
            "days_per_week": 3,
            "goal": "",
        },
        {
            "name": " 阿美 ",
            "hours_per_day": "0.5",
            "days_per_week": 2,
        },
    ]

    learners = clean_learners(raw_learners)

    print("--- 整理後的學員資料 ---")

    for learner in learners:
        print(learner)


if __name__ == "__main__":
    main()