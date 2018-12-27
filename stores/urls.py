from django.urls import path, re_path

from . import views


app_name = 'stores'
urlpatterns = [
    path('', views.stores_view, name='all_stores'),
    re_path(r'(?P<store_pk>\d+)/item/(?P<item_pk>\d+)$',
            views.item_detial, name='item_detail'),
    re_path(r'^(?P<pk>\d+)$', views.store_detail, name='store_detail'),
    re_path(r'^store_form/(?P<pk>\d+)$', views.store_create, name='edit_store'),
    re_path(r'^store_form/$', views.store_create, name='add_store'),
    re_path(r'^item_form/(?P<store_pk>\d+)/(?P<item_pk>\d+)$', views.item_create, name='edit_item'),
    re_path(r'^item_form/(?P<store_pk>\d+)$', views.item_create, name='add_item'),
]
