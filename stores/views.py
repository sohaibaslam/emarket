from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from . import models
from . import forms


def stores_view(request):
    stores = models.Store.objects.all()
    return render(request, 'stores/stores.html', {'stores': stores})


def store_detail(request, pk):
    store = models.Store.objects.get(pk=pk)
    return render(request, 'stores/store_detail.html', {'store': store})


def item_detial(request, store_pk, item_pk):
    item = models.Item.objects.get(store_id=store_pk, pk=item_pk)
    return render(request, 'stores/item_detail.html', {'item': item, 'store_pk':store_pk})


@login_required
def store_create(request, pk=None):
    store = get_object_or_404(models.Store, pk=pk) if pk else None
    form = forms.StoreForm(instance=store) if store else forms.StoreForm()

    if request.method == 'POST':
        form = forms.StoreForm(request.POST, instance=store)

        if form.is_valid():
            store = form.save()
            return HttpResponseRedirect(store.get_absolute_url())

    return render(request, 'stores/store_form.html', {'form': form})


@login_required
def item_create(request, store_pk, item_pk=None):
    store = get_object_or_404(models.Store, pk=store_pk)
    item = get_object_or_404(models.Item, pk=item_pk) if item_pk else None
    form = forms.ItemForm(instance=item) if item else forms.ItemForm()

    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)

        if form.is_valid():
            item = form.save(commit=False)
            item.store = store
            item.save()

            return HttpResponseRedirect(item.get_absolute_url())

    return render(request, 'stores/store_form.html', {'form': form, 'store': store})


class StoreListView(ListView):
    context_object_name = 'stores'
    model = models.Store
    template_name = 'stores/stores.html'


class StoreDetailView(DetailView):
    context_object_name = 'store'
    model = models.Store
    template_name = 'stores/store_detail.html'


class CreateStoreView(CreateView):
    model = models.Store
    fields = ('name', 'location')


class UpdateStoreView(UpdateView):
    model = models.Store
    fields = ('name', 'location')


class DeleteStoreView(DeleteView):
    model = models.Store
    success_url = reverse_lazy('stores:all_stores')
    template_name = 'stores/store_confirm_delete.html'
