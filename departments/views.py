from django.shortcuts import render,get_list_or_404,get_object_or_404,redirect,Http404
from django.contrib import  messages
from django.contrib.auth.decorators import permission_required
from  django.db.models import  Q
from django.http import  JsonResponse
from .models import Departmant,Department_Data,Indicator,Baseline,Report,Description
from .forms import (
    Department_Data_Form,Quartally_Form,
    Annualy_Filter,Department_Data_Form_Update,
    add_department,IndicatorForm, BaseLineForm,
    BaseLineUpdateForm,AddReportForm,
    Indicator_description,Indicator_description_update_form,
    UpdateReportForm,
)
# 0549011214
# Create your views here.

def all_department(request):
    departmant = Departmant.objects.all()
    query = request.GET.get('keyword')
    if query:
        departmant = departmant.filter(name__icontains=query)
    form = add_department(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('department:all_department')

    context = {
        'departmants':departmant,
        'form':form,
    }
    return render(request,'deparment/all_department.html',context)

@permission_required('add_indicator.Can add indicator')
def addIndicator(request,id):
    department = get_object_or_404(Departmant,id=id)
    # if request.method == 'POST':
    form = IndicatorForm(request.POST or None)
    if form.is_valid():
        department = department
        indicator =form.cleaned_data['indicator']
        add_indicator = Indicator.objects.create(indicator=indicator,department=department)
        messages.success(request,'saved')
        # return redirect('department:add_indicator',id)
    context = {
        'form':form,
        'departmant_name':department,
    }
    return render(request,'deparment/add_indicator.html',context)

# def update indicator(request):

#     return render(request,'deparment/add_indicator.html',context)


def allIndicator(request,id):
    department = get_object_or_404(Departmant,id=id)
    allIndicator = department.indicators.all()
   
    context = {
        'department':department,
        'allIndicator':allIndicator,
       
    }
    return render(request,'deparment/all_indicators.html',context)

def indicator_to_report(request,id):
    try:
        chart_type = {
            '1':'bar','2':'bar3d',
        }
        indicator = get_object_or_404(Indicator,id=id)
        reports = indicator.indicator_baseline
        form = Indicator_description(request.POST or None)
        if form.is_valid():
            indicator =indicator
            description = form.cleaned_data['description']
            Description.objects.create(indicator=indicator,description=description)
            # form.save()
            return redirect('department:indicator_reports',id)
       
    # print(reports)
    except Baseline.DoesNotExist:
        raise  Http404('THIS INDICATOR HAS NO BASELINE PLEASE SET ONE',indicator)


    context =  {
        'indicator':indicator,
        'reports':reports,
        'chart_type':chart_type,
        'form':form,
       
    }

    return render(request,'deparment/indicator_to_report.html',context)

def indicator_description_update(request,id):
    description = get_object_or_404(Description,id=id)
    form = Indicator_description_update_form(request.POST or None,instance=description)
    if form.is_valid():
        form.save()
        return redirect('department:indicator_reports',id)
    context = {
        'form_update':form, 
    }
    return render(request,'deparment/update_indicator_description.html',context)


def buidIndicatorChat(request,id,department_name):
    # report = Report.objects.values('date','value')
    
    base_line_values = []
    indicator = get_object_or_404(Indicator,id=id,department__name=department_name)
    # print(' indicator is ',indicator)
    base_line = indicator.indicator_baseline.all_saved_reports.all()
    for i in  base_line:
    
        base_line_values.append({i.date:i.value})
    
    return JsonResponse(base_line_values,safe=False)

@permission_required('add_baseline.Can add baseline')
def add_baseline(request,id):
    indicator = get_object_or_404(Indicator,id=id)
    # baseline = get_object_or_404(Baseline,id=indicator.id)
   
    # if request.method == 'POST':
    form = BaseLineForm(request.POST or None)
    if form.is_valid():
        indicator = indicator
        base_line =form.cleaned_data['base_line']
        value =form.cleaned_data['value']
        activity = form.cleaned_data['activity']
        add_indicator = Baseline.objects.create(indicator=indicator,base_line=base_line,value=value,activity=activity)
        messages.success(request,'new baseline added')
        return redirect('department:add_baseline',id)
    # set_session = request.session['base_line_exist']= \
    #     Baseline.objects.filter(base_line_available=True,indicator=indicator).exists(), 
 
    context = {
        'form':form,
        'indicator':indicator,
        'base_line_exist': Baseline.objects.filter(base_line_available=True,indicator=indicator).exists(),   
    }
    return render(request,'deparment/add_baseline.html', context)

# 


def update_baseline(request,id):
    baseline = Baseline.objects.get(id=id)
    # if request.method == 'POST':
    form = BaseLineUpdateForm(request.POST or None,instance=baseline)
    # base_line_available =base_line.base_line_available
    if form.is_valid():
   
        # return redirect('department:allindicator',id)
        form.save()
    else:
        form =BaseLineUpdateForm()
 
    context = {
        'form':form,
        # 'indicator':indicator,
        # 'base_line_exist': Baseline.objects.filter(base_line_available=True,indicator=indicator).exists(),   
       
    }
    return render(request,'deparment/update_baseline.html', context)


# 

def viewBaseline(request,id):
    indicator = get_object_or_404(Indicator,id=id)

    try:
        
        view_baseline = indicator.indicator_baseline
        # baseline1 = view_baseline
        # convert = str(baseline1)
    
        # converted_value = convert[0:-22]
    # print('view_baseline' ,view_baseline)
        # print('indicator  ', converted_value)

        form = AddReportForm(request.POST or None)
        if form.is_valid():
            base_line = view_baseline.base_line
            date = form.cleaned_data['date']
            value = form.cleaned_data['value']
            description = form.cleaned_data['description']
        # Report.objects.create(base_line=base_line,date=date,value=value,description=description)
        # print('parent ',baseline,'what i wanted base_line',view_baseline.base_line)
    except Baseline.DoesNotExist:
        raise  Http404('THIS INDICATOR HAS NO BASELINE PLEASE SET ONE',indicator)
   
    context = {
        'view_baseline':view_baseline,  #somthing wrong here when you remove this line
        'converted_value':indicator,
        # 'form':form,
       
    }
    return render(request,'deparment/view_baseline.html',context)


@permission_required('add_report.Can add report')
def add_report(request,id):
    baseline = get_object_or_404(Baseline,id=id) 
    # baseline1 = baseline
    # convert = str(baseline1)
    user = request.user.is_active
    print(user)
    
    # here = convert[0:-22]
    form = AddReportForm(request.POST or None)
    if form.is_valid():
        # # base_line = baseline
        date = form.cleaned_data['date']
        value = form.cleaned_data['value']
        description = form.cleaned_data['description']
        Report.objects.create(base_line=baseline,date=date,value=value,description=description)
        # form.save()
        messages.success(request,'saved')
        return redirect('department:add_report',id)

    context = {
        'form':form,
        'baseline':baseline,
        # 'value':baseline
    }
    return render(request,'deparment/add_report.html', context)


def UpdateReport(request,id,departmant_name):
    report = get_object_or_404(Report,id=id,base_line__indicator__department__name=departmant_name)
    form = UpdateReportForm(request.POST or None,instance=report)
    if form.is_valid():
        form.save()
        print(request.session.get('departmant_name'))
        return redirect('department:filter_by_department',request.session.get('departmant_name'),departmant_name)

    context ={
        'form':form,
        'report':report,
    }
    return render(request,'deparment/update_report.html',context)


def view_all_report(request):
    all_report = Report.objects.all()


    context ={
      'all_report':all_report,
    }
    return render(request,'deparment/all_records.html',context)


def filter_by_department(request,id,department_name):
    filter_department = get_object_or_404(Departmant,id=id,name=department_name)
    #setting this session and using the id in updatereport method above
    request.session['departmant_name']=id  
    # query_set = Report.objects.filter(base_line__indicator__department__name=filter_department)

    # get_indicators = query_set.values_list('base_line__indicator__indicator',flat=True).distinct()
    

    # indicator  = request.GET.get('indicator')
    
    # base_line = request.GET.get('base_line')
   
    # if indicator:
    #     query_set = query_set.filter(base_line__indicator__indicator__icontains=indicator)

    # if base_line:
    #         query_set = query_set.filter(base_line__base_line=int(base_line))
            
    # indicators_values = []
    #  # departmant = get_object_or_404(Baseline,id=id)
    # indicators = query_set
    # for i in indicators:
    #     indicators_values.append({i.date:i.value})
    #     # print(i)
    
    # return JsonResponse(indicators_values,safe=False)
    context = {
        'filter_department':filter_department,
        # 'all_report':query_set,
        # 'all_indicator':get_indicators,
        
    }

    return render(request,'deparment/depart.html',context)

# not using bellow methods or whatever
def add_departmant_Date(request,dep_id):
    department = get_object_or_404(Departmant,id=dep_id)
    form = Department_Data_Form(request.POST or None)

    if form.is_valid():
        department = department
        indicators = form.cleaned_data['indicators']
        base_line = form.cleaned_data['base_line']
        date = form.cleaned_data['date']

        department = Department_Data(department=department,indicators=indicators,base_line=base_line,date=date)
        department.save()
        return redirect('department:add_departmant_Date',dep_id)
        # return redirect('department:all_department')
    else:
        # messages.success(request,'not saved')
        form = Department_Data_Form()
    

    context = {
        'form':form,
        'department':department,

    }
    return render(request,'deparment/add_department_data.html',context)

    #    using the add new template but different forms.py

@permission_required('change_department_data.Can change department_ data',raise_exception=True,login_url='/login/')
def update_departmant_Date(request,id):
    
    department = get_object_or_404(Department_Data,id=id)
    # print(department.department.name)
  
    form = Department_Data_Form_Update(request.POST or None,instance=department)

    if form.is_valid():
        form.save()
        messages.info(request,'updated')

        return redirect('department:quartally_data')
       

    # else:
    #     form = Department_Data_Form()
    
    context = {
        'form':form,
        'department':department,

    }
    return render(request,'deparment/add_department_data.html',context)

@permission_required('delete_department_data.Can delete department_ data',raise_exception=True)
def delete(request,id):
    if request.method == 'POST':
        departmantdata = get_object_or_404(Department_Data,id=id)
       
        departmantdata.delete()
    return redirect('department:quartally_data')
       


def quartally_data(request):
    query = request.GET.get('keyword')
 
    query_set = Department_Data.objects.all().order_by('department__name')
    form = Quartally_Form(request.GET or None)
    sum_of_base_line = ''
    if form.is_valid():
        date1 = request.GET.get('date1')
        quarterly = request.GET.get('quarterly')
        department = form.cleaned_data['department']
        
        #FILTERING HERE  
        if date1 and quarterly and department:
        # quartarly and department
            query_set = query_set.filter(Q(date__quarter=quarterly)&Q(date__year=date1)&Q(department__name=department)).order_by('department__name')
            
        # quarterly without department
        elif date1 and quarterly:
            query_set = query_set.filter(Q(date__quarter=quarterly)&Q(date__year=date1)).order_by('department__name')

        # elif quarterly:
        #     query_set = query_set.all().order_by('department__name')
        #     print(quarterly)
        if query:
            query_set =query_set.filter(Q(department__name__icontains=query)|Q(indicators__icontains=query))
    
    context= {
        'form':form,
        'query_set':query_set,
        'sum_of_base_line': query_set.aggregate(Sum('base_line')),
        'total':Department_Data.objects.count()
    }

    return render(request,'deparment/all_data_quartally.html', context)



def annualy_data(request):
    query = request.GET.get('keyword')

    query_set = Department_Data.objects.all().order_by('department__name')
    form = Annualy_Filter(request.GET or None)

    if form.is_valid():
        date1 = request.GET.get('date1')
        quarterly = request.GET.get('quarterly')
        department = form.cleaned_data['department']
        

        #FILTERING HERE  
        # quartarly and department
        if date1  and department:
            query_set = query_set.filter(Q(date__year=date1)&Q(department__name=department))
            # print(query_set.query)
           
        # quarterly without department
        elif date1:
            query_set =  query_set.filter(date__year=date1)

        elif department:
            query_set = Department_Data.objects.all().order_by('department__name')
        
        if query:
            query_set =query_set.filter(Q(department__name__icontains=query)|Q(indicators__icontains=query))
    
    context= {
        'form':form,
        'query_set':query_set,
        'sum_of_base_line': query_set.aggregate(Sum('base_line')),
        'total':Department_Data.objects.count(),
    }

    return render(request,'deparment/all_department_annualy.html', context)

