from django.db import models

class CustomManager(models.Manager):
    def all_book_in_desc_price(request):
        return super().order_by('price').filter(is_deleted='n')

    def all_book_in_asc_price(request):
        return super().order_by('-price').filter(is_deleted='n')


