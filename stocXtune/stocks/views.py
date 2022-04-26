from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from stocks.models import Stock
from stocks.models import UserWatchlist
from stocks.models import WatchlistStocks
from .serializers import StockSerializer
from .serializers import UserWatchlistSerializer
from .serializers import WatchlistStockSerializer

from rest_framework.permissions import IsAdminUser

class StockList(generics.ListCreateAPIView):
    #permission_classes =[IsAdminUser]
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
class StockDetail(generics.RetrieveAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
class UserWatchlistList(generics.ListCreateAPIView):
    queryset = UserWatchlist.objects.all()
    serializer_class = UserWatchlistSerializer
class UserWatchlistDetail(generics.RetrieveAPIView):
    queryset = UserWatchlist.objects.all()
    serializer_class = UserWatchlistSerializer
class WatchlistStocksList(generics.ListCreateAPIView):
    queryset = WatchlistStocks.objects.all()
    serializer_class = WatchlistStockSerializer
class WatchlistStocksDetail(generics.RetrieveAPIView):
    queryset = WatchlistStocks.objects.all()
    serializer_class = WatchlistStockSerializer








# @api_view(['GET'])
# def getRoutes(request):
#     routes = [
#         {
#             'Endpoint': '/stocks/',
#             'method': 'GET',
#             'body': None,
#             'description': 'Returns an array of stocks'
#         },
#         {
#             'Endpoint': '/stocks/id',
#             'method': 'GET',
#             'body': None,
#             'description': 'Returns a single stocks object'
#         },
#         {
#             'Endpoint': '/stocks/create/',
#             'method': 'POST',
#             'body': {'body': ""},
#             'description': 'Creates new stocks with data sent in post request'
#         },
#         {
#             'Endpoint': '/stocks/id/update/',
#             'method': 'PUT',
#             'body': {'body': ""},
#             'description': 'Creates an existing stocks with data sent in post request'
#         },
#         {
#             'Endpoint': '/stocks/id/delete/',
#             'method': 'DELETE',
#             'body': None,
#             'description': 'Deletes and exiting stocks'
#         },
#     ]
#     return Response(routes)

# @api_view(['GET'])
# def getStocks(request):
#     stocks = Stock.objects.all()
#     serializer = StockSerializer(stocks, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def getStock(request,pk):
#     stocks = Stock.objects.get(id=pk)
#     serializer = StockSerializer(stocks, many=False)
#     return Response(serializer.data)

# @api_view(['GET'])
# def getUserWatchlists(request):
#     userwatchlists = UserWatchlist.objects.all()
#     serializer = UserWatchlistSerializer(userwatchlists, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def getUserWatchlist(request,pk):
#     userwatchlists = UserWatchlist.objects.get(id=pk)
#     serializer = UserWatchlistSerializer(userwatchlists, many=False)
#     return Response(serializer.data)


# @api_view(['GET'])
# def getWatchlistStocks(request):
#     watchliststocks = WatchlistStocks.objects.all()
#     serializer = WatchlistStockSerializer(watchliststocks, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def getWatchliststock(request,pk):
#     watchliststocks = WatchlistStocks.objects.get(id=pk)
#     serializer = WatchlistStockSerializer(watchliststocks, many=False)
#     return Response(serializer.data)

