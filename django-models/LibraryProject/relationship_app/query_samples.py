# books = Book.objects.filter(author_id=1)

books = Library.objects.get(name=library_name)
books.all()

author = Author.objects.get(name=author_name)
objects.filter(author=author)

librarian = Librarian.objects.get(name=librarian_name)

books.libraries.add(librarian.library)