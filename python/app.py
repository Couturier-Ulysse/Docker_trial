from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configuration de la base de données
db_config = {
    'user': 'root',
    'password': 'root',
    'host': 'mysql',
    'port': 3306,
    'database': 'db',
}

# Fonction pour récupérer les étudiants depuis la base de données
def get_students_from_db():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute('SELECT FirstName, Surname FROM students')
    students = cursor.fetchall()
    connection.close()
    
    return students

@app.route('/')
def index():
    students = get_students_from_db()
    return render_template('index.html', students=students)

@app.route('/insert', methods=['POST'])
def insert():
    firstname = request.form['firstname']
    surname = request.form['surname']

    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO students (FirstName, Surname) VALUES (%s, %s)", (firstname, surname))
    connection.commit()
    connection.close()

    students = get_students_from_db()
    return render_template('index.html', students=students)

@app.route('/get_students')
def get_students():
    students = get_students_from_db()
    student_data = [{'FirstName': student[0], 'Surname': student[1]} for student in students]
    return jsonify(student_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
