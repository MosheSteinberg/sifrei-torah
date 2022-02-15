from django.urls import path

from . import views

app_name='tracker'

urlpatterns = [
    path('', views.index, name='index'),
    path('seforim/', views.SeforimIndex, name='seforim-index'),
    path('seforim/<int:id>/', views.IndividualSefer, name='individual-sefer')
]