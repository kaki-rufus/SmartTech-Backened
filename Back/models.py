from django.db import models

# Create your models here.

# Home
class Home(models.Model):
    bg_image = models.ImageField(blank=True)

    class Meta:
        verbose_name_plural = 'Home'

# About
class About(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(null=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return self.name

# Shop
# class Shop(models.Model):
#     name = models.CharField(max_length=40)
#     description = models.TextField()

#     class Meta:
#         verbose_name_plural = 'Shop'

#     def __str__(self):
#         return self.name


# Networking


# Web Desing


# Data Analysis


# PC sales and Troubleshoot


# Mentorship


# Members
class Members(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField()
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Members'

    def __str__(self):
        return self.name

# contacts
class Contacts(models.Model):
    email = models.EmailField(max_length=20)
    phone = models.CharField(max_length=30)
    message = models.TextField(null=True)

    class Meta:
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.email