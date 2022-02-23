from django.shortcuts import render
from .models import Order
from cms.models import CmsSlider
from price.models import PriceTable, PriceCard


def index(requests):
    pt = PriceTable.objects.all()
    slider_list = CmsSlider.objects.all()
    return render(requests, "./index.html", {'slider_list': slider_list, 'pt': pt})


def thanks(requests):
    if requests.GET:
        name = requests.GET['name']
        phone = requests.GET['phone']
        element = Order(order_name=name, order_phone=phone)
        element.save()
        return render(requests, "./thansk.html", {'name': name,
                                                  'phone': phone},
                      )
    else:
        return render(requests, "./thansk.html")