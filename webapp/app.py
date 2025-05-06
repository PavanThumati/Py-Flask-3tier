from flask import Flask, render_template
import pymysql
import config

app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host=config.DB_HOST,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        database=config.DB_NAME
    )

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM users")  # example table
    users = cursor.fetchall()
    conn.close()
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
