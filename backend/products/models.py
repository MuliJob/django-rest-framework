"""Products Models"""
from django.db import models

# Create your models here.
class Product(models.Model):
    """Products Table"""
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15,
                                decimal_places=2, default=99.99)

    objects = models.Manager()

    def __str__(self):
        return self.title

    @property
    def sale_price(self):
        """
        Calculating Discount
        """
        return "%.2f" %(float(self.price) * 0.8)
    
    def get_discount(self):
        """
        Discount
        """
        return "155"
