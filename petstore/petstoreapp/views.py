from django.shortcuts import render
from petstoreapp.models import Pet
from django.db.models import Q

# Create your views here.
def home(request):
    p=Pet.objects.all()
    context={}
    context['data']=p
    return render(request,'index.html',context)

# def search(request):
#     query=request.GET['query']
    
#     name=Pet.objects.filter(name__icontains=query)
#     gender=Pet.objects.filter(gender__icontains=query)
#     detail=Pet.objects.filter(description__icontains=query)

#     allprod=name.union(gender,detail)
    
#     context={}
#     if allprod.count()==0:
#         context['errmsg']='Not Found'
#     context['data']=allprod
#     return render(request,'index.html',context) 

def catfilter(request,cv):
    p=Pet.objects.filter(gender=cv)
    context={}
    context['data']=p
    return render(request,'index.html',context)

def pricefilter(request):
    min=request.GET['min']
    max=request.GET['max']

    q1=Q(price__gte=min)
    q2=Q(price__lte=max)
    p=Pet.objects.filter(q1 & q2)

    context={}
    context['data']=p
    return render(request,'index.html',context)
