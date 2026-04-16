import os
import csv
import pandas as pd

def save_leaderboard(results):
    os.makedirs('leaderboard', exist_ok=True)
    scores_path = 'leaderboard/scores.csv'

    with open(scores_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Model Name', 'Accuracy (%)', 'F1-Score (%)'])

        for name, res in results.items():
            writer.writerow([name, res['Accuracy'], res['F1-Score']])

    print(f'Leaderboard saved at: {scores_path}')
    return scores_path
