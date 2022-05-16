from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from watchlists_api.models import Stock
from watchlists_api.models import UserWatchlist
from watchlists_api.models import WatchlistStocks
from .serializers import StockSerializer
from .serializers import UserWatchlistSerializer
from .serializers import WatchlistStockSerializer

from rest_framework.permissions import IsAuthenticated

class StockList(generics.ListCreateAPIView):
    #permission_classes =[IsAdminUser]
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
class StockDetail(generics.RetrieveAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
class UserWatchlistList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = UserWatchlist.objects.all()
    serializer_class = UserWatchlistSerializer
class UserWatchlistDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = UserWatchlist.objects.all()
    serializer_class = UserWatchlistSerializer
class WatchlistStocksList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = WatchlistStocks.objects.all()
    serializer_class = WatchlistStockSerializer
class WatchlistStocksDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = WatchlistStocks.objects.all()
    serializer_class = WatchlistStockSerializer
    
#Crud classes for Watchlist
# class CreateWatchlist(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#     parser_classes = [MultiPartParser, FormParser]

#     def post(self, request, format=None):
#         print(request.data)
#         serializer = UserWatchlistSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class AdminWatchlistDetail(generics.RetrieveAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = UserWatchlist.objects.all()
#     serializer_class = UserWatchlistSerializer


# class EditWatchlist(generics.UpdateAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = UserWatchlistSerializer
#     queryset = UserWatchlist.objects.all()


# class DeleteWatchlist(generics.RetrieveDestroyAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = UserWatchlistSerializer
#     queryset = UserWatchlist.objects.all()


""" Concrete View Classes
#CreateAPIView
Used for create-only endpoints.
#ListAPIView
Used for read-only endpoints to represent a collection of model instances.
#RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
#DestroyAPIView
Used for delete-only endpoints for a single model instance.
#UpdateAPIView
Used for update-only endpoints for a single model instance.
##ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
#RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
#RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""






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

