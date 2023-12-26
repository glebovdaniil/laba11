from django.shortcuts import render
from .models import velocity
def prodview(request):
    vels = velocity.objects.all()
    return render(request, 'prod/product.html', {'vels':vels})