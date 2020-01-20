from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404
from .models import Commodity,Commodity_type,Visit,Market,Description
from django.db.models import Q
from django.http import  JsonResponse
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from  .forms import  (
    VisitForm,CommodityTypeForm,
    CommodityForm,MarketForm,
    TraderForm,DescriptionForm,
    DescriptionFormUpdate
)
# Create your views here.

def market(request):
    market_name = Market.objects.all()
    form = MarketForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('market:market')
    # else:
    #     form = MarketForm()
    # visit_form = VisitForm(request.POST or None)
    # if visit_form.is_valid():
    #     date =request.POST.get('visit_date')
    #     print('visit_date ',date)
    #     Visit.objects.create(market_name=market_name,date=date)
        return redirect('market:market')

        # date =visit_form.cleaned_data['date']
        # Visit.objects.create(market_name=market_name,date=date)

    paginator = Paginator(market_name, 5)
    page = request.GET.get('page')
    try:
        markets = paginator.page(page)
    except PageNotAnInteger:
        markets = paginator.page(1)
    except EmptyPage:
        markets = paginator.page(paginator.num_pages)
    context = {
        'market':markets,
        'form':form,
        # 'visit_form':visit_form,
        'market_size':len(market_name)
    }
    return render(request,'market/all_market.html',context)

@permission_required('add_visit.Can add visit')
def add_date_to_visit(request,id):
    market_name = get_object_or_404(Market,id=id)
    form = VisitForm(request.POST or None)
    if form.is_valid():
        date = form.cleaned_data['date']
        Visit.objects.create(market_name=market_name,date=date)
        # print('saved in date add')
        return redirect('market:add_new_date',id)

    context = {
        'form':form,
        'market_name':market_name,
    }
    return render(request,'market/add_date_to_visit.html',context)


def visit_new_date(request,id):
    # print('new date page =', id)
    market_name = get_object_or_404(Market,id=id)
    request.session['visit_new_date_back_id']= id
    form = VisitForm(request.POST or None)
    if form.is_valid():
        date = form.cleaned_data['date']
        Visit.objects.create(market_name=market_name,date=date)
        return redirect('market:add_new_date',id)
    visit_days = Visit.objects.filter(market_name=market_name)
    # visit_days = get_list_or_404(Visit,market_name=market_name)
    paginator = Paginator(visit_days, 5)
    page = request.GET.get('page')
    try:
        visit_day = paginator.page(page)
    except PageNotAnInteger:
        visit_day = paginator.page(1)
    except EmptyPage:
        visit_day = paginator.page(paginator.num_pages)

    
    commodity_type = Commodity_type.objects\
        .filter(visit_day__market_name__name=market_name).distinct('name','commodity_type')
#    giving error if no value is set as default ie m is just a value (has no meaning)
    query = request.GET.get('keyword')
    if query:
        commodity_type = commodity_type.filter(
        Q(commodity_type__name__icontains=query)|
        Q(name__icontains=query)|
        Q(commodity_type__unit_of_sale__icontains=query)
    )
    # print(query)
    
    context = {
        'form':form,
        'visit_day':visit_day,
        'market':market_name,
        'commodity_type':commodity_type,
      
    }
    return render(request,'market/new_date.html',context)

@permission_required('add_commodity_type.Can add Commodity')
def addProduct(request,visit_id):
    # print(request.session['visit_new_date_back_id'],' is here')

    visit_day = get_object_or_404(Visit,id=visit_id)
    form = CommodityTypeForm(request.POST or None)
    if form.is_valid():
        visit_day = visit_day
        commodity_type = form.cleaned_data['commodity_type']
        name = form.cleaned_data['name']
        num_pieces = form.cleaned_data['num_pieces']
        weight_volume = form.cleaned_data['weight_volume']
        price = form.cleaned_data['price']
        trader = form.cleaned_data['trader']
        commodity_type = Commodity_type.objects.create(
            visit_day=visit_day,
            commodity_type=commodity_type,
            name =name,
            num_pieces =num_pieces,
            weight_volume =weight_volume,
            price =price,   
            trader=trader,
        )
        # print('visit  saved')
        return redirect('market:addProduct',visit_id)
    else:
        form = CommodityTypeForm()
        # print('visit not saved',visit_day)
    commodityForm =CommodityForm(request.POST or None)
    if commodityForm.is_valid():
        commodityForm.save()
        return redirect('market:addProduct',visit_id)
    else:
        commodityForm =CommodityForm()

    context = {
        'form':form,
        'visit_date':visit_day,
        'commodityForm':commodityForm,
       
    }

    return render(request,'market/add_product.html',context)

    
