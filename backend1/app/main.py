from flask import Flask, request, jsonify
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

@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data['name']
    email = data['email']

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO users (name, email) VALUES (%s, %s)', (name, email))
    connection.commit()
    connection.close()

    return jsonify({'message': 'User created successfully'}), 201

if _name_ == '_main_':
    app.run(debug=True, host='0.0.0.0')