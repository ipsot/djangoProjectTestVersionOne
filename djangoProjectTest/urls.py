from django.contrib import admin
from django.urls import path
from djangoProjectTest.testApp import views

urlpatterns = [
    path('calc/', views.index2),
    path('hello/<str:pname>/', views.index),
    path('indexView/', views.index_view),
    path('admin/', admin.site.urls),
    path('baseView/', views.base_view),
    path('formPage/', views.form_page),
    path('checkFormPage/', views.check_form_page),
    path('persons/', views.persons),
]
