import os
import sys
from icecream import ic

def generate_description():
    with open("description.md", "w") as f:
        for root, dirs, files in os.walk("."):
            for file in files:
                if file.endswith(".py") or file == "description.md":
                    file_path = os.path.join(root, file)
                    f.write(f"{file_path}\n")

def get_ignor(current_directory):
    file = os.path.join(current_directory, '.gitignore')
    with open(file=file, mode='r', encoding='utf-8') as f:
        ignor_list = f.readlines()
    ignor_list_clean = []
    for ignor_item in ignor_list:
        if '#' not in ignor_item:
            ignor_item = ignor_item.strip()
            if ignor_item != '':
                if ignor_item[-1] == r'/':
                    ignor_item = ignor_item[:-1]
                if ignor_item[0] == r'.':
                    ignor_item = ignor_item[1:]

                ignor_list_clean.append(ignor_item)
    # ic(ignor_list_clean)
    return ignor_list_clean


def des_creator():
    current_directory = os.getcwd()
    dir_list = os.listdir(current_directory)
    script_name = os.path.basename(sys.argv[0])
    ignor_list = [script_name, ]
    if '.gitignore' in dir_list:
        ignor_list += get_ignor(current_directory)
    ic(ignor_list)
    # for item in dir_list:
    #     if ignor_list != []
    #         if item not in i
    #             item_path = os.path.join()

if __name__ == '__main__':
    des_creator()
