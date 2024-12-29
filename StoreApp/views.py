from django.shortcuts import render, redirect
from LatestApp.models import CategoryDB, ProductDB
from StoreApp.models import SignupDB, CartDB
from django.contrib import messages


def home(req):
    cat = CategoryDB.objects.all()
    return render(req, "home.html", {'cat': cat})


def products(req):
    cat = CategoryDB.objects.all
    return render(req, "products.html", {'cat': cat})


def products_filtered(req, pro_id):
    pro = ProductDB.objects.filter(Product_Category=pro_id)
    return render(req, "products_filtered.html", {'pro': pro})


def single_product(req, pro_id):
    pro = ProductDB.objects.get(id=pro_id)
    return render(req, "single_product.html", {'pro': pro})


def sign_up(req):
    return render(req, "sign_up.html")


def sign_in(req):
    return render(req, "sign_in.html")


def save_signup(req):
    if req.method == "POST":
        username = req.POST.get('username')
        email = req.POST.get('email')
        mobile = req.POST.get('mobile')
        password = req.POST.get('password')
        confirm_password = req.POST.get('confirm_password')
        obj = SignupDB(Signup_Name=username,
                       Signup_Email=email,
                       Signup_Contact=mobile,
                       Signup_Password=password,
                       Signup_ConfirmPassword=confirm_password,
                       )
        obj.save()
        return redirect(sign_in)


def user_login(request):
    if request.method == "POST":
        un = request.POST.get('user')
        pw = request.POST.get('pass')
        if SignupDB.objects.filter(Signup_Name=un, Signup_Password=pw).exists():
            request.session['Signup_Name'] = un
            request.session['Signup_Password'] = pw
            return redirect(home)
        else:
            return redirect(sign_in)
    else:
        return redirect(sign_in)


def user_logout(request):
    del request.session['Signup_Name']
    del request.session['Signup_Password']
    return redirect(home)


def contact(req):
    return render(req, "contact.html")


def cart(request):
    carts = CartDB.objects.filter(Username=request.session['Signup_Name'])
    x = carts.count()
    subtotal = 0
    shipping_charge = 0
    total = 0
    for i in carts:
        subtotal += i.Total_Price
        if subtotal > 200000:
            shipping_charge = 4000
        else:
            shipping_charge = 1000
        total = subtotal + shipping_charge
    return render(request, "cart.html", {'carts': carts, 'subtotal': subtotal,
                                         'shipping_charge': shipping_charge, 'total': total, 'x': x})


def save_cart(request):
    if request.method == "POST":
        username = request.POST.get('username')
        product_name = request.POST.get('product_name')
        product_quantity = request.POST.get('product_quantity')
        total_price = request.POST.get('total_price')
        try:
            x = ProductDB.objects.get(Product_Name=product_name)
            img = x.Product_Image
        except ProductDB.DoesNotExist:
            img = None
        obj = CartDB(Username=username, Product_Name=product_name, Product_Quantity=product_quantity,
                     Total_Price=total_price, Product_Image=img)
        obj.save()
        return redirect(home)


def checkout(request):
    return render(request, "checkout.html")
