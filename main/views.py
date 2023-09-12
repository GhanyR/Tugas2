from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

def item_detail(request, pk):
    item = Item.objects.get(pk=pk)
    return render(request, 'main/item_detail.html', {'item': item})

def index(request):
    return render(request, 'main/index.html')

def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect('all_items_detail')
    else:
        form = ItemForm()
    return render(request, 'main/add_item.html', {'form': form})

def remove_item(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('all_items_detail')
    return render(request, 'main/remove_item.html', {'item': item})


def all_items_detail(request):
    items = Item.objects.all()
    context = {
        'items': items,  # Menggunakan 'items' karena di template Anda menggunakan 'items'
        'name': 'Ghany Rasyid Prawira',
        'class': 'PBP C',
        'npm': '2206082392'
    }
    return render(request, 'main/all_items_detail.html', context)