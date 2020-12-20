
def add_subject(name):
    # without debug
    if len(get(f"SELECT id from tasks WHERE name = {name!r};")) != 0:
        return "ERROR"
    insert(f"INSERT INTO tasks (id_subject, data) VALUES({id_subject!r}, {text!r});")
    return get(f"SELECT id from tasks WHERE id_subject = {id_subject!r} and data = {text!r};")[0][0]


def add_task(any_json, id_subject):
    # without debug
    if len(get(f"SELECT id from tasks WHERE data = {any_json!r};")) != 0:
        return "ERROR"
    insert(f"INSERT INTO tasks (id_subject, data) VALUES({id_subject}, {any_json!r});")
    return get(f"SELECT id from tasks WHERE data = {any_json!r};")[0][0]


def add_class(name):
    # without debug
    if len(get(f"SELECT id from students WHERE class = {name!r};")) != 0:
        return "ERROR"
    insert(f"INSERT INTO classes (name) VALUES({name!r});")
    return get(f"SELECT id from classes WHERE name = {name!r};")[0][0]


def add_test(name, task_list:str, id_class):
    # without debug
    if len(get(f"SELECT id from tests WHERE name = {name!r};")) != 0:
        return "ERROR"
    insert(f"INSERT INTO tests (name, id_class, list_tasks) VALUES({name}, {id_class}, {task_list});")
    return get(f"SELECT id from test WHERE name = {name!r};")[0][0]


def add_answer(any_json, id_task, id_student):
    # without debug
    if len(get(f"SELECT id from answers WHERE data = {any_json!r};")) != 0:
        return "ERROR"
    insert(f"INSERT INTO answers (id_task, id_student, data) VALUES({id_task}, {id_student}, {any_json!r});")
    return get(f"SELECT id from answers WHERE data = {any_json!r};")[0][0]


def get_all_users():
    answer = ""
    for line in get("SELECT * FROM students;"):
        _answer = ""
        for j in line:
            _answer += f"{j},"
        answer += f"{_answer[0:-1]};"
    return answer


def get_all_teachers():
    answer = ""
    for line in get("SELECT * FROM teachers;"):
        _answer = ""
        for j in line:
            _answer += f"{j},"
        answer += f"{_answer[0:-1]};"
    return answer


def add_student(FIO, login, password, school):
    if len(get(f"SELECT id from teachers WHERE login = {login!r};")) or \
       len(get(f"SELECT id from students WHERE login = {login!r};")) != 0:
        return "ERROR"

    insert(f"INSERT INTO students (FIO, login, password, school) VALUES({FIO!r}, {login!r}, {password!r}, {school!r});")
    return get(f"SELECT id from students WHERE login = {login!r};")[0][0]


def add_teacher(FIO, login, password):
    if len(get(f"SELECT id from teachers WHERE login = {login!r};")) or \
       len(get(f"SELECT id from students WHERE login = {login!r};")) != 0:
        return "ERROR"

    insert(f"INSERT INTO teachers (FIO, login, password) VALUES({FIO!r}, {login!r}, {password!r});")
    return get(f"SELECT id from teachers WHERE login = {login!r};")[0][0]


def login(login, password):
    teachers = get(f"SELECT id from teachers WHERE login = {login!r} and password = {password!r};")
    students = get(f"SELECT id from students WHERE login = {login!r} and password = {password!r};")
    if len(teachers) != 0:
        id = teachers[0][0]
        return f"teacher,{id}"
    if len(students) != 0:
        id = students[0][0]
        return f"student,{id}"
    return "ERROR"


def get_student():
    pass


def delete_all_students():
    insert(f"DELETE FROM students;")
    return "OK"


def delete_all_teachers():
    insert(f"DELETE FROM teachers;")
    return "OK"

