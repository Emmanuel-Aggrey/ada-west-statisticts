from django import  forms
from .models import  Department_Data,Departmant,Indicator,Baseline,Report,Description

class add_department(forms.ModelForm):
    class Meta:
        model = Departmant
         # exclude =['department']
        fields = '__all__'


class IndicatorForm(forms.ModelForm):
    class Meta:
        model = Indicator
        exclude =['department']

        # fields = '__all__'
class Indicator_description(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':40,'placeholder':'enter a description here'}))

    class Meta:
        model = Description
        exclude =['indicator']
    
class Indicator_description_update_form(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':40,'placeholder':'enter a description here'}))

    class Meta:
        model = Description
        fields = '__all__'

        # exclude =['indicator']
    


class BaseLineForm(forms.ModelForm):
    activity = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows':3,'cols':40}))

    
    class Meta:
        model = Baseline
        exclude =['indicator','base_line_available']

        widgets = {
            # 'base_line': forms.DateTimeInput(attrs={'class':'form-control','type':'date',}),
            # 'time': forms.DateTimeInput(attrs={'class':'form-control','type':'time'}),

        }


class BaseLineUpdateForm(forms.ModelForm):
    activity = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows':3,'cols':40}))

    class Meta:
        model = Baseline
        exclude = ['base_line_available']
        # fields = '__all__'
        # widgets = {
        #     'base_line': forms.DateTimeInput(attrs={'class':'form-control','type':'date',}),
        #     # 'time': forms.DateTimeInput(attrs={'class':'form-control','type':'time'}),

        # }

class AddReportForm(forms.ModelForm):
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows':3,'cols':40}))
    activity = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows':3,'cols':40}))

    # date =  forms.DateTimeInput(attrs={'class':'form-control','type':'date',}),


    class Meta:
        model = Report
        exclude = ['base_line',]


class UpdateReportForm(forms.ModelForm):
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows':3,'cols':40}))
    activity = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows':3,'cols':40}))

    # date =  forms.DateTimeInput(attrs={'class':'form-control','type':'date',}),


    class Meta:
        model = Report
        fields = '__all__'



class Department_Data_Form(forms.ModelForm):
    indicators = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':40}))
    class Meta:
        model = Department_Data
        exclude =['department']
        fields = '__all__'
        widgets = {
            'date': forms.DateTimeInput(attrs={'class':'form-control','type':'date',}),
            # 'time': forms.DateTimeInput(attrs={'class':'form-control','type':'time'}),

        }

class Department_Data_Form_Update(forms.ModelForm):
    indicators = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':40}))
    class Meta:
        model = Department_Data
        # exclude =['department']
        fields = '__all__'
        widgets = {
            # 'date': forms.DateTimeInput(attrs={'class':'form-control','type':'date',}),
            # 'time': forms.DateTimeInput(attrs={'class':'form-control','type':'time'}),

        }


class Quartally_Form(forms.Form):
    quarter = (
        ('1','FIRST QUARTER'),
        ('2','SECOND QUARTER'),
        ('3','THIRED QUARTER'),
        ('4','FORTH QUARTER'),
        # ('5','ANNUALY'),
        # ('6','ALL REPORTS'),
    )
    quarterly = forms.ChoiceField(choices=quarter,required=False)
    department = forms.ModelChoiceField(queryset=Departmant.objects.all(),empty_label='select department',required=False)
    date1 = forms.IntegerField(label='year',required=False,widget=forms.NumberInput( attrs={'style': 'width: 65px'}))




class  Annualy_Filter(forms.Form):
    # filter_from = forms.DateField()
    annauly = (
        ('1','ANNUALY'),
        ('2','ALL REPORTS'),
    )
    annualy = forms.ChoiceField(choices=annauly)
    department = forms.ModelChoiceField(queryset=Departmant.objects.all(),required=False, empty_label='select department')
    date1 = forms.IntegerField(label='year',required=False,widget=forms.NumberInput( attrs={'style': 'width: 65px'}))

# not using this for now
class OrderFilter_Form(forms.Form):
    order = [
        ['department__name','A-Z',],
        ['-department__name','Z-A',],
        ['date_updated','First Modeified'],
        ['-date_updated','Last Modified'],
    ]

    the_order = forms.ChoiceField(choices=order,required=False,label='order by')

order = {
    'department__name':'A-Z',
    '-department__name':'Z-A',
    'date_updated':'First Modeified',
    '-date_updated':'Last Modified',
}