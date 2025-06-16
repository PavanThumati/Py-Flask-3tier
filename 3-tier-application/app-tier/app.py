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
import mysql.connector, os, config

app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host=config.DB_HOST,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        database=config.DB_NAME
    )


@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, email) VALUES (%s, %s)', (data['name'], data['email']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'User added successfully'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
