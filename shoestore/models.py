from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField(max_length=200)

class ShoeType(models.Model):
    style = models.CharField(max_length=8)

class ShoeColor(models.Model):
    color_options = [
        ('R', 'Red'),
        ('O', 'Orange'),
        ('Y', 'Yellow'),
        ('G', 'Green'),
        ('B', 'Blue'),
        ('I', 'Indigo'),
        ('V', 'Violet'),
        ('BLA', 'Black'),
        ('W', 'White'),
    ]
    color_name = models.CharField(max_length=8, choices=color_options, default='White')

class Shoe(models.Model):
    size = models.IntegerField(null=False)
    brand = models.CharField(max_length=80)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='manufacturer')
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE, related_name='color')
    material = models.CharField(max_length=80)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE, related_name='type')
    fasten_type = models.CharField(max_length=80)