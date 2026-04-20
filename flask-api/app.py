from flask import Flask, jsonify, send_file
from flask_cors import CORS
import json, os, time

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)
RESULTS = "/data/results"
CSV_PATH = "/data/students.csv"

@app.route("/")
@app.route("/api/")
def api_index():
    return jsonify({
        "status": "online",
        "service": "Hadoop Analytics API",
        "endpoints": ["/api/status", "/api/grades", "/api/subject-averages", "/api/dept-analysis", "/api/top-rankers", "/api/pass-fail", "/api/histogram"]
    })

def parse_tsv(filename):
    data = {}
    path = os.path.join(RESULTS, filename)
    if not os.path.exists(path):
        return data
    try:
        with open(path) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("\t", 1)
                if len(parts) == 2:
                    key = parts[0].strip('"')
                    try:
                        data[key] = json.loads(parts[1])
                    except Exception:
                        data[key] = parts[1]
    except Exception as e:
        print(f"Error reading {filename}: {e}")
    return data

@app.route("/api/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/api/students")
def students():
    if os.path.exists(CSV_PATH):
        return send_file(CSV_PATH, mimetype="text/csv")
    return "Not found", 404

@app.route("/api/grades")
def grades():
    return jsonify(parse_tsv("grade_distribution.txt"))

@app.route("/api/subject-averages")
def subject_averages():
    return jsonify(parse_tsv("subject_average.txt"))

@app.route("/api/dept-analysis")
def dept_analysis():
    return jsonify(parse_tsv("dept_analysis.txt"))

@app.route("/api/top-rankers")
def top_rankers():
    raw = parse_tsv("top_rankers.txt")
    return jsonify(list(raw.values()))

@app.route("/api/pass-fail")
def pass_fail():
    return jsonify(parse_tsv("pass_fail.txt"))

@app.route("/api/histogram")
def histogram():
    return jsonify(parse_tsv("histogram.txt"))

@app.route("/api/status")
def status():
    files = os.listdir(RESULTS) if os.path.exists(RESULTS) else []
    required = ["grade_distribution.txt", "subject_average.txt", "dept_analysis.txt", "top_rankers.txt", "pass_fail.txt", "histogram.txt"]
    ready_files = [f for f in required if os.path.exists(os.path.join(RESULTS, f))]
    return jsonify({
        "ready": len(ready_files) == len(required),
        "files_ready": ready_files,
        "total_required": len(required)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
