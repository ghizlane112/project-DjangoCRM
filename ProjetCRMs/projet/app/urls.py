#app/urls


from django.urls import path
from . import views

urlpatterns = [
    path('/', views.one, name='one'),
   
]
