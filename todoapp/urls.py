from django.urls import path
from . import views

app_name = 'todoapp'  # <-- important for the namespace

urlpatterns = [
    path('', views.index, name='index'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/confirm/', views.delete_confirm, name='delete_confirm'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
