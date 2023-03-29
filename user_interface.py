from err_check import check_new_data
from work import *
from datetime import date


def menu():
    while True:
        read_all()
        print(f"\nWelcome to Notes\n{'*' * 20}\n")
        actions = input("1. Show all notes\n"
                        "2. Find note\n" 
                        "3. Add note\n"
                        "4. Edit note\n"
                        "5. Delete note\n"
                        "6. Exit\n")
        match actions:
            case "1":
                chose_output_method = input("1. Show all by number\n"
                                            "2. Show all by date\n")
                match chose_output_method:
                    case "1":
                        show_by_num()
                    case "2":
                        show_by_date()
# может сделать сорт по date вместо id - как реализован сорт по id - его у меня нет, тут просто по порядку идёт

            case "2":
                chose_serch_method = (input("1. Find by number\n"
                                            "2. Find by date\n"))
                match chose_serch_method:
                    case "1":
                        # find_by_number()
                        find_entry(input("Enter note's id: "), read_all())
                        # return
                    case "2":
                        find_by_date()
                        # return
            case "3":
                add_entry(add_menu())
            case "4":
                show_by_num()
                id_change = input(f"Enter the id: ")
                if find_entry(id_change, read_all()) and (answer := edit_menu()):
                    edit_entry(answer, id_change)
            case "5":
                show_by_num()
                del_entry(input("Enter note's id or note's date: "))
            case "6":
                logging.info("Stop program.\n")
                print("Bye!")
                break
            case _:
                logging.warning(f"Main menu, wrong item selected.")
                print("The data is not recognized, repeat the input.")

def add_menu():
    print("UI add_menu")

    # тут мы в логер отдаём команду что включили меню add
    # далее создаём словарь (dictionary) куда записываем все столбцы нашей базы данных в ключи, а
    # значение оставляем пустыми
    #
    logging.info('Start add menu')
    add_dict = {"id": "1", "header": "", "note": "", "date": ""}
    for i in add_dict:
        if i != "id" and i != "date":
            add_dict[i] = check_new_data(i)
    # current_date = date.today()
    # add_dict[date] = current_date
    logging.info('Stop edit menu')
    return add_dict

def edit_menu():
    add_dict = {"1": "header", "2": "note"}
    logging.info('Start edit menu')
    while True:
        print("\nChanging:")
        change = input("1. header\n"
                       "2. note\n"                     
                       "3. exit\n")
        match change:
            case "1" | "2":
                type_date = add_dict[change]
                return type_date, check_new_data(type_date)
            case "3":
                logging.info('Exited the edit menu')
                return 0
            case _:
                logging.warning(f"Edit menu, wrong item selected.")
                print("The data is not recognized, repeat the input.")
