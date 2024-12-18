import sqlite3

def hello_message():
    print("Добро пожаловать в программу для выполнения SQL-запросов.")
    print("Введите SQL-запрос (отправьте пустую строку для выполнения запроса):")

def get_sql() -> str:
    sql_list = []
    while True:
        user_input = input(">> ")
        if user_input:
            sql_list.append(user_input)
        else:
            break
    return "\n".join(sql_list)

def make_query(raw_sql: str):
    connection = sqlite3.connect("music.db")
    cursor_object = connection.execute(raw_sql)
    result = cursor_object.fetchall()
    connection.close()
    return result

def make_str_list(db_result: list[tuple]) -> list[str]:
    return [" , ".join(map(str, result)) + "\n" for result in db_result]

def save_result(str_list: list[str], filename: str):
    with open(f"{filename}.txt", "w", encoding="utf-8") as file:
        file.writelines(str_list)

hello_message()
raw_sql = get_sql()
print("Начинаю выполнение запроса...")
result = make_query(raw_sql)
print("Запрос успешно выполнен.")
filename = input("Введите название файла для сохранения результата: ")
str_list = make_str_list(db_result=result)
save_result(str_list=str_list, filename=filename)
print(f"Результаты успешно сохранены в файл '{filename}.txt'")
