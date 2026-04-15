from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report

def train_models(X_train, X_test, y_train, y_test, X_train_scaled=None, X_test_scaled=None):
    
    models = {
        'Logistic Regression': LogisticRegression(
            max_iter=1000, random_state=42, class_weight='balanced'
        ),
        'Decision Tree': DecisionTreeClassifier(
            max_depth=6, random_state=42, class_weight='balanced'
        ),
        'Random Forest': RandomForestClassifier(
            n_estimators=100, random_state=42, class_weight='balanced'
        ),
        'XGBoost': XGBClassifier(
            n_estimators=100, learning_rate=0.1, max_depth=5,
            random_state=42, eval_metric='logloss',
            scale_pos_weight=5
        )
    }

    results = {}

    for name, model in models.items():
        if name == 'Logistic Regression' and X_train_scaled is not None:
            model.fit(X_train_scaled, y_train)
            y_pred = model.predict(X_test_scaled)
        else:
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)

        acc = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred, output_dict=True, zero_division=0)

        results[name] = {
            'Accuracy': round(acc * 100, 2),
            'Precision': round(report['1']['precision'] * 100, 2),
            'Recall': round(report['1']['recall'] * 100, 2),
            'F1-Score': round(report['1']['f1-score'] * 100, 2)
        }

    return results
