from django.urls import path

from . import views

app_name = 'items'

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('<int:item_id>', views.item_view, name='item_view'),
    path('new', views.item_create, name='item_new'),
    path('edit/<int:item_id>', views.item_update, name='item_edit'),
    path('delete/<int:item_id>', views.item_delete, name='item_delete'),
]