import csv
import json
from files import JSON_FILE_PATH, CSV_FILE_PATH


# Функция для чтения CSV-файла и преобразования его в список книг
def read_books_from_csv(csv_file_path):
    with open(csv_file_path, "r") as file:
        return [row for row in csv.DictReader(file)]


# Функция для чтения JSON-файла и преобразования его в структуру данных
def read_data_from_json(json_file_path):
    with open(json_file_path, "r") as file:
        return json.load(file)


# Функция для извлечения нужных данных пользователей из JSON
def extract_user_data(data, keys_to_extract):
    return [
        {key: user[key] for key in keys_to_extract if key in user}
        for user in data
    ]


# Функция для распределения книг между пользователями
def distribute_books(books, users, books_per_user, remainder):
    book_index = 0
    for i, user in enumerate(users):
        user['books'] = []

        # Добавляем книги пользователю
        for _ in range(books_per_user):
            if book_index < len(books):
                book = books[book_index]
                user['books'].append({
                    'title': book.get('Title'),
                    'author': book.get('Author'),
                    'pages': book.get('Pages'),
                    'genre': book.get('Genre')
                })
                book_index += 1

        # Если остались книги, добавляем их пользователям с остатком
        if i < remainder:
            if book_index < len(books):
                book = books[book_index]
                user['books'].append({
                    'title': book.get('Title'),
                    'author': book.get('Author'),
                    'pages': book.get('Pages'),
                    'genre': book.get('Genre')
                })
                book_index += 1


# Функция для записи данных в JSON файл
def write_result_to_json(output_file_path, data):
    with open(output_file_path, mode='w') as output_file:
        json.dump(data, output_file, indent=4, ensure_ascii=False)


# Основная функция
def main():
    # 1. Чтение данных
    books = read_books_from_csv(CSV_FILE_PATH)
    data = read_data_from_json(JSON_FILE_PATH)

    # 2. Извлечение нужных данных пользователей
    keys_to_extract_users = ['name', 'gender', 'age']
    extracted_data = extract_user_data(data, keys_to_extract_users)

    # 3. Распределение книг по пользователям
    users = [{"name": user["name"]} for user in data if "name" in user]
    books_per_user = len(books) // len(users)
    remainder = len(books) % len(users)

    distribute_books(books, extracted_data, books_per_user, remainder)

    # 4. Запись результата в файл
    write_result_to_json('result.json', extracted_data)


# Запуск основной функции
main()