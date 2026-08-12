import sqlite3

# connect to the sqlite database
connection = sqlite3.connect("mydb.sqlite")

def initialize_schema():
    # open a cursor
    cursor = connection.cursor()

    # execute a sql statement to create a table
    # IF NOT EXISTS: create the table only if it does not exist
    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS todo_items(
        id INTEGER primary key autoincrement,
        title TEXT,
        description TEXT,
        complete_status BOOLEAN DEFAULT 0
    )
    """)

    # close the cursor
    cursor.close()

    # commit the changes
    connection.commit()

initialize_schema()

def show_todo_items():
    # get the cursor
    cursor = connection.cursor()

    # execute the select statement
    cursor.execute("SELECT id, title, description, complete_status from todo_items")

    # get the data
    items = cursor.fetchall()
    print('-' * 60)
    print(f"| {'id':<3} | {'Title':<40} | {'Status':>7} |")
    print('-' * 60)
    for (id, title, description, status) in items:
        print(f"| {id:<3} | {title:<40} | {status:^7} |")
        print('-' * 60)
    print()

    # close the cursor
    cursor.close()

def show_todo_item_details():
    # get the id from user
    id = int(input("enter id: "))

    # get the cursor
    cursor = connection.cursor()

    # execute the select statement
    cursor.execute("SELECT title, description, complete_status from todo_items where id = ?", (id, ))

    # get the data
    item = cursor.fetchone()
    if item is None:
        print(f"error: the todo item with requested id does not exist")
    else:
        # unpack the item
        # item: ('complete python assignments', 'complete python assignments from 1 to 6 before this weekend.', 0)
        title, description, complete_status = item

        print(f"title          : {title}")
        print(f"description    : {description}")
        print(f"complete status: {complete_status}")

    print()

    # close the cursor
    cursor.close()

def insert_todo_item():
    # get the input from user
    title = input("enter title: ")
    description = input("enter description: ")

    # get the cursor
    cursor = connection.cursor()

    # execute the select statement
    cursor.execute(
        "INSERT INTO todo_items (title, description) VALUES (?, ?)",
        # the first ? will be replaced with title value
        # the second ? will be replaced with description value
        (title, description))

    # persist the changes
    connection.commit()

    # close the cursor
    cursor.close()

def edit_todo_item():
    # get the input from user
    id = int(input("ente id: "))
    title = input("enter title: ")
    description = input("enter description: ")

    # get the cursor
    cursor = connection.cursor()

    # execute the select statement
    cursor.execute(
        "UPDATE todo_items set title = ?, description = ? WHERE id = ?",
        (title, description, id))

    # persist the changes
    connection.commit()

    # close the cursor
    cursor.close()

def mark_complete_todo_item():
    # get the input from user
    id = int(input("ente id: "))

    # get the cursor
    cursor = connection.cursor()

    # execute the select statement
    cursor.execute(
        "UPDATE todo_items set complete_status = 1 WHERE id = ?",
        (id, ))

    # persist the changes
    connection.commit()

    # close the cursor
    cursor.close()

def delete_todo_item():
    # get the input from user
    id = int(input("ente id: "))

    # get the cursor
    cursor = connection.cursor()

    # execute the select statement
    cursor.execute("DELETE FROM todo_items WHERE id = ?",(id, ))

    # persist the changes
    connection.commit()

    # close the cursor
    cursor.close()

def show_menu():
    print("Welcome to the Todo application")
    print("1. list the todo items")
    print("2. add an item")
    print("3. get existing item details")
    print("4. edit existing item")
    print("5. complete an item")
    print("6. delete an item")
    print("7. exit")

    # get choice from user
    choice = int(input("enter your choice: "))
    return choice

while True:
    # show the menu and get input from user
    choice = show_menu()

    if choice == 1:
        show_todo_items()
    elif choice == 2:
        insert_todo_item()
    elif choice == 3:
        show_todo_item_details()
    elif choice == 4:
        edit_todo_item()
    elif choice == 5:
        mark_complete_todo_item()
    elif choice == 6:
        delete_todo_item()
    elif choice == 7:
        print("bye bye..")
        break
    else:
        print("wrong input")

# close the connection
connection.close()