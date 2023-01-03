from flask import Flask
from flask import request, jsonify
import pymysql
import os

app = Flask(__name__)

# Set up the database connection
connection = pymysql.connect(host=os.environ['HOST'], user=os.environ['USER'], 
                                            password=os.environ['PASSWORD'], db=os.environ['DATABASE'] )

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
      phone_number = data["phone_number"]
      description = data["description"]
      
      # Insert the new person into the database
      sql = "INSERT INTO persons (name, surname, phone_number, description) VALUES (%s, %s, %s, %s)"
      cursor.execute(sql, (name, surname, phone_number, description))
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
@app.route("/persons/surname/<surname>", methods=["GET"])
def get_persons_by_name(name):
  try:
    with connection.cursor() as cursor:
      # Select all persons with the specified name from the database
      sql = "SELECT * FROM persons WHERE surname = %s"
      cursor.execute(sql, name)
      result = cursor.fetchall()
      return jsonify(result)
  except Exception as e:
    return str(e)

if __name__ == "__main__":
  app.run()

