from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Book
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse, resolve


from .forms import BookForm

def index(request):
    return render(request, 'Book_logs/index.html')

@login_required
def Books(request):

    Books = Book.objects.filter(owner=request.user).order_by('date_added')

    context={'Books':Books}
    return render(request, 'Book_logs/Books.html',context)

@login_required
def BookDetail(request,Book_id):
    book = Book.objects.get(id=Book_id)
    if book.owner != request.user:
        raise Http404
    entries=book.entry_set.order_by('-date_added')
    context={'book':book,'entries':entries}
    return render(request, 'Book_logs/BookDetail.html',context)

@login_required
def new_Book(request):
    if request.method != 'POST':
        form=BookForm()

    else:
        form=BookForm(request.POST)
        if form.is_valid():



            Book = form.save(commit=False)
            Book.owner = request.user
            Book.save()
            return HttpResponseRedirect(reverse('Book_logs:Books'))






    context={'form':form}
    return render(request, 'Book_logs/new_Book.html',context)

