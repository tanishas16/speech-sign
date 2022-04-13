import sys
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    data = request.json.get("data")
    print("tanzu")
    print(data)
    return jsonify({"data": {"val": data}})
if __name__ == "__main__":
    app.run(debug=True, threaded=True)
