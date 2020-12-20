
def add_subject(name):
    # without debug
    insert(f"INSERT INTO subjects (name) VALUES({name!r});")
    return get(f"SELECT id from subjects WHERE name = {name!r};")[0][0]


def add_task(any_json):
    # without debug                                     ?V
    insert(f"INSERT INTO tasks (id_subject, data) VALUES(1, {any_json!r});")
    return get(f"SELECT id from tasks WHERE data = {any_json!r};")[0][0]


def add_class(name):
    # without debug
    insert(f"INSERT INTO classes (name) VALUES({name!r});")
    return get(f"SELECT id from classes WHERE name = {name!r};")[0][0]


def add_test(name, task_list:str):
    # without debug
    # Можно сделать проверку, существует ли тест с таким названием        ?V
    insert(f"INSERT INTO tests (name, id_class, list_tasks) VALUES({name}, 1, {task_list});")
    return get(f"SELECT id from test WHERE name = {name!r};")[0][0]


def add_answer(any_json):
    # without debug                                                ?V ?V
    insert(f"INSERT INTO answers (id_task, id_student, data) VALUES(1, 1, {any_json!r});")
    return get(f"SELECT id from answers WHERE data = {any_json!r};")[0][0]


def delete_anything():
    ...


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

