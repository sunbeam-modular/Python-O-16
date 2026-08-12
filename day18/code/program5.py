import streamlit as st
import sqlite3
import pandas as pd

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
    cursor.execute("SELECT title, description, complete_status from todo_items")

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

# write header
st.header("Todo Application")

# write subheader
st.subheader("Manage your todo items easily")

# get input from user
title = st.text_input("enter title")
description = st.text_area("enter description")
button_save = st.button("Add")

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
    # create data frame using the items
    df = pd.DataFrame(todo_items, columns=["Title", "Description", "Status"])

    # display the list of items
    st.write(df)
else:
    st.warning("There are no todo items created yet")
