from django.contrib import admin

from library.models.Author import Author
from library.models.Book import Book
from library.models.Editorial import Editorial
from library.models.Loan import Loan

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Editorial)
admin.site.register(Loan)
