from django.db import models
from book.manager import CustomManager

# Create your models here.
class BookTable(models.Model):
    book_name=models.CharField(max_length=100)
    author_name=models.CharField(max_length=100)
    price=models.IntegerField()
    typeofbook=models.CharField(max_length=100)
    is_deleted=models.CharField(max_length=5,default='n')

    #CustomManager=models.Manager()
    CustomManager=CustomManager()
