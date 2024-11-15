from django.contrib import admin
from .models import Author, Book, Borrower, LoanHistory

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'nationality', 'birth_date')
    search_fields = ('name', 'nationality')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn', 'publisher', 'published_year')
    search_fields = ('title', 'isbn')
    list_filter = ('published_year',)
    filter_horizontal = ('authors',)  # Makes it easier to manage ManyToMany relationships

@admin.register(Borrower)
class BorrowerAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_info', 'address')
    search_fields = ('name', 'contact_info')

@admin.register(LoanHistory)
class LoanHistoryAdmin(admin.ModelAdmin):
    list_display = ('borrow_date', 'return_date', 'book', 'borrower')
    search_fields = ('book__title', 'borrower__name')
    list_filter = ('borrow_date', 'return_date')
