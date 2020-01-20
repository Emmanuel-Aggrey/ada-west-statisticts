from .import views
from django.urls import path

app_name ='market'
urlpatterns =[
    path('market/',views.market,name='market'),
    path('add_new_date/<int:id>/',views.visit_new_date,name='add_new_date'),
    path('all_productes/<int:product_id>/',views.all_productes,name='all_products'),
    path('addProduct/<int:visit_id>/',views.addProduct,name='addProduct'),
    path('add_date_to_visit/<int:id>/',views.add_date_to_visit,name='add_date_to_visit'),
    path('buidInCommodityChart/<str:name>/<str:c_type>/<str:market_name>/',views.buidInCommodityChart,name='buidInCommodityChart'),
    path('distinct_commodity/<str:name>/<str:c_type>/<str:market_name>/<str:unit_of_sale>/',views.distinct_commodity_with_graph,name='distinct_commodit_with_graph'),
    path('update_description/<str:market_name>/',views.update_distinct_commodity_with_graph_about,name='update_description'),
]