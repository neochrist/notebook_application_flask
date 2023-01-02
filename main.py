from flask import Flask
from flask import request, jsonify
import pymysql

app = Flask(__name__)

# Set up the database connection
connection = pymysql.connect(host="localhost", user="neochrist", password="pass", db="test4")

# Create a route to return all persons
@app.route("/persons", methods=["GET"])
def get_all_persons():
  try:
    with connection.cursor() as cursor:
      # Select all persons from the database
      sql = "SELECT * FROM persons"
      cursor.execute(sql)
      result = cursor.fetchall()
      return jsonify(result)
  except Exception as e:
    return str(e)

# Create a route to create a new person
@app.route("/persons/create", methods=["POST"])
def create_person():
  try:
    with connection.cursor() as cursor:
      # Read the data from the request
      data = request.get_json()
      name = data["name"]
      surname = data["surname"]
      # phone_number = data["phone_number"]
      # description = data["description"]
      
      # Insert the new person into the database
      sql = "INSERT INTO persons (name, surname) VALUES (%s, %s)"
      cursor.execute(sql, (name, surname))
      connection.commit()
      return "Person created successfully"
  except Exception as e:
    return str(e)

# Create a route to get all persons with the same name
@app.route("/persons/name/<name>", methods=["GET"])
def get_persons_by_name(name):
  try:
    with connection.cursor() as cursor:
      # Select all persons with the specified name from the database
      sql = "SELECT * FROM persons WHERE name = %s"
      cursor.execute(sql, name)
      result = cursor.fetchall()
      return jsonify(result)
  except Exception as e:
    return str(e)

# Create a route to get all persons with the same surname
if __name__ == "__main__":
  app.run()

