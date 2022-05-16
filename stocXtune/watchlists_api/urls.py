from django.urls import path
from .views import WatchlistStocksDetail, WatchlistStocksList, StockList, StockDetail, UserWatchlistList, UserWatchlistDetail

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'watchlists_api'

urlpatterns = [
    path ('<int:pk>/',StockDetail.as_view(),name = 'stockdetail'),
    path ('',StockList.as_view(),name = 'stocklist'),
    path ('watchlistdetail/<int:pk>/',UserWatchlistDetail.as_view(),name = 'watchlist'),
    path ('watchlistlist/',UserWatchlistList.as_view(), name = 'watchlistlist'),   
    path ('watchliststocks/',WatchlistStocksList.as_view(), name = 'watchliststocks'),
    path ('watchliststocksdetail/<int:pk>/',WatchlistStocksDetail.as_view(), name = 'watchliststocksdetail'),
    
]

# path('', views.getRoutes, name = "routes"),
    # path('stocks/', views.getStocks, name = "stocks"),
    # path('stocks/<str:pk>/', views.getStock, name = "stock"),
    # path('userwatchlists/', views.getUserWatchlists, name = "userwatchlists"),
    # path('userwatchlists/<str:pk>/', views.getUserWatchlist, name = "userwatchlist"),
    # path('watchliststocks/', views.getWatchlistStocks, name = "watchliststocks"),
    # path('watchliststocks/<str:pk>/', views.getWatchliststock, name = "watchliststock"),
    
    

