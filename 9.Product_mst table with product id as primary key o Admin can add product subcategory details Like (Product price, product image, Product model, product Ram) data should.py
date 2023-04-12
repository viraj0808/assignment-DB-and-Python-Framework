'''--Django runs through each URL pattern, in order, and stops at the first one that matches the requested URL, matching against path_info . Once one of the URL patterns matches,
Django imports and calls the given view, which is a Python function (or a class-based view).'''




'''from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('books.urls')),
]'''
