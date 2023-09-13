import glob
import os
import re


def task1():
    folder_path = 'test'
    find_name = 'filenames.txt'

    found_files = glob.glob(os.path.join(folder_path, '**', find_name), recursive=True)

    number_of_found_files = len(found_files)

    print(f'Найдено {number_of_found_files} файлов:')
    for file in found_files:
        print(file)


def task2():
    folder_path = 'test'
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    found_emails = []

    file_paths = glob.glob(os.path.join(folder_path, '**', '*'), recursive=True)
    
    for file_path in file_paths:
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                emails = re.findall(email_regex, content)
                found_emails.extend(emails)

    count_email = len(found_emails)

    if found_emails:
        print(f'Найдено {count_email} email адреса :')
        for email in found_emails:
            print(email)
    else:
        print(f"Email-адресов не найдено в файлах в папке '{folder_path}'.")


def main():
    task1()
    task2()
    # дополнительно: придумать над механизмом оптимизации 2-й задачи (параллелизация)


if __name__ == '__main__':
    main()
