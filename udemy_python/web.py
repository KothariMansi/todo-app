import streamlit as st
from functions import get_todos,create_file

FILEPATH = "udemy_python/files/todoss.txt"

create_file(FILEPATH)
#todos = get_todos('udemy_python/files/todoss.txt')
#todos = get_todos('todoss.txt')
todos = get_todos(FILEPATH)

st.title("My ToDo App")
st.subheader("This is My Todo App")
st.write("This app is for you to help record of things to do.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo....", key='x')
