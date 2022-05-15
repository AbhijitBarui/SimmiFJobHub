from django.urls import path
from . import views

urlpatterns = [
    path('',views.careers,name='careers'),
    path('getjobform',views.getjobform,name='getjobform'),
    path('postjobform',views.postjobform,name='postjobform'),
    path('<int:form_id>/',views.getapplicationform,name='getapplicationform'),
    path('<int:form_id>/postapplicationform',views.postapplicationform,name='postapplicationform'),
    path('viewappcategory/',views.viewappcategory,name='viewappcategory'),
    path('viewappcategory/<int:job_id>/',views.viewapplications,name='viewapplications'),
    path('viewappcategory/<int:job_id>/<int:app_id>/',views.viewapplication,name='viewapplication'),
    path('viewappcategory/<int:job_id>/<int:app_id>/reviewed',views.reviewed,name='reviewed'),
    path('viewappcategory/<int:job_id>/<int:app_id>/accepted',views.accepted,name='accepted'),
]