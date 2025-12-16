import sqlite3
from typing import List
import datetime
from .model import Todo

conn = sqlite3.connect('todos.db', check_same_thread=False)
c = conn.cursor()


def create_table():
    c.execute("""
        CREATE TABLE IF NOT EXISTS todos(
            task TEXT,
            category TEXT,
            date_added TEXT,
            date_completed TEXT,
            status INTEGER,
            position INTEGER
        )
    """)
    conn.commit()


create_table()


def insert_todo(todo: Todo):
    c.execute("SELECT COUNT(*) FROM todos")
    count = c.fetchone()[0]

    todo.position = count  

    with conn:
        c.execute("""
            INSERT INTO todos 
            VALUES (:task, :category, :date_added, :date_completed, :status, :position)
        """, {
            'task': todo.task,
            'category': todo.category,
            'date_added': todo.date_added,
            'date_completed': todo.date_completed,
            'status': todo.status,
            'position': todo.position
        })


def get_all_todos() -> List[Todo]:
    c.execute("SELECT * FROM todos ORDER BY position ASC")
    rows = c.fetchall()

    todos = []
    for row in rows:
        todos.append(Todo(*row))

    return todos   


def delete_todo(position: int):
    c.execute("SELECT COUNT(*) FROM todos")
    count = c.fetchone()[0]

    with conn:
        
        c.execute("DELETE FROM todos WHERE position = :position",   {"position": position})

        for pos in range(position + 1, count):
            change_position(pos, pos - 1)


def change_position(old_position: int, new_position: int, commit=True):
    c.execute("""
        UPDATE todos 
        SET position = :new_position 
        WHERE position = :old_position
    """, {
        "old_position": old_position,
        "new_position": new_position
    })
    if commit:
        conn.commit()


def update_todo(position: int, task: str, category: str):
    with conn:
        if task is not None and category is not None:
            c.execute("""
                UPDATE todos SET task = :task, category = :category WHERE position = :position """, {'position': position, 'task': task, 'category': category})

        elif task is not None:
            c.execute("""
                UPDATE todos SET task = :task 
                WHERE position = :position
            """, {'position': position, 'task': task})

        elif category is not None:
            c.execute("""
                UPDATE todos SET category = :category 
                WHERE position = :position
            """, {'position': position, 'category': category})


def complete_todo(position: int):
    with conn:
        c.execute("""
            UPDATE todos 
            SET status = 2, date_completed = :date_completed 
            WHERE position = :position
        """, {
            'position': position,
            'date_completed': datetime.datetime.now().isoformat()})
