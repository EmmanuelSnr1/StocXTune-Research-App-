from django.contrib import admin

from .models import Stock
from .models import UserWatchlist
from .models import WatchlistStocks
# Register your models here.

admin.site.register(Stock)
admin.site.register(UserWatchlist)
admin.site.register(WatchlistStocks)
