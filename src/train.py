import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load toy data
data = load_iris()
X, y = data.data, data.target

# Split and train
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X_train, y_train)

# Save model and feature names
joblib.dump({
    "model": model,
    "feature_names": data.feature_names
}, "model.joblib")

print("✅ Model saved as model.joblib")
