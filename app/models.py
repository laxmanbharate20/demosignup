from django.db import models
from django.core.validators import RegexValidator,MaxValueValidator
from django.contrib.auth.models import User

class RegisterModel(models.Model):
    # first_name = models.CharField(max_length=10)
    # last_name = models.CharField(max_length=10)
    # username = models.CharField(max_length=20,unique = True)
    business_name = models.CharField(max_length=20)
    business_licn_no = models.CharField(max_length=20,)
    phone_no = models.BigIntegerField(unique = True,validators=[RegexValidator(r'^[7-9][0-9]{9}$',message='Invalid phone number')])
    # email = models.EmailField(unique = True)
    # password = models.CharField(max_length=20)
    # password2 = models.CharField(max_length=20)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
