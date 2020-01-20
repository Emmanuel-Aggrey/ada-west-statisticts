from django.db import models
from departments.models import BaseModel
from django.utils import  timezone
# Create your models here.

class Market(BaseModel):
    name = models.CharField(max_length=50,unique=True,help_text='create a new market')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Market'
        verbose_name = 'Market'  
        ordering = ['-date_add']


class Visit(BaseModel):
    market_name = models.ForeignKey(Market,on_delete=models.CASCADE,related_name='visits')
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f'Market {self.market_name} : Date {self.date}'
    class Meta:
        ordering = ['-date_add']

class Commodity(BaseModel):
    name = models.CharField(max_length=200,unique=True)
    unit_of_sale = models.CharField(max_length=20,blank=True, null=True)


    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Commodity\'s'
        verbose_name = 'Commodity'

class Commodity_type(BaseModel):
    visit_day = models.ForeignKey(Visit,on_delete=models.CASCADE,related_name='commodity_visits')
    commodity_type = models.ForeignKey(Commodity,on_delete=models.CASCADE,verbose_name='commodity',related_name='commodities')
    name = models.CharField('commodity type',max_length=200,blank=True, null=True,help_text='eg if you select rice as commodity local or perfume will be the commodity type')
    num_pieces = models.PositiveSmallIntegerField('number of pieces',blank=True, null=True)
    weight_volume = models.CharField('weight volume (kg/litre)',max_length=5,blank=True, null=True)
    price = models.DecimalField('price (GH₵)',blank=True, null=True,decimal_places=2,max_digits=10)
    the_trader = (
        ('t1','Trader 1'),('t2','Trader 2'),('t3','Trader 3'),('t4','Trader 4'),('t5','Trader 5'),
    )
    trader = models.CharField(max_length=2,choices=the_trader,blank=True, null=True)
    def __str__(self):
        return '{} Item-Type {} name {}'.format(str(self.visit_day),str(self.commodity_type),self.name)

    class Meta:
        verbose_name_plural = 'Commodity Type\'s'
        verbose_name = 'Commodity'

class Description(models.Model):
    market_name = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.description