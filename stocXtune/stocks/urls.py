from django.urls import path
from . import views
from .views import WatchlistStocksDetail, WatchlistStocksList, StockList, StockDetail, UserWatchlistList, UserWatchlistDetail

app_name = 'stocks'

urlpatterns = [
    path ('<int:pk>/',StockDetail.as_view(),name = 'stockdetail'),
    path ('',StockList.as_view(),name = 'stocklist'),
    path ('watchlistdetail/<int:pk>/',UserWatchlistDetail.as_view(),name = 'watchlist'),
    path ('watchlistdetail',UserWatchlistList.as_view(), name = 'watchlistlist'),
    path ('watchliststocks/<int:pk>/',WatchlistStocksList.as_view(), name = 'watchliststocks'),
    path ('watchliststocksdetail',WatchlistStocksDetail.as_view(), name = 'watchliststocksdetail'),
    
]

# path('', views.getRoutes, name = "routes"),
    # path('stocks/', views.getStocks, name = "stocks"),
    # path('stocks/<str:pk>/', views.getStock, name = "stock"),
    # path('userwatchlists/', views.getUserWatchlists, name = "userwatchlists"),
    # path('userwatchlists/<str:pk>/', views.getUserWatchlist, name = "userwatchlist"),
    # path('watchliststocks/', views.getWatchlistStocks, name = "watchliststocks"),
    # path('watchliststocks/<str:pk>/', views.getWatchliststock, name = "watchliststock"),