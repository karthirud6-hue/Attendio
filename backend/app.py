from flask import Flask, request, jsonify
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# Connect to your MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="attendio"
)
cursor = db.cursor()

@app.route("/mark_attendance", methods=["POST"])
def mark_attendance():
    data = request.get_json()
    name = data.get("name")
    
    if not name:
        return jsonify({"status": "error", "message": "No name provided"}), 400
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Example: Insert attendance or update if exists
    cursor.execute("""
        INSERT INTO attendance (name, status, timestamp) 
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE status=%s, timestamp=%s
    """, (name, "Present", timestamp, "Present", timestamp))
    
    db.commit()
    return jsonify({"status": "success", "name": name})

if __name__ == "__main__":
    app.run(debug=True)
