from django.db import models
from  django.shortcuts import  reverse
from django.utils import  timezone

# Create your models here.


class BaseModel(models.Model):
    date_add = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract =True

class Departmant(BaseModel):
    name = models.CharField(max_length=50,unique=True)
    
    def __str__(self):
        return self.name

class Indicator(BaseModel):
    department = models.ForeignKey(Departmant,on_delete=models.CASCADE,related_name='indicators')
    indicator = models.CharField(max_length=200,unique=True)

    def get_absolute_url(self):
        return reverse('department:add_indicator', args=[self.id])

 

    def __str__(self):
        return "Department: {} : INDICATOR:  {}".format(str(self.department),self.indicator)

class Description(BaseModel):
    indicator = models.OneToOneField(Indicator,on_delete=models.CASCADE,related_name='description')
    description = models.TextField(blank=False, null=True,help_text='write a note about this indicator')

    def __str__(self):
        return self.description

class Baseline(BaseModel):
    indicator = models.OneToOneField(Indicator,on_delete=models.CASCADE,related_name='indicator_baseline')
    # base_line = models.DateField(default=timezone.now)
    base_line = models.PositiveIntegerField()
    value  = models.PositiveIntegerField(help_text='numbers only',blank=True, null=True)
    activity = models.TextField(blank=True, null=True)
    base_line_available =models.BooleanField(default=True)

    def __str__(self):
        return "{} : baseline {}  : value {}".format(str(self.indicator),self.base_line,self.value)

    

class Report(BaseModel):
    base_line = models.ForeignKey(Baseline,on_delete=models.CASCADE,related_name='all_saved_reports')
    # date = models.DateField(default=timezone.now)
    date = models.PositiveIntegerField('year')
    value = models.PositiveIntegerField(blank=True, null=True)
    activity = models.TextField(blank=True, null=True)

    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{} : {} : {}".format(str(self.base_line),self.value,self.date)

    




class Department_Data(BaseModel):
    department = models.ForeignKey(Departmant,on_delete=models.CASCADE,related_name='all_departmants')
    indicators = models.TextField()
    base_line = models.PositiveSmallIntegerField()
    date = models.DateField()

    def __str__(self):
        return str(self.department)

    def get_absolute_url(self):
        return reverse('department:update_departmant_Date', args=[self.id])



    class Meta:
        verbose_name = 'Department Data'
        verbose_name_plural = 'Department Data'

    




