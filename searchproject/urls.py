from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/search/linq', views.search_view, name='search_view')
    path(r'api/search/word=<word>&numberres=<limit>', views.search_view, name='search_view')
]
