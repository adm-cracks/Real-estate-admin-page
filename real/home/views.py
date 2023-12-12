from django.shortcuts import render,redirect
from django.http.response import JsonResponse
from django.contrib.auth.models import auth,User
from django.contrib.auth.decorators import login_required
from django.db.models.query_utils import Q
from .models import *


# Create your views here.


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        pas = request.POST['password']

        try:
            user_ = User.objects.get(email=email)
            valid = auth.authenticate(username = user_.username,password = pas)
            u = User.objects.get(is_superuser=user_.is_superuser)
            print(u.is_superuser)
            if valid is not None and  u.is_superuser == True: 
                auth.login(request,valid)
                return JsonResponse(
                {'success' : True},
                safe= False
                )
            
                
        except:
            print("except")
            return JsonResponse(
                {'success' : False,'msg':'Invalid user or password'},
                safe= False
                )  
    else:
        return render(request,'login.html')
    


@login_required(login_url="/")

def adm(request):
    pro = Property.objects.all()
    user = Tenant.objects.all()
    return render(request,'admin.html',{'pro':pro,'user':user})   

#@login_required(login_url="/")
def search(request):
    type = request.POST['type']
    price = request.POST['price']
    print(type,price)
    pro = units.objects.filter(unit_type=type,rent_cost__lte = price)
    return render(request,'main.html',{'pro':pro,'s':f"{type} {price}"})





def property_view(request):
    id=request.GET['xnt']
    pro = Property.objects.get(id=id)
    return render(request,'pro_details.html',{'pro':pro})



def user_view(request):
    id= request.GET.get('cvt')
    try: 
        user = Tenant.objects.get(id=id)
        return render(request,'profile.html',{'us':user})
    except:
        return redirect('/')


def logout(request):
    auth.logout(request)
    return  render(request,'login.html')



def search_auto(request):
  if 'term' in request.GET:
    h = request.GET['term']
    print(h)
    l = Property.objects.filter(Q(name__contains=h))
    dot = []
    for i in l:
      dot.append(i.name)
    return JsonResponse(dot,safe = False)
  return redirect('/')


def search2(request):
  k = request.POST['ser']
  if Property.objects.filter(name=k):
    d = Property.objects.get(name=k)
    print(d)
    return render(request,'pro_details.html',{'pro':d})
  else:
    z = "Property not found "
    return render(request, 'pro_details.html',{'msg':z})