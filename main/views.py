from django.shortcuts import render, HttpResponse
from .models import ToDo

# Create your views here.

def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def third(request):
    return HttpResponse("This is page test3")

def books(request):
    return render(request, 'books.html')

def add_todo(request):
    form = request.POST
    text = form['todo_text']
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)

def add_book(request):
    form = request.POST
    book = Book(
        title = form['title'],
        subtitle = form['subtitle'],
        description = form['description'],
        price = form['price'],
        genre = form['genre'],
        author = form['author'],
        year = form['year'][:10]
    )

    book.save()
    return redirect(books)


def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)
