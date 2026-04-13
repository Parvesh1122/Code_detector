from flask import Flask, request, jsonify, render_template
import os
import re

app = Flask(__name__)

DATASET_PATH = "dataset"


# ---------------- HOME ----------------
@app.route('/')
def home():
    return render_template("index.html")


# ---------------- VALIDATION ----------------
def is_valid_code(code):
    return bool(code and code.strip())


# ---------------- LANGUAGE DETECTION ----------------
def detect_language(code):
    code = code.lower()
    if "#include" in code or "int main" in code:
        return "C++"
    elif "function" in code or "console.log" in code:
        return "JavaScript"
    elif "<html" in code:
        return "HTML"
    elif "def " in code:
        return "Python"
    return "Unknown"


# ---------------- PREPROCESS (IMPROVED) ----------------
def preprocess(code):
    # remove comments
    code = re.sub(r'//.*|/\*.*?\*/', '', code, flags=re.DOTALL)

    # lowercase
    code = code.lower()

    # replace variable names → normalize
    code = re.sub(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', 'var', code)

    # remove spaces
    code = ''.join(code.split())

    return code


# ---------------- LCS ----------------
def lcs(X, Y):
    m, n = len(X), len(Y)
    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(m):
        for j in range(n):
            if X[i] == Y[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

    return dp[m][n]


def similarity_score(a, b):
    if not a or not b:
        return 0
    return (lcs(a, b) / max(len(a), len(b))) * 100


# ---------------- CLASSIFICATION ----------------
def classify(score):
    if score == 100:
        return "Exact Copy (Plagiarism Confirmed)"
    elif score > 80:
        return "High Plagiarism"
    elif score > 50:
        return "Moderate Similarity"
    else:
        return "Low Similarity"


# ---------------- MAIN API ----------------
@app.route('/check', methods=['POST'])
def check():
    data = request.get_json()

    if not data or "code" not in data:
        return jsonify({"error": "Invalid request"}), 400

    user_code = data["code"]

    if not is_valid_code(user_code):
        return jsonify({"error": "Enter code first"}), 400

    if not os.path.exists(DATASET_PATH):
        return jsonify({"error": "Dataset not found"}), 500

    files = os.listdir(DATASET_PATH)
    if not files:
        return jsonify({"error": "Dataset empty"}), 500

    user_code_clean = preprocess(user_code)
    language = detect_language(user_code)

    best_score = 0
    best_file = "No match"

    for file in files:
        path = os.path.join(DATASET_PATH, file)

        if not os.path.isfile(path):
            continue

        with open(path, 'r', errors='ignore') as f:
            dataset_code = preprocess(f.read())

            # 🔥 EXACT MATCH CHECK
            if user_code_clean == dataset_code:
                return jsonify({
                    "similarity": 100.0,
                    "file": file,
                    "language": language,
                    "type": "Exact Copy (Plagiarism Confirmed)"
                })

            score = similarity_score(user_code_clean, dataset_code)

            if score > best_score:
                best_score = score
                best_file = file

    return jsonify({
        "similarity": round(best_score, 2),
        "file": best_file,
        "language": language,
        "type": classify(best_score)
    })


if __name__ == "__main__":
    app.run(debug=True)