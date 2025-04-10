from django.db import models

class Author(models.Model):
    """
    Represents a book author.
    Fields:
        - name: Name of the author.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Represents a book.
    Fields:
        - title: Title of the book.
        - publication_year: Year the book was published.
        - author: ForeignKey to Author, indicating the book's author.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
