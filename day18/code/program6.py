import streamlit as st
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

def get_todo_items():
    # get the cursor
    cursor = connection.cursor()

    # execute the select statement
    cursor.execute("SELECT id, title, description, complete_status from todo_items")

    # get the data
    items = cursor.fetchall()
    
    # close the cursor
    cursor.close()

    return items

def insert_todo_item(title, description):
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

def mark_complete_todo_item(id):
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

def delete_todo_item(id):
    # get the cursor
    cursor = connection.cursor()

    # execute the select statement
    cursor.execute("DELETE FROM todo_items WHERE id = ?",(id, ))

    # persist the changes
    connection.commit()

    # close the cursor
    cursor.close()

# write header
st.header("Todo Application")

# write subheader
st.subheader("Manage your todo items easily")

# get input from user
title = st.text_input("enter title")
description = st.text_area("enter description")
button_save = st.button("Add", key="save")

# check if button_save is clicked
if button_save:
    # make sure that the title and description have non-empty string values
    if title and description:
        # inser new item in the database
        insert_todo_item(title=title, description=description)
    else:
        st.warning("title and description are mandatory")


# create a header for the list of todo items
st.subheader("Your Todo Items")

# get all todo items from table
todo_items = get_todo_items()

# check if there are any todo items in the table
if todo_items:
    for id, title, description, status in todo_items:
        # create 4 equal columns
        # col1, col2, col3, col4 = st.columns(4)

        # create 4 columns with different widths
        col1, col2, col3, col4 = st.columns([2, 4, 0.5, 1])

        # add the contents in col1
        with col1:
            st.write(title)

        # add the contents in col2
        with col2:
            st.write(description)

        # add the contents in col3
        with col3:
            checkbox = st.checkbox("", value=status, key=f"status_{id}")
            if checkbox:
                mark_complete_todo_item(id)

        # add the contents in col4
        with col4:
            button_delete = st.button("delete", key=f"delete_{id}")

            # check if delete button is clicked
            if button_delete:
                # delete the item by its id
                delete_todo_item(id)

                # restart the page
                st.rerun()
    
else:
    st.warning("There are no todo items created yet")
