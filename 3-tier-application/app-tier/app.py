# from flask import Flask, render_template
# import pymysql
# import config

# app = Flask(__name__)

# def get_db_connection():
#     return pymysql.connect(
#         host=config.DB_HOST,
#         user=config.DB_USER,
#         password=config.DB_PASSWORD,
#         database=config.DB_NAME
#     )

# @app.route('/')
# def index():
#     conn = get_db_connection()
#     cursor = conn.cursor()
#     cursor.execute("SELECT id, name FROM users")
#     users = cursor.fetchall()
#     conn.close()
#     return render_template('index.html', users=users)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)

from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST", "db")
DB_USER = os.environ.get("DB_USER", "root")
DB_PASS = os.environ.get("DB_PASS", "root")
DB_NAME = os.environ.get("DB_NAME", "userdb")

@app.route("/users", methods=["GET"])
def get_users():
    conn = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users)

@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    name, email = data["name"], data["email"]
    conn = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "User added successfully"}, 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
