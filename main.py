from note_manager import note_manager
from console_view import console_view as view
import configparser
import os

main_menu_points = ["1. Вывести записи", "2. Создать запись", "3. Редактировать запись", "4. Удалить запись", "5. Выход"]



def read_config():
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read("settings.ini")  # читаем конфиг
    return config

def run(nm):
    status = True

    while(status):
        view.print_text(nm.get_text())
        view.print_list(main_menu_points)

        user_input = view.read_int()
        if user_input == 1:
            print_notes(nm.get_text())
        if user_input == 2:
            create_note_handler(nm)
        if user_input == 3:
            pass
        if user_input == 4:
            pass
        if user_input == 5:
            view.print_text("До свидания!")
            status = False          

def create_note_handler(nm):
    title = view.read_text("Введите название: ")
    body = view.read_text("Введите содержание: ")
    nm.add_note(title, body)

def print_notes(nm):
    view.print_text(nm)
def create_note():
    view.print_text("")

if __name__ == "__main__":
    config = read_config()
    print(os.getcwd())
    nm = note_manager(config["notes"]["SERIALIZE_PATH"])
    run(nm)
    

