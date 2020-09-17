from .views import home, new_search
from django.urls import path

urlpatterns=[
	path('',home,name='home'),
	path('new_search',new_search,name='new_search')
]