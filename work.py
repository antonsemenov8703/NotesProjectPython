from os import path
import csv
import pandas as pd
from err_check import find_entry
from logg import logging
from datetime import date

all_data = {}
last_id = 0
name_db = "Notes.csv"
name_sorted_db = "sorted_Notes.csv"

def read_all():
    global all_data, last_id

    logging.info(f"Show all entries. Database File - {name_db}")
    if path.exists(name_db):
        with open(name_db, "r", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)
            all_data = [i for i in csv_reader]
            last_id = all_data[-1]["id"]
            return all_data
    else:
        logging.warning(f"The database is not connected! Missing database file.")
        print("The database is not connected!")

def add_entry(data):
    global last_id
    logging.info(f"Adding a new note: {data}")
    last_id = int(last_id) + 1
    data["id"] = last_id
    data["date"] = date.today()

    with open(name_db, "a", encoding="utf-8", newline="") as file:
        fieldnames = ["id", "header", "note", "date"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(data)
        logging.warning(f"Data added to the list: {data.values()}")
        print("Data added to the list")

def del_entry(data_del):
    global all_data

    logging.info(f"Deleting a note: {data_del}")
    id_cand = find_entry(data_del, all_data)
    if id_cand:
        id_del = input(f"Enter note's id to delete: ")
        logging.info(f"Id selected: {id_del}")

        if id_del in id_cand:
            all_data = [k for k in all_data if k["id"] != id_del]
            with open(name_db, "w", encoding="utf-8", newline="") as file:
                fieldnames = ["id", "header", "note", "date"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(all_data)
                logging.info(f"Note deleted")
                print("Note deleted\n")
        else:
            logging.warning(f"No data found: {data_del}")
            print("Id not found.\n")
    else:
        logging.warning(f"No data found: {data_del}")

def edit_entry(data_change, id_change):
    global all_data
    key, value = data_change

    logging.info(f"Data changes: {data_change}")
    if find_entry(id_change, all_data):
        for i, v in enumerate(all_data):
            if v["id"] == id_change:
                logging.info(f"Current value: {v[key]}")
                v[key] = value
                v["date"] = date.today()
                logging.info(f"New value: {v[key]}")
                all_data[i] = v

        with open(name_db, "w", encoding="utf-8", newline="") as file:
            fieldnames = ["id", "header", "note", "date"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(all_data)
            logging.info(f"Data changed")
            print("Data changed\n")
    else:
        logging.warning(f"No data found: {data_change}")
        print("Id not found.\n")

def show_by_num():
    for_output = [" ".join(k.values()) for k in all_data]
    print(*for_output, sep="\n", end=f"\n{'-' * 20}\n\n")

def show_by_date():

    df = pd.read_csv(name_db)
    sorted_df = df.sort_values(by='date')
    sorted_df.to_csv(name_sorted_db, index=False)

    if path.exists(name_sorted_db):
        with open(name_sorted_db, "r", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)
            all_sorted_data = [i for i in csv_reader]
    else:
        logging.warning(f"The database is not connected! Missing database file.")
        print("The database is not connected!")

    for_output = [" ".join(k.values()) for k in all_sorted_data]
    print(*for_output, sep="\n", end=f"\n{'-' * 20}\n\n")

