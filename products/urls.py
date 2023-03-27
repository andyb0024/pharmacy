from .views import ProductListView,ProductCreateView
from django.urls import path

urlpatterns = [
    path('list/', ProductListView.as_view()),
    path('create/', ProductCreateView.as_view()),
]