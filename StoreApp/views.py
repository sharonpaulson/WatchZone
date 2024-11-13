from django.shortcuts import render, redirect
from LatestApp.models import CategoryDB, ProductDB
from StoreApp.models import SignupDB


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


def user_login(req):
    if req.method == "POST":
        un = req.POST.get('user')
        pw = req.POST.get('pass')
        if SignupDB.objects.filter(Signup_Name=un, Signup_Password=pw).exists():
            req.session['Signup_Name'] = un
            req.session['Signup_Password'] = pw
            return redirect(home)
        else:
            return redirect(sign_in)
    else:
        return redirect(sign_in)


def user_logout(req):
    del req.session['Signup_Name']
    del req.session['Signup_Password']
    return redirect(home)


def contact(req):
    return render(req, "contact.html")

