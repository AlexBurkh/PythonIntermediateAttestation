from note_manager import note_manager
from console_view import console_view as view
import configparser
import os

main_menu_points = ["1. Вывести записи", "2. Создать запись", "3. Редактировать запись", "4. Удалить запись", "5. Выход"]
modify_menu_points = ["1. Изменить заголовок", "2. Изменить тело", "3. Отмена"]
exit_menu_points = ["1. Выйти и сохранить", "2. Выйти без сохранения", "3. Отмена"]



def read_config():
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read("settings.ini")  # читаем конфиг
    return config

def run(nm):
    status = True

    while(status):
        view.print_list(main_menu_points)

        user_input = view.read_int()
        if user_input == 1:
            print_notes_handler(nm)
        if user_input == 2:
            create_note_handler(nm)
        if user_input == 3:
            modify_note_handler(nm)
        if user_input == 4:
            delete_note_handler(nm)
        if user_input == 5:
            status = exit_handler(nm)

def print_notes_handler(nm):
    view.print_text(nm.get_info())
def create_note_handler(nm):
    title = view.read_text("Введите название")
    body = view.read_text("Введите содержание")
    nm.add_note(title, body)
def modify_note_handler(nm):
    id = view.read_int("Введите id записи")
    if id is not None and id < len(nm.get_notes()) and id >= 0:
        view.print_list(modify_menu_points)
        point = view.read_int()
        if point == 1:
            new_title = view.read_text("Введите новый заголовок")
            nm.modify_note(id, new_title)
        if point == 2:
            new_body = view.read_text("Введите новое тело записи")
            nm.modify_note(id, body = new_body)
    else:
        view.print_text("Некорректный id записи")
def delete_note_handler(nm):
    id = view.read_int("Введите id записи")
    if id is not None and id < len(nm.get_notes()) and id >= 0:
        nm.delete_note(id)
def exit_handler(nm):
    view.print_text("Сохранить результат?")
    view.print_list(exit_menu_points)
    user_input = view.read_int()
    if user_input == 1:
        nm.save_notes()
    if user_input == 3:
        return True
    view.print_text("До свидания!")
    return False

if __name__ == "__main__":
    config = read_config()
    nm = note_manager(config["notes"]["SERIALIZE_PATH"])
    run(nm)
    

