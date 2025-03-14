from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

@permission_required("bookshelf.can_create", raise_exception=True)
def book_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        published_date = request.POST.get("published_date")
        description = request.POST.get("description")
        Book.objects.create(title=title, author=author, published_date=published_date, description=description)
        return redirect("book_list")
    return render(request, "bookshelf/book_form.html")

@permission_required("bookshelf.can_edit", raise_exception=True)
def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.published_date = request.POST.get("published_date")
        book.description = request.POST.get("description")
        book.save()
        return redirect("book_list")
    return render(request, "bookshelf/book_form.html", {"book": book})

@permission_required("bookshelf.can_delete", raise_exception=True)
def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "bookshelf/book_confirm_delete.html", {"book": book})


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book
from .forms import ExampleForm  # Use Django forms to validate input

@login_required
@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    query = request.GET.get("q")
    if query:
        books = Book.objects.filter(title__icontains=query)  # Prevents SQL injection
    else:
        books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

@login_required
@permission_required("bookshelf.can_create", raise_exception=True)
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "bookshelf/book_form.html", {"form": form})

@login_required
@permission_required("bookshelf.can_edit", raise_exception=True)
def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)
    return render(request, "bookshelf/book_form.html", {"form": form, "book": book})






from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book
from .forms import ExampleForm  # Use Django forms to validate input

@login_required
@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    query = request.GET.get("q")
    if query:
        books = Book.objects.filter(title__icontains=query)  # Prevents SQL injection
    else:
        books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

@login_required
@permission_required("bookshelf.can_create", raise_exception=True)
def book_create(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = ExampleForm()
    return render(request, "bookshelf/book_form.html", {"form": form})

@login_required
@permission_required("bookshelf.can_edit", raise_exception=True)
def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = ExampleForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = ExampleForm(instance=book)
    return render(request, "bookshelf/book_form.html", {"form": form, "book": book})
