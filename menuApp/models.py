from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ContactsModel(models.Model):

    contact_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(default='xyz@abc.com')
    spam = models.BooleanField(default=False)
    owner_name = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.contact_name
