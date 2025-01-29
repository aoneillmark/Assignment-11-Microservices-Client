from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

books_api = 'http://flask-books-app-mark.ascqdbbyaugdbqd4.uksouth.azurecontainer.io:5000/'

@app.route('/')
def get_json():
    r = requests.get(books_api)
    return r.json()

@app.route('/books')
def get_books():
    r = requests.get(books_api)
    books = r.json()
    genre_filter = request.args.get('genre')

    filters = {key: value.lower() for key, value in request.args.items()}


    def matches(book):
        for key, value in filters.items():
            if key in book:
                if isinstance(book[key], str):
                    if value not in book[key].lower():
                        return False
                else:
                    if str(book[key]) != value:
                        return False
        return True

    filtered_books = [book for book in books if matches(book)]

    return jsonify(filtered_books)


if __name__ == '__main__':
    app.run()