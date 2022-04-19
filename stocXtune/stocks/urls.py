from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name = "routes"),
    path('stocks/', views.getStocks, name = "stocks"),
    path('stocks/<str:pk>/', views.getStock, name = "stock"),
    path('userwatchlists/', views.getUserWatchlists, name = "userwatchlists"),
    path('userwatchlists/<str:pk>/', views.getUserWatchlist, name = "userwatchlist"),
    path('watchliststocks/', views.getWatchlistStocks, name = "watchliststocks"),
    path('watchliststocks/<str:pk>/', views.getWatchliststock, name = "watchliststock"),
]