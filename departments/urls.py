from  django.urls import  path
from .import views
app_name = 'department'

urlpatterns = [
    path('all_department/',views.all_department,name='all_department'),
    path('add_departmant_Date/<int:dep_id>/',views.add_departmant_Date,name='add_departmant_Date'),
    path('update_departmant/<int:id>/update/',views.update_departmant_Date,name='update_departmant_Date'),
    path('quartally_data/',views.quartally_data,name='quartally_data'),
    path('annualy_data/',views.annualy_data,name='annualy_data'),
    path('delete/<int:id>/delete/',views.delete,name='delete'),

    path('indicator/<int:id>/addnew/',views.addIndicator,name='add_indicator'),
    path('allindicator/<int:id>/',views.allIndicator,name='allindicator'),
    path('baseline/<int:id>/add/',views.add_baseline,name='add_baseline'),
    path('update_baseline/<int:id>/',views.update_baseline,name='update_baseline'),
    path('add_report/<int:id>/',views.add_report,name='add_report'),
    path('updateReport/<int:id>/<str:departmant_name>/',views.UpdateReport,name='updateReport'),
    path('viewBaseline/<int:id>/',views.viewBaseline,name='viewBaseline'),
    path('all_report',views.view_all_report,name='all_report'),
    path('filter_by_department/<int:id>/<str:department_name>/',views.filter_by_department,name='filter_by_department'),
    path('buidIndicatorChat/<int:id>/<str:department_name>/',views.buidIndicatorChat,name='buidIndicatorChat'),
    path('reports/<int:id>/',views.indicator_to_report,name='indicator_reports'),
    path('update_description/<int:id>/',views.indicator_description_update,name='update_description'),

]