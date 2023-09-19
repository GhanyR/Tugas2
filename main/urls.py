from django.urls import path
from . import views
from .views import add_item, remove_item

urlpatterns = [
    path('add_item/', add_item, name='add_item'),
    path('remove_item/<int:pk>/', remove_item, name='remove_item'),
    path('', views.all_items_detail, name='all_items_detail'),
    path('item_detail/<int:pk>/', views.item_detail, name='item_detail'),
    path('view_html/', views.view_html, name='view_html'),
    path('view_xml/', views.view_xml, name='view_xml'),
    path('view_json/', views.view_json, name='view_json'),
    path('view_xml_id/<int:pk>/', views.view_xml_id, name='view_xml_id'),
    path('view_json_id/<int:pk>/', views.view_json_id, name='view_json_id'),
]
    