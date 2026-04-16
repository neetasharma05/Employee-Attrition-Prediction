import pandas as pd
import os

def update_leaderboard(name, accuracy, f1_score):
    os.makedirs('leaderboard', exist_ok=True)
    path = 'leaderboard/scores.csv'

    # Load existing data
    if os.path.exists(path):
        df = pd.read_csv(path)
    else:
        df = pd.DataFrame(columns=["Name", "Accuracy (%)", "F1-Score (%)"])

    # Add new entry
    new_entry = pd.DataFrame([[name, accuracy, f1_score]],
                             columns=["Name", "Accuracy (%)", "F1-Score (%)"])

    df = pd.concat([df, new_entry], ignore_index=True)

    # Sort leaderboard
    df = df.sort_values(by="Accuracy (%)", ascending=False)

    # Save back
    df.to_csv(path, index=False)

    print("✅ Leaderboard Updated!")
    return df
