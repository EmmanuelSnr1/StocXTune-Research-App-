from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.


class Stock(models.Model):
    ticker = models.CharField(max_length=10)

    def __str__(self):
        return self.ticker


class UserWatchlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="watchlist",null=True, blank=True)
    name = models.CharField(max_length=30)
    Description = models.TextField()

    def __str__(self):
        return self.name


class WatchlistStocks(models.Model):
    watchlistid = models.ForeignKey(UserWatchlist,on_delete=models.CASCADE)
    ticker = models.CharField(max_length=10)    

    def __str__(self):
        return self.ticker