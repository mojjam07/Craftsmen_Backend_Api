from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    is_craftsman = models.BooleanField(default=False)
    is_apprentice = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    photo = models.ImageField(upload_to='category_photos')

    def __str__(self):
        return self.name

class Craftsman(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, default=None)
    telephone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    skill = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='craftsman_photos')

class Apprentice(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, default=None)
    skill_to_learn = models.CharField(max_length=100)
    selfie = models.ImageField(upload_to='apprentice_photos')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(max_length=100, default='pending')

class Job(models.Model):
    craftsman = models.ForeignKey(Craftsman, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default='pending')