def all_productes(request,product_id):
    form = TraderForm()
    visit_date = get_object_or_404(Visit,id=product_id)
    query_set = visit_date.commodity_visits.all()
    
    # query_set = Commodity_type.objects.all()
    query = request.GET.get('keyword')
    trader = request.GET.get('trader')
    # if query:
    #     print('all', trader)
    #     query_set = query_set.filter(Q(commodity_type__name__icontains=query)|Q(
    #         name__icontains=query))
      
    if trader:
        query_set = query_set.filter(Q(commodity_type__name__icontains=trader)|Q(
            name__icontains=trader)|Q(trader__icontains=trader))
        if 'all' in trader:
            query_set = visit_date.commodity_visits.all()
        if 'none' in trader:
                query_set = visit_date.commodity_visits.filter(trader=None)
            
  

    context =   {
        'products':query_set,
        'visit_date':visit_date,
        'form':form,
        'total_size': visit_date.commodity_visits.count()
    }
    return render(request,'market/all_products.html',context)

def distinct_commodity_with_graph(request,name,c_type,market_name,unit_of_sale):
    # get_object_or_404(Description,)
    # get_description = ''
    # get_description = Description.objects.filter(market_name= name+c_type+market_name+unit_of_sale).latest('description')
    # form_update = DescriptionForm(request.POST or None,instance=get_description)
    # if form_update.is_valid():
    #     description = form_update.cleaned_data['description']
    #     market_info = name+c_type+market_name+unit_of_sale
    #     Description.objects.create(market_name=market_info,description=description)

        # form_update.save()

    form = DescriptionForm(request.POST or None)
    if form.is_valid():
        # market = Market.objects.get(name=market_name)

        description = form.cleaned_data['description']
        market_info = name+c_type+market_name+unit_of_sale
        # print(market_info)
        # print(market)
        Description.objects.create(market_name=market_info,description=description)
    
        return redirect('market:distinct_commodit_with_graph',name,c_type,market_name,unit_of_sale)
    query_set = get_list_or_404(Commodity_type,name=name,commodity_type__name=c_type,\
    visit_day__market_name__name=market_name)
    # giving a 404 so must do this
    get_description = ''
    try:
        get_description = Description.objects.filter(market_name= name+c_type+market_name+unit_of_sale).latest('description')
    
    #     print(get_description)
       
    except :
        pass

    context = {
        'commodity_type':query_set,
        'commodity':name,
        'market_name':market_name,
        'c_type':c_type,
        'form':form,
        'unit_of_sale':unit_of_sale,
        'get_description':get_description,
        # 'form_update':form_update,
    }

    return render(request,\
        'market/distinct_commodity_with_graph.html',\
            context)
# description update


def buidInCommodityChart(request,name,c_type,market_name):
   
    commodity_type_values = []
    commodity = Commodity_type.objects.filter(
        name=name,commodity_type__name=c_type,\
        visit_day__market_name__name=market_name
    ).order_by('visit_day__date')

    for i in commodity:
        date = i.visit_day.date.strftime('%Y-%m-%d')
        commodity_type_values.append({date:float(i.price)})

    return JsonResponse(commodity_type_values,safe=False)

def update_distinct_commodity_with_graph_about(request,market_name,):
    get_description = Description.objects.filter(market_name= market_name).latest('description')
    form_update = DescriptionFormUpdate(request.POST or None,instance=get_description)
    if form_update.is_valid():
        forform_update.save()
        # return redirect('market:distinct_commodit_with_graph',name,c_type,market_name,unit_of_sale)

    context = {
        'form_update':form_update,
        'get_description':get_description,
    }
    return render(request,'market/update_description.html',context)
    
