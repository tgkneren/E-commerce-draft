from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class Customer(models.Model):
    username= models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    
    def __str__(self):
        return f"username:{self.username},password:{self.password}"
 
