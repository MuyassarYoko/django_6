from django.urls import path

from fresh_app.views import IndexListView, index, AuthorListView, BookListView, AuthorDetailView

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('index/', index, name='indexx'),
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('authors/<str:fio_start>', AuthorListView.as_view()),
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<slug:name>', BookListView.as_view(), name='book-list'),
    path('books/pages/<int:start>/<int:end>', BookListView.as_view(), name='book-list'),
    path('books/title_desc/<slug:query>', BookListView.as_view(), name='book-list'),
    path('books/author/<slug:author_query>', BookListView.as_view(), name='book-list'),
    path('author-detail/<int:pk>', AuthorDetailView.as_view(), name='author-detail'),
]
