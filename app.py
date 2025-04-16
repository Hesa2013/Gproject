from flask import Flask, render_template, request, redirect, url_for
from mysql.connector import Error
import mysql.connector
import logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Heesahross5&",
            database="system_analysis_&_design"  # تغيير المسافات إلى _
        )
        if connection.is_connected():
            logging.error("Connected to MySQL Database")
        return connection
    except Error as e:
        logging.error(f"Error: {e}")
        return None

# استدعاء ملفات html
@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        full_name = request.form['name']
        user_id = request.form['id']

        # انشاء اتصال بقاعدة البيانات
        connection = create_connection()
        if connection is None:
            return "خطأ في الاتصال بقاعدة البيانات"

        # ادخال قاعدة البيانات في قاعدة البيانات
        cursor = connection.cursor()
        cursor.execute("INSERT INTO create_account (username, password, full_name, id) VALUES (%s, %s, %s, %s)",
                       (username, password, full_name, user_id))
        connection.commit()
        cursor.close()
        connection.close()

        # اعادة التوجيه الى صفحة تسجيل الدخول بعد نجاح التسجيل
        return redirect(url_for('login'))

    return render_template('create_account.html')  # التاكد من ان الصفحة هي create_account.html

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()

        connection = create_connection()
        if connection is None:
            return "خطأ في الاتصال بقاعدة البيانات"

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM create_account WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()

        cursor.close()
        connection.close()

        if user:
            return redirect(url_for('introduction'))
        else:
            return "Invalid username or password"   # فشل تسجيل الدخول

    return render_template('login.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sad/introduction')
def introduction():
    return render_template('SAD/introduction.html')

@app.route('/sad/study_plan')
def study_plan():
    return render_template('SAD/study_plan.html')

@app.route('/sad/faq')
def faq():
    return render_template('SAD/faq.html')

@app.route('/practical_project')
def practical_project():
    return render_template('practical_project.html')

@app.route('/training')
def training():
    return render_template('training.html')

@app.route('/final_page')
def final_page():
    return render_template('final_page.html')

if __name__ == '__main__':
    app.run(debug=True)