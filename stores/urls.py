from django.urls import path, re_path

from . import views


app_name = 'stores'
urlpatterns = [
    path('', views.StoreListView.as_view(), name='all_stores'),
    re_path(r'(?P<store_pk>\d+)/item/(?P<item_pk>\d+)$',
            views.item_detial, name='item_detail'),
    re_path(r'^(?P<pk>\d+)$', views.StoreDetailView.as_view(), name='store_detail'),
    re_path(r'^update_store/(?P<pk>\d+)$', views.UpdateStoreView.as_view(), name='edit_store'),
    re_path(r'^add_store/$', views.CreateStoreView.as_view(), name='add_store'),
    re_path(r'^delete_store/(?P<pk>\d+)$', views.DeleteStoreView.as_view(), name='delete_store'),
    re_path(r'^item_form/(?P<store_pk>\d+)/(?P<item_pk>\d+)$', views.item_create, name='edit_item'),
    re_path(r'^item_form/(?P<store_pk>\d+)$', views.item_create, name='add_item'),
]
