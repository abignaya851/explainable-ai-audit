import subprocess
import os

def test_explain_runs():
    res = subprocess.run(["python", "src/explain.py"], capture_output=True, text=True)
    assert res.returncode == 0, res.stderr
    assert os.path.exists("shap_summary.png")
