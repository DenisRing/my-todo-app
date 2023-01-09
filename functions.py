"""
stores the funciton calls for main.py
A list is a class, and we create instances of it, instances of lists
"""



def get_todos(filepath="todos.txt"):
    """
    This is a docstring. Read a file and return
    list of to-do items.
    """
    with open(filepath) as file_local:
        todos_local = file_local.readlines()
    return todos_local



def write_todos(todos_arg, filepath="todos.txt"): #non default params must go before default paras
    """
    Write the to-do items list in the text file
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)




if __name__ == "__main__": ##this only executes if functions is the main file, e.g. we are running functions.py directly (not related to main.py)
    print("Hello from functions")
    print(get_todos())