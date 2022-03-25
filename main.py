from flask import Flask, render_template, request
from flask_cors import CORS
from solver import getSudoku
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/", methods=["GET"])
def get_example():
    return render_template("index.html")

@app.route("/getNewSudoku", methods=["GET"])
def getNewSudoku():
    level = request.args.get('level')
    return getSudoku(level)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)