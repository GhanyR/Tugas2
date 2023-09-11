from django.urls import path
from . import views
from .views import add_item, remove_item

urlpatterns = [
    path('', views.index, name='index'),
    path('add_item/', add_item, name='add_item'),
    path('remove_item/<int:pk>/', remove_item, name='remove_item'),
    path('item_detail/', views.all_items_detail, name='all_items_detail'),
    path('item_detail/<int:pk>/', views.item_detail, name='item_detail'),
]