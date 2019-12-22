from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/search/word=<word>res=<limit>', views.search_view, name='search_view')
]
