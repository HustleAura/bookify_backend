import pickle
import difflib

book_list = pickle.load(open('book_list.pkl', 'rb'))
cosine_similarity_matrix = pickle.load(open('similarity_matrix.pkl', 'rb'))

class RecommenderClass:

    def recommender(self, book_title):
        # getting the closest matching book title with the given input. Helps incase there is any mistake in spelling
        book_title = difflib.get_close_matches(book_title, book_list['book_title'], 1)[0]

        # finding the index of the book from the bookList and taking out its similarity with other books from similarity matrix
        index = book_list[book_list['book_title'] == book_title]['index'].values[0]
        similar_books = list(enumerate(cosine_similarity_matrix[index]))

        # sorting the books in descending order. The most similar book is recommended first
        sorted_similar_books = sorted(similar_books, key=lambda x: x[1], reverse=True)

        # taking index from sorted list and adding respective book title in the same order to return list of recommended books
        recommended_books = []
        for book in sorted_similar_books:
            recommended_books.append(book_list['book_title'][book[0]])

        return recommended_books

    # utility functions for using the recommendation algorithm in various ways
    def user_recommendation(self, book_title):
        return self.recommender(book_title)[1:4]

    def search_recommendation(self, book_title):
        return self.recommender(book_title)[0:18]