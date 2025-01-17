from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Borrower(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    is_borrowed = models.BooleanField(default=False)
    borrower = models.ForeignKey(
        'Borrower', on_delete=models.SET_NULL, null=True, blank=True, related_name='borrowed_books'
    )
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True, blank=True, related_name='books'
    )

    def __str__(self):
        return self.title

