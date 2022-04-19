from curses.ascii import US
from rest_framework.serializers import ModelSerializer
from .models import Stock, WatchlistStocks
from .models import UserWatchlist
from .models import WatchlistStocks

class StockSerializer(ModelSerializer):
    class Meta: 
        model = Stock
        fields = '__all__'


class UserWatchlistSerializer(ModelSerializer):
    class Meta: 
        model = UserWatchlist
        fields = '__all__'

class WatchlistStockSerializer(ModelSerializer):
    class Meta: 
        model = WatchlistStocks
        fields = '__all__'
