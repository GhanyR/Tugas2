from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import json
from main.models import Item

def item_detail(request, pk):
    item = Item.objects.get(pk=pk)
    return render(request, 'main/item_detail.html', {'item': item})

def index(request):
    return render(request, 'main/index.html')

def add_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
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

@login_required(login_url='/login')
def all_items_detail(request):
    items = Item.objects.filter(user=request.user)
    context = {
        'items': items, 
        'name': request.user.username,
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

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('login')
    
    context = {'form':form}
    return render(request, 'main/register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            user.last_login = timezone.now()
            user.save(update_fields=['last_login'])
            return redirect('all_items_detail')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'main/login.html', context)
  
def logout_user(request):
    logout(request)
    return redirect('login')

def add_quantity(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.amount += 1
    item.save()
    return redirect('all_items_detail')

def remove_quantity(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.amount -= 1
    item.save()
    return redirect('all_items_detail')

def get_all_items(request):
    items = Item.objects.filter(user=request.user)
    data = serializers.serialize('json', items)
    return JsonResponse(data, safe=False)

def create_item_ajax(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False, "errors": form.errors})

def delete_item_ajax(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'DELETE':
        item.delete()
        return JsonResponse({"success": True})
    return JsonResponse({"success": False})

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Item.objects.create(
            user = request.user,
            name = data["name"],
            category = data["category"],
            amount = int(data["amount"]),
            power = int(data["power"]),
            price = int(data["price"]),
            description = data["description"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)