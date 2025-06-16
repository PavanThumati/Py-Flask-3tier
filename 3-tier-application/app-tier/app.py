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

import time
import pymysql
from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

# Wait until the DB is reachable
for i in range(30):
    try:
        db = pymysql.connect(
            host='db',
            user='root',
            password='rootpassword',
            database='userdb'
        )
        print("✅ Connected to MySQL")
        break
    except pymysql.err.OperationalError as e:
        print(f"⏳ Waiting for DB... ({i+1}/30)")
        time.sleep(2)
else:
    raise Exception("❌ Could not connect to DB after 30 attempts")

# HTML page with form and data list
HTML = """
<!DOCTYPE html>
<html>
<head><title>User List</title></head>
<body>
  <h1>User List</h1>
  <form method="POST">
    <input type="text" name="name" placeholder="Enter name" required>
    <button type="submit">Add</button>
  </form>
  <ul>
  {% for user in users %}
    <li>ID: {{ user[0] }}, Name: {{ user[1] }}</li>
  {% endfor %}
  </ul>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    cursor = db.cursor()
    if request.method == 'POST':
        name = request.form['name']
        cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
        db.commit()
        return redirect('/')
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return render_template_string(HTML, users=users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
