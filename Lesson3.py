import json
import csv
import random


def r_json():
    with open("files/users.json", "r") as f:
        users = json.loads(f.read())

    custom_users = []
    for user in users:
        user_test = {
            'name': user['name'],
            'gender': user['gender'],
            'address': user['address'],
            'age': user['age'],
            'books': []
        }
        custom_users.append(user_test)
    return custom_users


def r_csv():
    with open("files/books.csv", newline='') as f:
        reader = csv.reader(f)
        header = next(reader)

        books = [dict(zip(header, row)) for row in reader]

    custom_books = []
    for book in books:
        book_test = {
            'title': book['Title'],
            'author': book['Author'],
            'pages': book['Pages'],
            'genre': book['Genre']
        }
        custom_books.append(book_test)
    return custom_books


def share_books(books_list, users_list):
    for _ in range(len(books_list)):
        for user in users_list:
            if len(books_list) == 0:
                return users_list
            random_book = random.choice(books_list)
            user['books'].append(random_book)
            books_list.remove(random_book)
    return users_list


if __name__ == '__main__':
    users = r_json()
    books = r_csv()

    users_list = share_books(books_list=books, users_list=users)

    with open('reference_json', 'w') as reference_json:
        json.dump(users_list, reference_json, indent=4)

print(reference_json)
