from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import products
from django.utils import timezone
# Create your views here.
@login_required
def create(request):
    if request.method =='POST':
        if(request.POST['title'] and request.POST['body'] and request.POST['url']):
            prod = products()
            prod.title = request.POST['title']
            prod.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                prod.url = request.POST['url']
            else:
                prod.url = 'http://' + request.POST['url']
            prod.icon = request.FILES['icon']
            prod.image = request.FILES['image']
            prod.pub_date = timezone.datetime.now()
            prod.hunter = request.user
            prod.save()
            return redirect('home')
        else:
            return render(request,'create.html',{'error':'all fields required'})    
    else:
        return render(request,'create.html')

def all(request):
    x = request.user
    li=[]
    product = products.objects
    for prod in product.all() :
        if x == prod.hunter:
            li.append(prod)

    return render(request,'all.html',{'products':li},)