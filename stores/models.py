from django.db import models
from django.urls import reverse
from emarket.settings import AUTH_USER_MODEL


class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stores:store_detail', kwargs={
            'pk': self.id
        })


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    color = models.CharField(max_length=100)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stores:item_detail', kwargs={
            'store_pk': self.store.id,
            'item_pk': self.id
        })
