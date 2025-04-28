from flask import Flask, jsonify
import mysql.connector

app = Flask(_name_)

# Conexión a la base de datos
def get_db_connection():
    connection = mysql.connector.connect(
        host='db',  # Nombre del contenedor de base de datos
        user='root',
        password='rootpassword',
        database='users_db'
    )
    return connection

@app.route('/list_users', methods=['GET'])
def list_users():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    connection.close()
    return jsonify(users)

if _name_ == '_main_':
    app.run(debug=True, host='0.0.0.0')