FILEPATH = 'todo.txt'


def get_todos(filepath=FILEPATH):
    """read a text file and\
   - returns a todo item"""

    with open(filepath, 'r') as file:
        todo_local = file.readlines()
    return todo_local


def write_todo(todo, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todo)


if __name__ == "__main__":
    print("Hello")
    print(get_todos("todo.txt"))
