from django.shortcuts import render

# Create your views here.
from django.views import View


class ShopView(View):
    def index(request):
        return render(request, "shop/index.html")