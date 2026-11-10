import pandas as pd
df = pd.DataFrame({
    "worker": ["Worker-A", "Worker-B", "Worker-C"],
    "no_helmet_count": [3, 0, 7]
})

df["risk_score"] = df["no_helmet_count"]
print(df)
def risk_level(score):
    if score > 5 :
        return "safe"
    elif score >= 1:
        return "warning"
    else:
        return "safe"
df["risk_level"] = df["risk_score"].apply(risk_level)
print(df)
