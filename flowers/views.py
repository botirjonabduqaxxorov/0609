from django.shortcuts import render, get_object_or_404
from .models import Type, Flower
from django.shortcuts import render

def home(request):
    return render(request, 'flowers/home.html')


def all_flowers(request):
    flowers = Flower.objects.all()
    return render(request, 'flowers/all_flowers.html', {'flowers': flowers})

def flowers_by_type(request, type_id):
    flowers = Flower.objects.filter(type_id=type_id)
    flower_type = get_object_or_404(Type, pk=type_id)
    return render(request, 'flowers/flowers_by_type.html', {'flowers': flowers, 'flower_type': flower_type})

def flower_detail(request, pk):
    flower = get_object_or_404(Flower, pk=pk)
    return render(request, 'flowers/flower_detail.html', {'flower': flower})

def list_types(request):
    types = Type.objects.all()
    return render(request, 'flowers/list_types.html', {'types': types})
