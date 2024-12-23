from files import JSON_FILE_PATH, CSV_FILE_PATH
import csv
import json

with open(CSV_FILE_PATH, "r") as file_1:
    books = [a['Title'] for a in csv.DictReader(file_1)]
    print(books)

with open(JSON_FILE_PATH, "r") as file_2:
    data = json.load(file_2)


keys_to_extract = ['name', 'gender', 'age']
extracted_data = [{key: item[key] for key in keys_to_extract if key in item} for item in data]
users = [{"name": user["name"]} for user in data if "name" in user]


books_per_user = len(books) // len(users)
remainder = len(books) % len(users)


book_index = 0
for i, user in enumerate(extracted_data):
    user['books'] = books[book_index:book_index + books_per_user]
    book_index += books_per_user
    if i < remainder:
        user['books'].append(books[book_index])
        book_index += 1

with open('result.json', mode='w') as output_file:
    json.dump(extracted_data, output_file, indent=4, ensure_ascii=False)
