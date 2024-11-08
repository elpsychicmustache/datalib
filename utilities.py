# Name: utilities
# Author: ElPsychicMustache
# Created: 2024-11-04

import pandas as pd


def get_df_from_csv(file_path: str, file_name: str, date_columns: list[str], column_names: list[str]) -> pd.DataFrame:
    
    # TODO: Move full_file_path to validate_input
    # making sure user did not forget to add '/' at the end of file path
    if file_path[-1] != '/':
        file_path += '/'

    full_file_path: str = f"{file_path}{file_name}"

    read_csv_kwargs: dict = {}

    if date_columns:
        read_csv_kwargs['parse_dates'] = date_columns
    if column_names:
        read_csv_kwargs['names'] = column_names

    return pd.read_csv(full_file_path, **read_csv_kwargs)


def prompt_selection_for_list(list_of_options: list[str]) -> list[str]:

    selection_list: list[int]
    option_dict: dict[int, str] = {i: list_of_options[i] for i in range(len(list_of_options))}

    for (key, value) in option_dict.items():
        print(f"{key}: {value}")
    
    # TODO: move to validate_input
    user_selection_str = str(input("[*] Please enter the numbers next to each column to use as subsets to find duplicates.\nNumbers should be separated by spaces. Leave blank to select all columns: "))
    if user_selection_str == "":
        user_selection_list = []
    else:
        user_selection_list: list[int] = user_selection_str.split(" ")

    if user_selection_list:
        for selection in user_selection_list:
            selection_list.append(option_dict[selection])
        return selection_list
    else:
        return list(option_dict.values())
    
