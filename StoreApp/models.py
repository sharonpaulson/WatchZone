from django.db import models


class SignupDB(models.Model):
    Signup_Name = models.CharField(max_length=100, null=True, blank=True)
    Signup_Email = models.CharField(max_length=100, null=True, blank=True)
    Signup_Contact = models.CharField(max_length=100, null=True, blank=True)
    Signup_Password = models.CharField(max_length=100, null=True, blank=True)
    Signup_ConfirmPassword = models.CharField(max_length=100, null=True, blank=True)


class CartDB(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    Product_Name = models.CharField(max_length=100, null=True, blank=True)
    Product_Quantity = models.IntegerField(null=True, blank=True)
    Total_Price = models.IntegerField(null=True, blank=True)
    Product_Image = models.ImageField(upload_to="cart_images/", null=True, blank=True)