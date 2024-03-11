from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from library.views.Author import AuthorView
from library.views.Book import BookView
from library.views.Editorial import EditorialView
from library.views.Loan import LoanView

router = routers.DefaultRouter()
router.register(r'editorial', EditorialView, 'editorial')
router.register(r'author', AuthorView, 'author')
router.register(r'book', BookView, 'book')
router.register(r'loan', LoanView, 'loan')


urlpatterns = [
    path("api/v1/", include(router.urls)),
    path('docs/', include_docs_urls(title='Editorial API')),
    path('docs/', include_docs_urls(title='Author API')),
    path('docs/', include_docs_urls(title='Book API')),
    path('docs/', include_docs_urls(title='Loan API'))]
