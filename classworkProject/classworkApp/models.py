from django.db import models

# Create your models here.
from django.db import models

# Add a new Dog model to your schema. Give it the fields: name, breed, color, and gender. Name should be a dog name, breed should be dog breed, color should be the color of the dog, and gender should be the gender of the dog.


class Dog(models.Model):
    name = models.CharField(max_length=200)
    breed = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)


# Add a new Account model to your schema. Give it the fields: username, realName, accountNumber, balance. Username should be a username the user uses to log in, the realName should be a user's real name, accountNumber should be the user's account number, and balance is the user's balance.

class Account(models.Model):
    username = models.CharField(max_length=200)
    fullName = models.CharField(max_length=200)
    accountNumber = models.IntegerField()
    balance = models.DecimalField(decimal_places=3, max_digits=20)




