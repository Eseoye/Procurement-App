from django.db import models
from django.contrib.auth.models import User


# Create your models here. To do the products

# For naming of the categories field using tuple
CATEGORY = (
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),
)


class Product(models.Model):
    name = models.CharField(max_length=100, null=True) # null is used to add & delete its not good 4deployment so remove
    category = models.CharField(max_length=30, choices=CATEGORY, null=True) # you use choices so you can add more to the category
    quantity = models.PositiveIntegerField(null=True)
    
    # to change the words from plura e.g orders on the admin dashboard
    #class Meta:
        #verbose_name_plural = 'Product'
    
    # how to make the product look in my admin panel instead of project object its displaying

    def __str__(self):
        return f'{self.name}-{self.quantity}'
    
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True) # to use the user you must import user at the top
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0)
    # is_authenticated = models.BooleanField(null=True, default=False)
    
    def __str__(self):
        return f'{self.product}-{self.status} ordered by {self.staff.username}'


