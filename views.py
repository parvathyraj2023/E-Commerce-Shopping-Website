from django.shortcuts import render,redirect
from mainapp.models import categorydb,productdb
from Frontend.models import contactdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def indexpage(request):
    return render(request,"index.html")

def addcategory(request):
    return render(request,"AddCategory.html")
def savecategory(request):
    if request.method == "POST":
        na = request.POST.get('name')
        ds = request.POST.get('description')
        im = request.FILES['image']
        obj = categorydb(Category_name=na,Description=ds, Category_image=im)
        obj.save()
        messages.success(request,"Category added successfully...!")
        return redirect(addcategory)

def displaycategory(request):
    data = categorydb.objects.all()
    return render(request, "DisplayCategory.html", {'data': data})

def editcategory(request,dataid):
    data=categorydb.objects.get(id=dataid)
    return render(request,"EditCategory.html",{'data':data})

def deletedata(request,dataid):
    data=categorydb.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "Category Deleted...!")
    return redirect(displaycategory)

def updatecategory(request,dataid):
    if request.method=="POST":
        na = request.POST.get('name')
        ds = request.POST.get('description')
        try:
            img=request.FILES['image']
            fs= FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=categorydb.objects.get(id=dataid).Category_image
        categorydb.objects.filter(id=dataid).update(Category_name=na,Description=ds,Category_image=file)
        return redirect(displaycategory)

def addproduct(request):
    category=categorydb.objects.all()
    return render(request,"AddProduct.html",{'category':category})

def saveproduct(request):
    if request.method == "POST":
        ca = request.POST.get('category')
        na = request.POST.get('name')
        ds = request.POST.get('description')
        pr = request.POST.get('price')
        im = request.FILES['image']
        obj = productdb(Category=ca,Product_name=na,Description=ds, Price=pr,Category_image=im)
        obj.save()
        messages.success(request, "Product added successfully...!")
        return redirect(addproduct)


def displayproduct(request):
    data = productdb.objects.all()
    return render(request, "DisplayProduct.html", {'data': data})

def editproduct(request,product_id):
    data=categorydb.objects.all()
    product=productdb.objects.get(id=product_id)
    return render(request,"EditProduct.html",{'data':data,'product':product})

def updateproduct(request,product_id):
    if request.method=="POST":
        ca = request.POST.get('category')
        pna = request.POST.get('pname')
        ds = request.POST.get('description')
        pr = request.POST.get('price')
        try:
            img=request.FILES['image']
            fs= FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=productdb.objects.get(id=product_id).Category_image
        productdb.objects.filter(id=product_id).update(Category=ca,Product_name=pna,Description=ds,Price=pr,Category_image=file)
        return redirect(displayproduct)

def deleteproduct(request,dataid):
    data=productdb.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "Product Deleted...!")
    return redirect(displayproduct)

def adminloginpage(request):
    return render(request,"AdminLogin.html")

def adminlogin(request):
    if request.method=="POST":
        un=request.POST.get('user_name')
        pwd=request.POST.get('pass_word')
        if User.objects.filter(username__contains=un).exists():
            x=authenticate(username=un,password=pwd)
            if x is not None:
                login(request,x)
                request.session['username']=un
                request.session['password']=pwd
                return redirect(indexpage)
            else:
                return redirect(adminloginpage)
        else:
            return redirect(adminloginpage)

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(adminloginpage)

def displaycontactdetails(request):
    data=contactdb.objects.all()
    return render(request,"DisplayContactDetails.html",{'data':data})
def deletecontact(request,dataid):
    data=contactdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycontactdetails)

def editcontact(request,dataid):
    data=contactdb.objects.get(id=dataid)
    return render(request,"EditContact.html",{'data':data})

def updatecontact(request,dataid):
    if request.method=="POST":
        fn = request.POST.get('fname')
        ln = request.POST.get('lname')
        nm = request.POST.get('number')
        em = request.POST.get('email')
        ad = request.POST.get('address')
        ci = request.POST.get('city')
        co = request.POST.get('country')
        contactdb.objects.filter(id=dataid).update(Firstname=fn,Lastname=ln,Number=nm,Email=em,Address=ad,City=ci,Country=co)
        return redirect(displaycontactdetails)
