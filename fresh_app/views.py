import datetime

from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView

from fresh_app.models import Author, Book


class IndexListView(TemplateView):
    template_name = 'main/index.html'


def index(request):
    name = 'hi yoko'
    num_list = []
    dt = datetime.datetime.now()
    return render(request, 'main/indexx.html', {'name': name,
                                                'num_list': num_list,
                                                'dt': dt})


# def get_author(request, pk):
#     author = Author.objects.filter(fio__startswith=pk)
#     return render(request, 'main/author.html', {'author': author})

class AuthorListView(ListView):
    template_name = 'main/author_list.html'
    model = Author
    context_object_name = 'authors'

    def get_queryset(self):
        fio_start = self.kwargs.get('fio_start')
        if fio_start:
            return Author.objects.filter(fio__startswith=fio_start)
        return Author.objects.all()


# def get_book(request):
#     book_name = request.GET.get('book')
#     book = Book.objects.filter(name__icontains=book_name)
#     return render(request, 'main/book.html', {'book': book})
#
#
# def get_book_by_page(request, min, max):
#     book = Book.objects.filter(num_pages__gte=min, num_pages__lte=max)
#     return render(request, 'main/book.html', {'book_page_range': book})
#
#
# def get_book_by_title_descr(request, book):
#     book = Book.objects.filter(Q(name__icontains=book) | Q(description__icontains=book))
#     return render(request, 'main/book.html', {'get_by_title_descr': book})
#
#
# def get_book_by_author_name(request, str):
#     book = Book.objects.filter(author_fio__icontains=str)
#     return render(request, 'main/book.html', {'author_fio': book})
# def get_author_by_id(request, pk):
#     author = Author.objects.get(id=pk)
#     books = author.book_set.all()
#     return render(request, 'main/author.html', {'author': author})


class BookListView(ListView):
    template_name = 'main/book_list.html'
    model = Book
    context_object_name = 'books'

    def get_queryset(self):
        name = self.kwargs.get('name')
        start = self.kwargs.get('start')
        end = self.kwargs.get('end')
        query = self.kwargs.get('query')
        author_query = self.kwargs.get('author_query')

        if name:
            return Book.objects.filter(name__icontains=name)
        elif start and end:
            return Book.objects.filter(num_pages__gte=start, num_pages__lte=end)
        elif query:
            return Book.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        elif author_query:
            return Book.objects.filter(author__fio__icontains=author_query)
        return Book.objects.all()


class AuthorDetailView(DetailView):
    queryset = Author.objects.prefetch_related('book_set')
    template_name = 'main/author_detail.html'
    model = Author
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.book_set.all()
        return context