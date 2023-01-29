from django.urls import path
from . import views

appname = 'account'

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('customer/', views.customer, name='booknow'),
    path('host/', views.host, name='host'),
    path('dateandtime/',views.dateandtime,name='dateandtime'),
    path('bikes/',views.bikes,name='bikes'),
    path('cars/',views.cars,name='cars'),
    path('pay1/',views.pay1,name='pay1'),
    path('pay2/',views.pay2,name='pay2'),
    path('pay3/',views.pay3,name='pay3'),
    path('pay4/',views.pay4,name='pay4'),
    path('pay5/',views.pay5,name='pay5'),
    path('pay6/',views.pay6,name='pay6'),
    path('pay7/',views.pay7,name='pay7'),
    path('pay8/',views.pay8,name='pay8'),
    path('pay9/',views.pay9,name='pay9'),
    path('pay10',views.pay10,name='pay10'),
    path('pay11/',views.pay11,name='pay11'),
    path('pay12/',views.pay12,name='pay12'),
    path('pay13/',views.pay13,name='pay13'),
    path('pay14/',views.pay14,name='pay14'),
    path('pay15/',views.pay15,name='pay15'),
    path('pay16/',views.pay16,name='pay16'),
    path('pay17/',views.pay17,name='pay17'),
    path('pay18/',views.pay18,name='pay18'),
    path('pay19/',views.pay19,name='pay19'),
    path('pay20/',views.pay20,name='pay20'),
    path('success/',views.success,name='success'),
    path('logout/',views.logout_view,name='logout'),
    path('hostadd/',views.hostadd,name='hostadd'),
    path('host/success/',views.added,name='added'),

]
