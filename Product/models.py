from django.db import models
from Category.models import Categories
# Create your models here.

class Products(models.Model):
    STATE = (
            ('Active','Active'),
            ('Ended','Ended')
        )

    DURATION = (
        ('5 days,','5 days,'),
        ('10 days','10 days'),
        ('15 days','15 days'),
        ('20 days','20 days')
    )
    Product_Code = models.CharField(max_length=250)
    Name         = models.CharField(max_length=250)
    Price        = models.FloatField(null=False)
    Quantity     = models.FloatField(null=False)
    Start_Date   = models.DateTimeField(auto_now_add=True ,blank = True )
    Dration      = models.CharField(max_length=250 , null = False , choices=DURATION)
    Image        = models.ImageField(upload_to="static/img" , blank = True)
    State        = models.CharField(max_length=250 , null = False , choices=STATE)
    category     = models.ManyToManyField(Categories)

    def __str__(self):
        return self.Name

