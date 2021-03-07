from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.contents_list.as_view())
]