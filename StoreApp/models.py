from django.db import models


class SignupDB(models.Model):
    Signup_Name = models.CharField(max_length=100, null=True, blank=True)
    Signup_Email = models.CharField(max_length=100, null=True, blank=True)
    Signup_Contact = models.CharField(max_length=100, null=True, blank=True)
    Signup_Password = models.CharField(max_length=100, null=True, blank=True)
    Signup_ConfirmPassword = models.CharField(max_length=100, null=True, blank=True)
