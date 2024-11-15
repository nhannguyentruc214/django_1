from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    nationality = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    published_year = models.PositiveIntegerField()
    authors = models.ManyToManyField(Author, related_name='books')

    def __str__(self):
        return self.title

class Borrower(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class LoanHistory(models.Model):
    borrow_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='loan_histories')
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE, related_name='loan_histories')

    def __str__(self):
        return f"Loan {self.pk}: {self.borrower.name} - {self.book.title}"
