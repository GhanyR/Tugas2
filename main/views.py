from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.template import loader

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
        'items': items, 
        'name': 'Ghany Rasyid Prawira',
        'class': 'PBP C',
        'npm': '2206082392',
        'item_count': items.count(),
    }
    return render(request, 'main/all_items_detail.html', context)

def view_html(request):
    items = Item.objects.all()
    template = loader.get_template('main/view_html.html')
    context = {'items': items}
    return HttpResponse(template.render(context, request))

def view_xml(request):
    items = serializers.serialize('xml', Item.objects.all())
    return HttpResponse(items, content_type='application/xml')

def view_json(request):
    items = serializers.serialize('json', Item.objects.all())
    return JsonResponse(items, safe=False)

def view_xml_id(request, pk):
    item = serializers.serialize('xml', [Item.objects.get(pk=pk)])
    return HttpResponse(item, content_type='application/xml')

def view_json_id(request, pk):
    item = serializers.serialize('json', [Item.objects.get(pk=pk)])
    return JsonResponse(item, safe=False)

