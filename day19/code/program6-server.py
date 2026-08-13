# pip install mysql-connector-python

from flask import Flask, request, jsonify
import mysql.connector


# open the connection
connection = mysql.connector.connect(
    host="127.0.0.1",       # host running mysql server
    user="root",            # user name of mysql server
    password="root",        # password for the mysql server user
    database="sample_db",   # database name
    port=3306               # mysql port number
)

# create flask app
app = Flask(__name__)

@app.route('/todo', methods=['GET'])
def get_todo_items():
    # create a cursor
    cursor = connection.cursor()

    # execute the query
    cursor.execute("SELECT id, title, description, complete_status, created_timestamp FROM todo_items;")

    # get all the rows (list of tuples)
    rows = cursor.fetchall()

    # convert the list of tuples to list of dictionaries
    items = []
    for (id, title, description, complete_status, created_timestamp) in rows:
        items.append({
            "id": id,
            "title": title,
            "description": description,
            "complete_status": complete_status,
            "created_timestamp": created_timestamp
        })

    # close the cursor
    cursor.close()

    # return the data
    return items

@app.route('/todo', methods=['POST'])
def post_todo_item():
    # get the json data sent by client
    title = request.json.get('title')
    description = request.json.get('description')

    # create cursor
    cursor = connection.cursor()

    # execute the insert query
    cursor.execute("INSERT INTO todo_items (title, description) VALUES (%s, %s)", (title, description))

    # commit the changes
    connection.commit()

    # close the cursor
    cursor.close()

    return jsonify({"status": "success", "message": "successfully inserted new item"})

@app.route('/todo/<id>', methods=['DELETE'])
def delete_todo_item(id):
    # create cursor
    cursor = connection.cursor()

    # execute the insert query
    cursor.execute("DELETE FROM todo_items WHERE id = %s", (id,))

    # commit the changes
    connection.commit()

    # close the cursor
    cursor.close()

    return jsonify({"status": "success"})

@app.route('/todo/<id>', methods=['PUT'])
def edit_todo_item(id):
    # get the json data sent by client
    title = request.json.get('title')
    description = request.json.get('description')

    # create cursor
    cursor = connection.cursor()

    # execute the insert query
    cursor.execute("UPDATE todo_items set title = %s, description = %s WHERE id = %s", (title, description, id))

    # commit the changes
    connection.commit()

    # close the cursor
    cursor.close()

    return jsonify({"status": "success", "message": "successfully inserted new item"})


# run the application
app.run(host="0.0.0.0", port=5200, debug=True)
