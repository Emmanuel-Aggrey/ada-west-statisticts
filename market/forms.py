from django import  forms
from .models import Market,Commodity,Commodity_type,Visit,Description

class MarketForm(forms.ModelForm):
    class Meta:
        model = Market
        fields = '__all__'



class VisitForm(forms.ModelForm):
    class Meta:
        
        model = Visit
        exclude = ['market_name']
        # fields  = '__all__'
        widgets = {
            'date': forms.DateTimeInput(attrs={'class':'form-control','type':'date',}),
            # 'time': forms.DateTimeInput(attrs={'class':'form-control','type':'time'}),

        }

class CommodityForm(forms.ModelForm):
    class Meta:
        model = Commodity
        fields = '__all__'





class CommodityTypeForm(forms.ModelForm):
  
    class Meta:
        model = Commodity_type
        exclude = ['visit_day']
        fields = '__all__'





class DescriptionForm(forms.ModelForm):
    description = forms.Textarea(attrs={'cols':2,'rows':3})
    # market_name = forms.CharField(required=False)
    class Meta:
        model = Description
        exclude = ['market_name',]
        # fields = [
        #     'description',
        # ]

class DescriptionFormUpdate(forms.ModelForm):
    class Meta:
        model = Description
        fields = '__all__'
        
class TraderForm(forms.Form):
    the_trader = [
        ('all','All'),('t1','Trader 1'),
        ('t2','Trader 2'),('t3','Trader 3'),
        ('t4','Trader 4'),('t5','Trader 5'),
        ('none','No Trader'),
    ]
    trader = forms.ChoiceField(choices=the_trader,initial='all')
































































































































































