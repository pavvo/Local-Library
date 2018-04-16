from django.shortcuts import render
from django.views import generic
from .models import Book, Author, BookInstance, Genre

# Create your views here.
def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    num_genres=Genre.objects.all().count()

    # particular_book=Book.objects.filter(summary__icontains="Tolkien")

    # Available books (status = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # The 'all()' is implied by default.
    
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context={'num_books': num_books,
                                                  'num_instances': num_instances,
                                                  'num_instances_available': num_instances_available,
                                                  'num_authors': num_authors,
                                                  'num_genres': num_genres,
                                                  # 'particular_book': particular_book,
    }
    )

class BookListView(generic.ListView):
    model = Book
    # paginate_by = 2

class BookDetailView(generic.DetailView):
    model = Book