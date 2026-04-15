import pandas as pd

def save_leaderboard(results, path="leaderboard/scores.csv"):
    data = []

    for name, res in results.items():
        data.append({
            "Model": name,
            "Accuracy": res['Accuracy'],
            "F1-Score": res['F1-Score']
        })

    df = pd.DataFrame(data)
    df = df.sort_values(by="Accuracy", ascending=False)
    df.to_csv(path, index=False)

    return df
