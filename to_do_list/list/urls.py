from django.urls import path
from list import views

urlpatterns = [
    path('lists/<int:list_pk>/', views.lists),
    path('lists/', views.lists),
    path('lists/<int:list_pk>/items', views.lists_items),
    path('lists/<int:list_pk>/items/<int:item_pk>', views.lists_items),
]