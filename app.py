from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Подключение к базе данных
def get_db_connection():
    conn = sqlite3.connect('courier_delivery_db.sqlite')
    conn.row_factory = sqlite3.Row  # Для работы с результатами как с объектами
    return conn

# Главная страница
@app.route('/')
def index():
    conn = get_db_connection()
    data = conn.execute('SELECT * FROM full_info').fetchall()  # Получаем все данные из объединенной таблицы
    conn.close()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
