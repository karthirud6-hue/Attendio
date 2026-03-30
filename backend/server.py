from flask import Flask, request, jsonify
import csv
from datetime import datetime

app = Flask(__name__)

@app.route('/mark_attendance', methods=['POST'])
def mark_attendance():
    data = request.json
    name = data.get("name")

    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    with open("attendance.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, date, time, "Present"])

    return jsonify({"message": f"{name} marked present"})


@app.route('/get_attendance', methods=['GET'])
def get_attendance():
    data = []

    try:
        with open("attendance.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(row)
    except:
        pass

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
