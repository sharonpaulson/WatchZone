from django.shortcuts import render, redirect
from LatestApp.models import CategoryDB, ProductDB
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError


def index(req):
    return render(req, "index.html")


def add_categories(req):
    return render(req, "add_categories.html")


def save_categories(req):
    if req.method == "POST":
        category_name = req.POST.get('category_name')
        category_description = req.POST.get('category_description')
        category_image = req.FILES['category_image']
        obj = CategoryDB(Category_Name=category_name,
                         Category_Description=category_description,
                         Category_Image=category_image)
        obj.save()
        return redirect(add_categories)


def display_categories(req):
    cat = CategoryDB.objects.all()
    return render(req, "display_categories.html", {'cat': cat})


def edit_categories(req, cat_id):
    cat = CategoryDB.objects.get(id=cat_id)
    return render(req, "edit_categories.html", {'cat': cat})


def update_categories(req, cat_id):
    if req.method == "POST":
        category_name = req.POST.get('category_name')
        category_description = req.POST.get('category_description')

        try:
            category_image = req.FILES['category_image']
            fs = FileSystemStorage()
            file = fs.save(category_image.name, category_image)

        except MultiValueDictKeyError:
            file = CategoryDB.objects.get(id=cat_id).Category_Image

        CategoryDB.objects.filter(id=cat_id).update(
            Category_Name=category_name, Category_Description=category_description, Category_Image=file
        )
        return redirect(display_categories)


def delete_categories(req, cat_id):
    cat = CategoryDB.objects.filter(id=cat_id)
    cat.delete()
    return redirect(display_categories)


def add_products(req):
    cat = CategoryDB.objects.all()
    return render(req, "add_products.html", {'cat': cat})


def save_products(req):
    if req.method == "POST":
        product_category = req.POST.get('product_category')
        product_name = req.POST.get('product_name')
        product_description = req.POST.get('product_description')
        product_price = req.POST.get('product_price')
        product_image = req.FILES['product_image']
        obj = ProductDB(Product_Category=product_category, Product_Name=product_name,
                        Product_Description=product_description,
                        Product_Price=product_price, Product_Image=product_image)
        obj.save()
        return redirect(add_products)


def display_products(req):
    pro = ProductDB.objects.all()
    return render(req, "display_products.html", {'pro': pro})


def edit_products(req, pro_id):
    cat = CategoryDB.objects.all()
    pro = ProductDB.objects.get(id=pro_id)
    return render(req, "edit_products.html", {'pro': pro, 'cat': cat})


def update_products(req, pro_id):
    if req.method == "POST":
        product_category = req.POST.get('product_category')
        product_name = req.POST.get('product_name')
        product_description = req.POST.get('product_description')
        product_price = req.POST.get('product_price')

        try:
            product_image = req.FILES['product_image']
            fs = FileSystemStorage()
            file2 = fs.save(product_image.name, product_image)
        except MultiValueDictKeyError:
            file2 = ProductDB.objects.get(id=pro_id).Product_Image

        ProductDB.objects.filter(id=pro_id).update(
            Product_Category=product_category,
            Product_Name=product_name,
            Product_Price=product_price,
            Product_Description=product_description,
            Product_Image=file2
        )
        return redirect(display_products)


def delete_products(req, pro_id):
    pro = ProductDB.objects.filter(id=pro_id).delete()
    return redirect(display_products)
