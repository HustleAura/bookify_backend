import os
import pickle
from flask import Flask, request, jsonify
from recommender_class import RecommenderClass

app = Flask('__name__')
recommender_object = RecommenderClass()

book_list = pickle.load(open('book_list.pkl', 'rb'))


@app.route('/')
def home():
    return 'Welcome to bookify backend. Go to https://github.com/HustleAura/Bookify to use Bookify'


@app.route('/user', methods=['POST'])
def user():
    book_title = request.form.get('book_title')
    try:
        result = recommender_object.user_recommendation(book_title)
    except:
        return jsonify({'recommended_books': 'no result found'})
    else:
        return jsonify({'recommended_books': result})


@app.route('/search', methods=['POST'])
def search():
    book_title = request.form.get('book_title')
    try:
        result = recommender_object.search_recommendation(book_title)
    except:
        return jsonify({'recommended_books': 'no result found'})
    else:
        return jsonify({'recommended_books': result})


@app.route('/image_url', methods=['POST'])
def image_url():
    book_title = request.form.get('book_title')
    if book_title == 'no result found':
        return jsonify({'image_url': 'no result found'})
    else:
        imager = book_list[book_list['book_title'] == book_title]['img_s']
        image = imager.to_json()
        return jsonify({'image_url': image})


if __name__ == '__main__':
    port = os.environ.get("PORT", 5000)
    app.run(debug=False, host="0.0.0.0", port=port)
