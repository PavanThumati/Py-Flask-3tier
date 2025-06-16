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

from flask import Flask, render_template, request, redirect
import pymysql
import config

app = Flask(__name__)

db = pymysql.connect(
    host=config.DB_HOST,
    user=config.DB_USER,
    password=config.DB_PASSWORD,
    database=config.DB_NAME
)

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
    return render_template("index.html", users=users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
