from django.urls import path
from . import views

urlpatterns = [
    path('', views.QuoteCategoryAPIView.as_view(), name="home"),
    path('quotes/', views.QuoteAPIView.as_view(), name="home2"),
]