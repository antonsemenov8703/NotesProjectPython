import logging
def find_entry(data_find, all_info):
    logging.info(f"Search for an entry: {data_find}")
    candidates = [" ".join(i.values()) for i in all_info if data_find in i.values()]
    if candidates:
        logging.info(f"Search result: {candidates}")
        print(*candidates, sep="\n", end="\n\n")
        return [n[0] for n in candidates]
    else:
        logging.warning(f"No data found: {data_find}")
        print("Note's id or note's date not found.\n")
        return 0

def check_new_data(num):
    # мы принимаем на вход num а именно это будет  header, note, data и дальше проверяем,
    # введенные пользователем значения согласно правилам записи этих столбцов
    # Подумать можно ли сделать проверку более качественной:
    # чтобы проверял header и note на пустоту
    answer = input(f"Enter a {num}: ")
    while True:
        if num == "header":
            if 0 < len(answer) < 30:
                break
        if num == "note":
            if len(answer) > 0:
                break
        answer = input(f"Data is incorrect!\n"
                       f"Header should be no longer than 30 simbols"
                       f"Enter a {num}: ")
    return answer
