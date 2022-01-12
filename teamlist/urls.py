from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('add/',views.addteams,name='add'),
    path('list/',views.listteams,name='list'),
    path('update/',views.update,name='update'),
    path('delete/',views.delete,name='delete')
]