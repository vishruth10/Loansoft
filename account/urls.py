from django.urls import path
from . import views
from django.contrib import admin

from django.views.static import serve
from django.conf.urls import url


urlpatterns= [
    path('', views.index, name='index'),
    path('search',views.search,name='search'),
    path('success',views.success,name="success"),
    path('details',views.details,name="details"),
    path('history/<str:name>',views.history,name="history"),
    path('history_user',views.history_user,name="history_user"),
    path('user_details',views.user_details,name="user_details"),
    path('loan_form/<str:name>/<str:dept>',views.loan_form,name="loan_form"),
    path('update_form/<str:name>/<str:dept>',views.update_form,name="update_form"),
    path('take_loan',views.take_loan,name="take_loan"),
    path('update_loan',views.update_loan,name="update_loan"),
    path('total',views.total,name="total"),
    # path('history_user',views.history_user,name="history_user"),
    path url(r '^media/(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT}), 
    path url(r '^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]