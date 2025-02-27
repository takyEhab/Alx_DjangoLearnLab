# books = Book.objects.filter(author_id=1)

books = Library.objects.get(name=library_name)
books.all()
