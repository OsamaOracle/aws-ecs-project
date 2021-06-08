from django.shortcuts import render
from .models import Item


# Create your views here.

def index(request):
    # item1 = Item()
    # item1.name = 'Man T -shirt'
    # item1.price = '60'
    # item1.image_url = 'tshirt-img.png'
    #
    # item2 = Item()
    # item2.name = 'Man -shirt'
    # item2.price = '30'
    # item2.image_url = 'dress-shirt-img.png'
    #
    # item3 = Item()
    # item3.name = 'Woman Scart'
    # item3.price = '30'
    # item3.image_url = 'women-clothes-img.png'

    # items=[item1,item2,item3]

    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})
