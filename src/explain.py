import joblib
import shap
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load model
obj = joblib.load("model.joblib")
model = obj["model"]
feature_names = obj["feature_names"]

# Load sample data
data = load_iris()
X = pd.DataFrame(data.data, columns=feature_names)

# Explain model
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

# Create summary plot
shap.summary_plot(shap_values, X, show=False)
plt.savefig("shap_summary.png")
print("✅ SHAP summary saved as shap_summary.png")
