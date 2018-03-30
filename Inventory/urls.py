from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'inventory'
urlpatterns = [
    path(
        '',
        HomeView.as_view(),
        name="home"
    ),
    path(
        'new-product',
        new_product,
        name="new-product"
    ),
    path(
        'delete',
        delete,
        name="delete"
    ),
    path(
        'add',
        add,
        name="add"
    ),
    path(
        'sub',
        sub,
        name="sub"
    ),
]
