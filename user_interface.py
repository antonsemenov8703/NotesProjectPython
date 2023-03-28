from err_check import check_new_data
from work import *

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
# продумать реализацию by date , чтобы во первых автоматически проставлялась дата и как сделать сортировку???
# может сделать сорт по date вместо id - как реализован сорт по id - его у меня нет, тут просто по порядку идёт


    #         функционал по поиску по id должен быть в проге
    # нужно найти как выставлять дату



            case "2":
                chose_serch_method = (input("1. Find by number\n"
                                            "2. Find by date\n"), read_all())
                match chose_serch_method:
                    case "1":
                        find_by_number()
                        return
                    case "2":
                        find_by_date()
                        return
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
    # тут мы в логер отдаём команду что включили меню add
    # далее создаём словарь (dictionary) куда записываем все столбцы нашей базы данных в ключи, а
    # значение оставляем пустыми
    #
    # Тут нужно изменить чтобы столбцы были id, header, note, date
    logging.info('Start add menu')
    # add_dict = {"id": "1", "name": "", "surname": "", "phone": "", "birth year": "", "experience since": ""}
    add_dict = {"id": "1", "header": "", "note": "", "date": ""}
    for i in add_dict:
        if i != "id" and i != "date":
            add_dict[i] = check_new_data(i)
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
